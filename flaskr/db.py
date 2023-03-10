import sqlite3
import click
import pandas as pd
from flask.cli import with_appcontext
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')


@click.command(name='create')
@with_appcontext
def insert_artist():
    db = get_db()
    artists = pd.read_csv('./flaskr/top_tracks_of_2022_usa.csv')
    artists.to_sql('tracks', db, if_exists='replace', index=True)
    click.echo('Created and inserted tracks into DB.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


def init_artists(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(insert_artist)