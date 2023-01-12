from flask import (
    Blueprint, render_template
)
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/names/')
def names():
    db = get_db()
    rows = db.execute('SELECT COUNT (DISTINCT artist) FROM tracks').fetchall()
    return render_template('blog/artist.html', rows=rows)


@bp.route('/tracks/')
def tracks():
    db = get_db()
    rows = db.execute('SELECT COUNT (title) FROM tracks').fetchall()
    return render_template('blog/tracks.html', rows=rows)


@bp.route('/tracks/<genre>/')
def tracks_genre(genre):
    db = get_db()
    all_tracks = db.execute("SELECT * FROM tracks WHERE genre = ? COLLATE NOCASE", (genre,)).fetchall()
    return render_template('blog/tracks_genre.html', all_tracks_genre=len(all_tracks))


@bp.route('/tracks-sec/')
def tracks_sec():
    db = get_db()
    rows = db.execute('SELECT title, length / 1000.0 from tracks').fetchall()
    return render_template('blog/tracks_sec.html', rows=rows)


@bp.route('/tracks-sec/statistics/')
def tracks_statistics():
    db = get_db()
    total_length = db.execute('SELECT SUM(length) FROM tracks;').fetchall()
    avg = db.execute('SELECT AVG (ROUND(length / 1000.0)) FROM tracks;').fetchall()
    return render_template('blog/tracks_stats.html', total_length=total_length, avg=avg)





