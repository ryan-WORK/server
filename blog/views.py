from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
# from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from taggit.models import Tag

from .utils.alerts import BlogEmailErrors
from .models import Post
from .forms import EmailPostForm, SearchForm, CommentForm
# from django.conf import settings
from splashed.toolbox.email_service import o_o_mail
from .api.serializers import PostSerializer
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class DefAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('xapikey')
        if not token:
            return None

        try:
            user_token = Token.objects.get(key=token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user_token, None




def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'page': page,
                   'posts': posts,
                   'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(request.POST, request.user)
        # HERE ?
        if comment_form.is_valid():
            print('Post', request.POST['body'])
            print('User', request.user.username, CommentForm().Meta.fields)

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # # Assign the current post to the comment
            new_comment.email = request.user.email
            new_comment.post = post
            new_comment.name = request.user
            new_comment.body = request.POST['body']
            # # Save the comment to the database
            new_comment.save()
            print()
            try:
                print("email")
            except BlogEmailErrors():
                pass
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                 .order_by('-same_tags', '-publish')[:4]

    return render(request,
                  'blog/post/detail_no_auth.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST, request.user)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                                          post.get_absolute_url())
            subject = f'[CollegeBudgetStudio.com] {post.title}'
            gisting = '{}  recommends you reading "{}"'.format(request.user, post.title)
            message = f"Check out this post '{post.title}' \n {cd['name']} thinks : {cd['comments']}"
            person_from = '\n\n{} '.format(cd['name'])
            #  Old Email Dont Use
            # send_mail(subject, message, 'info@collegebudgetstudio.com', [cd['to']])
            o_o_mail(subject_mess=subject, title=subject, body=message, more="New Mail Testing =)", to_who=[cd['to']],
                     fromwho=person_from, gisting=gisting, app_url=post_url)
            sent = True
            # print('New Mail', request.user)

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            print(query)
            results = Post.objects.annotate(
                similarity=TrigramSimilarity('title', query),
            ).filter(similarity__gt=0.3).order_by('-similarity')
            print(results)

    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


class PostsViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


def app_about(request):
    return render(request, 'about.html', {})
