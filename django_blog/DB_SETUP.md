Database Setup Guide (PostgreSQL)

This project uses PostgreSQL as the database backend.

Follow the steps below after cloning the repository.

1. Install PostgreSQL (Ubuntu)
sudo apt update
sudo apt install postgresql postgresql-contrib


Verify installation:

sudo systemctl status postgresql


If not running:

sudo systemctl start postgresql
sudo systemctl enable postgresql

2. Create Database and User

Switch to the PostgreSQL system user:

sudo -i -u postgres
psql


Create the database and user:

CREATE DATABASE mydjangodb;

CREATE USER mydjangouser WITH PASSWORD 'mypassword';

ALTER ROLE mydjangouser SET client_encoding TO 'utf8';
ALTER ROLE mydjangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydjangouser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE mydjangodb TO mydjangouser;

3. Fix Schema Permissions (IMPORTANT)

PostgreSQL may not automatically grant schema ownership. Run:

\c mydjangodb

GRANT ALL ON SCHEMA public TO mydjangouser;
ALTER SCHEMA public OWNER TO mydjangouser;
ALTER DATABASE mydjangodb OWNER TO mydjangouser;


Exit:

\q
exit

4. Install PostgreSQL Driver in Virtual Environment

Activate your virtual environment, then:

pip install psycopg2-binary


If installation fails:

sudo apt install libpq-dev python3-dev
pip install psycopg2-binary

5. Apply Migrations
python manage.py migrate

6. Run Development Server
python manage.py runserver