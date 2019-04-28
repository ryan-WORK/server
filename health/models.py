from django.db import models
from django.utils import timezone
from django.conf import settings


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Article(models.Model):
    PUBLICATION_TYPE = (
        ('acts', 'Acts'),
        ('measures', 'Measures'),
        ('facts', 'Facts'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='health_articles')
    body = models.TextField()
    answer = models.CharField(max_length=250, blank=True)
    image = models.URLField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    typeof = models.CharField(max_length=10,
                              choices=PUBLICATION_TYPE,
                              blank=True,
                              default='facts')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('blog:post_detail',
    #                    args=[self.publish.year,
    #                          self.publish.month,
    #                          self.publish.day,
    #                          self.slug])


class Response(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='response')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Response by {} on {}'.format(self.name, self.article)


class File(models.Model):
    response = models.ForeignKey(Response,
                                 on_delete=models.CASCADE,
                                 related_name='file')
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


class ArticleFile(models.Model):
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='afile')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
