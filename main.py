import consts
import json
import matplotlib.pyplot as plt
from functions import obtener_obj_tweet

from classes.DB import DB
from classes.Twitter import Twitter

if __name__ == '__main__':

    db = DB()
    twitter = Twitter(consts.API_KEY, consts.API_SECRET_KEY,
                      consts.ACCESS_TOKEN, consts.ACCESS_TOKEN_SECRET)

    api = twitter.obtener_api()
    cursor = twitter.obtener_cursor()

    # Parametros de busqueda Tweets
    search_term = "ecuador AND covid OR SARS-CoV-2 AND vacunacion OR vacuna"

    #tweet_list = cursor(
    #    api.search, q=params_busqueda, lang="es").items(20)

    tweet_listM = cursor(api.search,
                q=search_term,
                lang="es",
                since='2021-06-01',
                until='2021-06-15').items(200)  

    temp_arrM = [obtener_obj_tweet(tweet) for tweet in tweet_listM]

    tweet_listJ = cursor(api.search,
                q=search_term,
                lang="es",
                since='2021-06-16').items(200)  

    temp_arrJ = [obtener_obj_tweet(tweet) for tweet in tweet_listJ]
    
    def graficar(temp_arr, mitad): 
        n = 0
        p = 0
        neutro = 0
        pp=0
        #    print(type(temp_arr))
        for t in temp_arr:
            for a in t: 
                valor = t[a]
                if valor == 'N':
                    n = n + 1
                if valor == 'P':
                    p= p + 1
                if valor == 'P+':
                    pp = pp + 1
                if valor == 'NONE':
                    neutro = neutro + 1
            #print(valor)
            
        #print('Negativo: '+str(n) + 'Positivo:'+ str(p)+' Muy positivo:' + str(pp) +' Neutro:' + str(neutro))
            
        eje_x = ['Muy positivo', 'Positivo', 'Neutro', 'Negativo']
        eje_y = [pp,p,neutro,n]
        plt.bar(eje_x, eje_y)
        plt.ylabel('Cantidad de tweets')
        plt.xlabel('Sentimiento')
        plt.title('Opinión general sobre la vacuna de la '+mitad+' mitad del mes de Junio')
        plt.show()
            
        with open("temp.json", "w") as file:
            file.write(json.dumps(temp_arr))

        db.guardar_tweets()

    graficar(temp_arrM,'primera')
    graficar(temp_arrJ,'segunda')
