### Features

`flask --app flaskr init-db`  - init empty db
`flask --app flaskr create` - init db with tracks

PATH: /names/ - total unic artists

PATH: /tracks/ - total tracks

PATH: /tracks/genre - rock, pop, dance etc...

PATH: /tracks-sec/ - title and length of track

PATH: /tracks-sec/statistics/ - avg length and total length of all tracks

PATH: /requirements/ - Check requirements.txt for this project

PATH: /generate_users/ + GET - Generate random name+email

PATH: /mean/ - Mean of CSV table

PATH: /space/ - Count astronauts in real time


### CSV

You need spotify account. Go to https://watsonbox.github.io/exportify/
and export .csv file with tracks.
Put your .csv file to flaskr directory.

You can change path and name of .csv file here:
`/flaskr/db.py` at line 44
