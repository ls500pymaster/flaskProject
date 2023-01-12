import os
from flask import Flask
from faker import Faker
fake = Faker()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # init commands from db.py
    from . import db
    db.init_app(app)
    db.init_artists(app)

    # @app.route('/requirements/')
    # def requirements():
    #     with open('requirements.txt', 'r') as f:
    #         lines = f.readlines()
    #     return lines
    #
    #
    # @app.route('/generate_users/', methods=['GET'])
    # def generate_users(count=100):
    #     args = request.args
    #     if "count" in args:
    #         count = int(request.args.get("count", default=100))
    #     new_list = []
    #     for i in range(count):
    #         new_list.append(fake.name())
    #         new_list.append(fake.email())
    #     return render_template('usernames.html', new_list=new_list)
    #
    #
    # @app.route('/mean/')
    # def mean():
    #     read_csv = pd.read_csv('../hw.csv')
    #     height = round(read_csv["height"].mean() * 2.54)
    #     weight = round(read_csv["weight"].mean() * 0.45359237)
    #     return render_template(
    #         'cosmo.html',
    #         title="HW.CSV",
    #         height=height,
    #         weight=weight,
    #     )
    #
    #
    # @app.route('/space/')
    # def space():
    #     response = req.get('http://api.open-notify.org/astros.json')
    #     response.raise_for_status()
    #     jsonResponse = response.json()
    #     for key, value in jsonResponse.items():
    #         print(value)
    #     return render_template(
    #         'cosmo.html',
    #         title="SPACE",
    #         cosmo=value,
    #     )

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/names/', endpoint='names')

    from . blog import tracks
    app.register_blueprint(blog.bp, name=tracks)
    app.add_url_rule('/tracks/', endpoint='tracks')

    from .blog import tracks_sec
    app.register_blueprint(blog.bp, name=tracks_sec)
    app.add_url_rule('/tracks-sec/', endpoint='tracks-sec')

    from .blog import tracks_genre
    app.register_blueprint(blog.bp, name=tracks_genre)
    app.add_url_rule('/tracks/', endpoint='tracks')

    from .blog import tracks_statistics
    app.register_blueprint(blog.bp, name=tracks_statistics)
    app.add_url_rule('/tracks/statistics/', endpoint='statistics')

    return app
