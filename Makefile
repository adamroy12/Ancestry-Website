tag=latest
organization=adamroy12
image=ancestry-website

build:
	docker build --force-rm $(options) -t ancestry-website:latest .

build-prod:
	$(MAKE) build options="--target production"

push:
	docker tag $(image):latest $(organization)/$(image):$(tag)
	docker push $(organization)/$(image):$(tag)

compose-start:
	docker-compose up --remove-orphans $(options) 

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(options) website python manage.py $(cmd)


start-server:
	python manage.py runserver 0.0.0.0:80

helm-deploy:
	helm upgrade --install ancestry-website ./helm/django-website

migrate:
	python manage.py migrate