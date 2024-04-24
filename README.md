# TELEGRAM BOT NOTIFIER SERVER

## Python3.9 Flask3 Postgres16

## Setup

Make sure you have `docker` and `docker-compose` installed on your machine.

Create `.env` file using `.env_template`.

Commands

To build the project

    make

To migrate

    make migrate

To run the project

    make run

To jump into container

    $ make shell
    root@<containerid>:/project#

To stop running containers

    make stop
