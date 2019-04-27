

.PHONY: serve
serve:             ## make serve to serve docs
	@python manage.py runserver

.PHONY: app
app:
	@python manage.py startapp ${NEW}

.PHONY: migrate
migrate:
	@python manage.py makemigrations ${APP} && python manage.py migrate

.PHONY: image
image:             ## make image
	@docker build -t pwa


.PHONY: clean.docker
clean.docker:
	docker system prune --all --force --volumes
#
#
#SUBDIRS = conf master exporter slave
#
#.PHONY: kube.create
#kube.create:
#	@cd kubernetes && for dir in $(SUBDIRS); do \
#          kubectl create -f $$dir; \
#        done
#
#.PHONY: kube.delete
#kube.delete:
#	@cd kubernetes && for dir in $(SUBDIRS); do \
#              kubectl delete -f $$dir; \
#            done
#
#.PHONY: kube.start
#kube.start:
#	minikube start
#
#.PHONY: kube.stop
#kube.stop:
#	minikube stop
#
#.PHONY: kube.kill
#kube.kill:
#	minikube stop && minikube delete
#
#.PHONY: page
#page:
#	@touch ./docs/${NEW}.rst


