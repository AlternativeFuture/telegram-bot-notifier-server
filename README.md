# movads-backend

## Setup

* Create and activate virtual environment.
* Install requirements


    $ pip install -r requirements.txt


* Copy [README](migrations%2FREADME).env_example to .env
* Migrate database

    $ alembic init migrations
    $ alembic upgrade head


## Run the project

    $ export FLASK_APP=app
    $ flask run
    
## Hashing password manually as flask command

    $ flask hash-password <password>
    
## Create and delete admin users manually as flask command

    $ flask add-admin <username> <password>
    $ flask delete-admin <username>
