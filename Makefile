RUN=docker compose run --rm app

run:
	docker compose run --service-ports --rm app

stop:
	docker compose down

migrate:
	$(RUN) alembic upgrade head
