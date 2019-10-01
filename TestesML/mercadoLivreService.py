import json
import requests
import meli

header = json.load(open('config.json'))
client_id = header['TestDevelopers']['app_id']
client_secret = header['TestDevelopers']['secret_key']
redirect_uri = header['TestDevelopers']['redirect_uri']

class MercadoLivreService:
    def getCode(self):
        ml = meli.Meli(client_id=client_id, client_secret=client_secret)
        req = requests.get('https://auth.mercadolivre.com.br/authorization', 'response_type=code&client_id='+client_id)
        #ml.authorize(req, redirect_uri)
        return ml.auth_url(redirect_URI=redirect_uri)

    # def getAccessToken(self):
    #     redirect_uri = header['TestDevelopers']['redirect_uri']
    #     req = requests.get("api.mercadolibre.com/oauth/token?grant_type=authorization_code&client_id="+client_id+"&client_secret="+client_secret+"&code=TG-5d8834c6b2852d00064e9cc3-471765183&redirect_uri="+redirect_uri)
    #     response = req.content
    #     data = response.
    #     token = json.loads(data)
    #
    #     if response.getcode() == 200:
    #         return str(token["access_token"])
    #     elif response.getcode() == 400:
    #         return str(token['message'])

    # def getUser(self):
    #     token = MercadoLivreService.getAccessToken(self)
    #     con.request("GET", "/users/me?access_token="+token)
    #     response = con.getresponse()
    #     data = response.read()
    #     user = json.loads(data)
    #     return user
