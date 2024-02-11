.PHONY: migration run alembic migration

venv:
	python3 -m venv ./venv

migration:
	venv/bin/python -m alembic revision --autogenerate -m "$(MIG_NAME)"
	venv/bin/python -m alembic upgrade head

run:
	venv/bin/python -m bot
	# or just run bot.py using env