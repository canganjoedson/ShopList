

Initiate Poetry
```bash
poetry new <projectname>
poetry add <packagename>
poetry shell #activate .venv
```

Initiate Alembic
```bash
#alembic init foldername
alembic init alembic
alembic revision -m "init" #create migrations
```

Create sqlite3 database
```bash
sqlite3 shoplist.db
```

Update all migrations availables
```bash
alembic upgrade head #apply migrations
alembic downgrade base #undo migrations to the base
alembic history #show history
alembic history -i #show current status
```

Open database and check
```bash
sqlite3 shoplist.db
.tables #show tables
.schema #show schema
```

### SQLACodeGen to work with database first -: existing database and generate code

```bash
poetry add sqlacodegen
sqlacodegen sqlite:///shoplist.db

sqlacodegen sqlite:///shoplist.db > models.py #generate models
```

### Obs release candidate for SQLACodeGen

To generate all existing tables
```bash
poetry add sqlacodegen==3.0.0rc1
sqlacodegen --generator tables sqlite:///shoplist.db
```

### To create auto generated migrations
```bash
alembic revision --autogenerate -m "hashed_password added to table user"
alembic upgrade +1 #or alembic upgrade head(top) to apply migrations
```

### Offline migrations
```bash
alembic upgrade +1 --sql > xpto.sql
```

### Compare types require change on env.py

```python
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        render_as_batch=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            render_as_batch=True,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()
```

### Batch operation required to apply alter table
```python
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashed_password', sa.String(length=100)))
```