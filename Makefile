down:
	docker-compose down

run-db:
	docker-compose up -d mongo
	docker-compose up -d mongo-express

run-api:
	docker-compose up api

run-all:
	docker-compose up

run-api-test:
	docker-compose run api  sh -c "pip install -r requirements_ci.txt && pytest --cov=. --cov-config=.coveragerc"