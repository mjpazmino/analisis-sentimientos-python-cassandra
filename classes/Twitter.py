from tweepy import OAuthHandler, API, Cursor


class Twitter:

    def __init__(self, API_KEY,
                 API_SECRET_KEY,
                 ACCESS_TOKEN,
                 ACCESS_TOKEN_SECRET):
        self.auth = OAuthHandler(
            API_KEY, API_SECRET_KEY)
        self.auth.set_access_token(
            ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def obtener_api(self):
        return API(self.auth)

    def obtener_cursor(args):
        return Cursor
