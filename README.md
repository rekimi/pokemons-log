# Pokemon Logs
This serve a pokemon logs API using FASTAPI

# Requirements
- Python `3.10.6`
- Database `Postgresql`

## Setup & Installation
#### Create environment
`$: python -m venv pokemon-env `
#### Activate environment
`$: source pokemon-env/bin/activate `
#### Install packages
`$: pip install -r requirements.txt `
#### Setup .env
- copy `.env-sample` to `.env`
- modified the field to your local setup

## Database Migration
#### Create migration
- you dont need to create migration if nothing changes on models, you simply just migrate the database
- `$: alembic revision --autogenerate`
#### Migrate Databse
- `$: alembic upgrade head`

## Running
- `$: uvicorn src.main:app --reload ` default port is 8000, to change port, add `--port 1234`
## Accessing swagger
- Go to `localhost:port/docs`
