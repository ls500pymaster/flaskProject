# from flask import Flask, request, render_template
# from faker import Faker
# import pandas as pd
# import requests
#
# fake = Faker()
# app = Flask(__name__)
#
#
# @app.route('/requirements/', methods=['GET'])
# def requirements():
#     with open('requirements.txt') as f:
#         lines = f.readlines()
#     return lines
#
#
# @app.route('/generate_users/', methods=['GET'])
# def generate_users(count=100):
#     count = int(request.args.get("count", 100))
#     new_list = []
#     for _ in range(count):
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
#     response = requests.get('http://api.open-notify.org/astros.json')
#     response.raise_for_status()
#     json_response = response.json()
#     for key, value in json_response.items():
#         print(value)
#     return render_template(
#         'cosmo.html',
#         title="SPACE",
#         cosmo=value,
#     )