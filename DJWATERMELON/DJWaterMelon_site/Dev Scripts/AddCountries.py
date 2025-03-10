import sqlite3 as sq3
import pandas as pd

countries_json = pd.read_json('DJWATERMELON/DJWaterMelon_site/Dev Scripts/countries.json')
print(countries_json['name'].values)

genres_json = pd.read_json('DJWATERMELON/DJWaterMelon_site/Dev Scripts/genres.json')
print(genres_json[0].values)

connection = sq3.connect("DJWATERMELON/DJWaterMelon_site/db.sqlite3")

cursor = connection.cursor()

"""
que = "INSERT INTO Collections_country (country_name) VALUES (?)"

for item in countries_json['name'].values:
    cursor.execute(que, (item,))
    connection.commit()
"""

"""
que = "INSERT INTO Collections_genre (genre_name) VALUES (?)"

for item in genres_json[0].values:
    cursor.execute(que, (item,))
    connection.commit()
"""