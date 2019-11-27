import json
import requests

#Por enquanto, o programa consegue pegar o access_token e com ele retornar as informações do usuario

header = json.load(open('config.json'))
client_id = header['TestDevelopers']['app_id']
client_secret = header['TestDevelopers']['secret_key']
redirect_uri = header['TestDevelopers']['redirect_uri']

class MercadoLivreService:
    def getCode(self):
        #TO DO: implementar nesse método a URL de redirecionamento certa e pegar o CODE contido nessa url
        #passando ele para o método getAccessToken
        req = requests.get('https://auth.mercadolivre.com.br/authorization?response_type=code&client_id='+client_id)
        response = req.url
        return response

    def getAccessToken(self, code: str):
        redirect_uri = header['TestDevelopers']['redirect_uri']
        params = {'grant_type': 'authorization_code', 'client_id': client_id, 'client_secret': client_secret, 'code': code, 'redirect_uri': redirect_uri}
        req = requests.post('https://api.mercadolibre.com/oauth/token', data=params)
        response = req.content
        data = json.loads(response)

        try:
            return data['access_token']
        except:
            return data['message']

    def getUser(self):
        token = MercadoLivreService.getAccessToken(self, 'AQUI VAI O CODE GERADO')
        req = requests.get("https://api.mercadolibre.com/users/me?access_token="+token)
        response = req.content
        user = json.loads(response)
        return user
