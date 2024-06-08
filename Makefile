### Makefile

install:
	docker-compose exec python poetry install
run:
	docker-compose exec python poetry run python /app/main.py
