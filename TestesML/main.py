from mercadoLivreService import MercadoLivreService

mlService = MercadoLivreService
#accessToken = mlService.getAccessToken(None)
codeURL = mlService.getCode(None)
#user = mlService.getUser(None)
print(codeURL)
#print(user)
