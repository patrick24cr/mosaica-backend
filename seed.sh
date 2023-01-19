#!/bin/bash
rm -rf rarev2api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations moasaicaapi
python3 manage.py migrate moasaicaapi
python3 manage.py loaddata users
python3 manage.py loaddata tiles
python3 manage.py loaddata responseSets
python3 manage.py loaddata userTileScores
python3 manage.py loaddata questions
python3 manage.py loaddata badQuestionReports
