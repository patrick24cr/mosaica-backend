#!/bin/bash
rm -rf server/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations mosaicaapi
python3 manage.py migrate mosaicaapi
python3 manage.py loaddata users
python3 manage.py loaddata tiles
python3 manage.py loaddata responseSets
python3 manage.py loaddata userTileScores
python3 manage.py loaddata questions
#python3 manage.py loaddata badQuestionReports
