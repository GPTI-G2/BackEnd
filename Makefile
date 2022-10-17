
.PHONY: up
up:
	docker-compose up --build

.PHONY: build
build:
	docker-compose build

.PHONY: down
down:
	docker-compose down

.PHONY: migrate!
migrate!:
	docker-compose run api python manage.py migrate

.PHONY: makemigrations!
makemigrations!:
	docker-compose run api python manage.py makemigrations

.PHONY: superup!
superup:
	docker-compose run api python manage.py makemigrations
	docker-compose run api python manage.py migrate
	docker-compose run api python manage.py loaddata store/seeds/*.json
	docker-compose up --build -d

.PHONY: black
black:
	docker-compose run api black ./*.py ./api/*.py ./store/*.py ./store/tests/*.py

# flake8:
# 	docker-compose run app flake8 *.py

.PHONY: pylint
pylint:
	docker-compose run api pylint  ./*.py ./api/*.py ./store/*.py ./store/tests/*.py

.PHONY: test
test:
	docker-compose run api pytest

.PHONY: supertest
supertest:
	sudo docker-compose run api python manage.py makemigrations
	sudo docker-compose run api python manage.py migrate
	sudo docker-compose run api pytest

.PHONY: seed-development
seeds!:
	docker-compose run api python manage.py loaddata store/seeds/*.json