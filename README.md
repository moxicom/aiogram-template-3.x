# aiogram template v3.x with database (postgres sqlalchemy orm) migration
### by @moxicom

Start file is `bot.py` file.
SQLAlchemy ORM models are contained in the `repository/models.py` file.

 
1. Create venv by using `make venv` command.

2. Install requirements by using `requirements.txt`.

3. Create `.env` file

4. Make migration by using `make migration MIG_NAME=<my_migration_name>` command.

5. Run bot by using `make run` command.