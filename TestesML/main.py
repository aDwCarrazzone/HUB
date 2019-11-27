from mercadoLivreService import MercadoLivreService

mlService = MercadoLivreService
#accessToken = mlService.getAccessToken(None, 'TG-5d940c68d110490006a2e122-471765183')
#codeURL = mlService.getCode(None)
user = mlService.getUser(None)
print(user)
