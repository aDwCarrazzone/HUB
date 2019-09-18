import json
import http.client

con = http.client.HTTPSConnection("api.mercadolibre.com")
header = json.load(open('config.json'))
data = {}

class MercadoLivreService:
    def getAccessToken(self):
        client_id = header['TestDevelopers']['app_id']
        client_secret = header['TestDevelopers']['secret_key']
        redirect_uri = header['TestDevelopers']['redirect_uri']
        con.request("POST", "/oauth/token?grant_type=authorization_code&client_id="+client_id+"&client_secret="+client_secret+"&code=TG-5d81783708a5ed00060a336d-471765183&redirect_uri="+redirect_uri)
        response = con.getresponse()
        data = response.read()
        return data

    def getUser(self, token):
        con.request("GET", "/users/me?access_token="+token)
        response = con.getresponse()
        user = response.read()
        return user
