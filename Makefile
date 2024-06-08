### Makefile

install:
	docker compose exec python poetry install
run:
	docker compose exec python poetry run python /app/delete_all.py
	docker compose exec python poetry run python /app/main.py
delete:
	docker compose exec python poetry run python /app/delete_all.py