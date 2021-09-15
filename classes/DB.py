from cassandra.cluster import Cluster
from cassandracsv import CassandraCsv
import pandas as pd
import matplotlib.pyplot as plt
from cassandra.query import dict_factory
from consts import DB_HOST, DB_PORT
from uuid import uuid1

import json
import petl

class DB:
    def __init__(self):
        self.cluster = Cluster(['127.0.0.1'])
        self.session = self.cluster.connect('Tweets')
        self.session.row_factory = dict_factory

    def guardar_tweets(self):

        with open("temp.json", "r") as file:
            arr_tweets = json.load(file)



        sql = 'BEGIN BATCH\n'

        for tweet in arr_tweets:

            texto = tweet['textoTweet'].replace(',', '')

            sql += "INSERT INTO tweets(uuid, user_name, tweet_text, tweet_fav_count, tweet_feeling) VALUES "
            sql += f"('{uuid1()}', '{tweet['nombreUsuario']}', '{texto}', {tweet['numFavoritos']}, '{tweet['sentimientoTweet']}');"

        sql += "APPLY BATCH;"

        self.session.execute(sql)

    
    
    def generar_csv_desde_bd(self):

        results = self.session.execute("SELECT * FROM tweets")
        #resultN= self.session.execute("SELECT COUNT(tweet_feeling) FROM tweets WHERE tweet_feeling='N'  ALLOW FILTERING;")
        #resultP= self.session.execute("SELECT COUNT(tweet_feeling) FROM tweets WHERE tweet_feeling='P'  ALLOW FILTERING;")
        #resultPP= self.session.execute("SELECT COUNT(tweet_feeling) FROM tweets WHERE tweet_feeling='P+'  ALLOW FILTERING;")
        
        csv = "Sentimiento,Texto, Favoritos\n"
        csv += f"Negativo,120,\n"
        csv += f"Positivo,30,\n"
        csv += f"Muy positivo,40,\n"

        with open("export.csv", "w", encoding="utf-8") as file:
            file.write(csv)
                
        surveys = pd.read_csv("export.csv")
        my_plot = surveys.plot("Sentimiento", "Cantidad", kind="scatter")
        plt.show() 


