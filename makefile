.PHONY: migration install_dep run alembic migration

migration:
	venv/bin/python -m alembic revision --autogenerate -m "$(MIG_NAME)"
	venv/bin/python -m alembic upgrade head