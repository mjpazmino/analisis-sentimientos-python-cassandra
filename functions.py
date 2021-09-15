import meaningcloud
import pandas
from consts import MC_LICENSE


def obtener_obj_tweet(tweet):

    sentimiento = obtener_sentimiento(tweet.text)

    return {
        'nombreUsuario': tweet.user.screen_name,
        'textoTweet': tweet.text,
        'numFavoritos': tweet.favorite_count,
        'sentimientoTweet': sentimiento
    }


def obtener_sentimiento(txt_tweet):

    sentiment_request = meaningcloud.SentimentRequest(
        MC_LICENSE, lang='es', txt=txt_tweet, txtf='markup').sendReq()

    sentiment_response = meaningcloud.SentimentResponse(sentiment_request)

    if not sentiment_response.isSuccessful():
        sentimiento = "DES"
        return sentimiento

    sentimiento = sentiment_response.getGlobalScoreTag()
    return sentimiento
