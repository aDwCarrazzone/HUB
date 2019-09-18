from mercadoLivreService import MercadoLivreService
import json

mlService = MercadoLivreService
application = mlService.getAccessToken(None)
user = mlService.getUser(None, "APP_USR-8786283849719360-091802-f8dce77e54ee4e34ba1205dd8886accf-471765183")
print(application)
print(user)
