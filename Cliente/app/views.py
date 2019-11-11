from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

import json
import urllib

# Create your views here.
@csrf_exempt
def login(request):
	if request.method == "GET":
		return render_to_response('login.html')
	else:

		usuario = request.POST['usuario']
		password = request.POST['pass']

		#------------------------------------

		#url = "http://APLICACION_API/URL_LOGIN"
		#data = urllib.urlopen(url)


		if usuario == "pepe" and password == "123":
			data = '''
			[{
  				"code": "200",
				"message" : "OK"
			}]
			'''
		else:
			data = '''
			[{
  				"code": "403",
				"message" : "Bad User"
			}]
			'''
		#--------------------------------
		jsonData = json.loads(data)
		if jsonData[0]["code"] == "200":
			return render_to_response("principal.html",{ 'mensaje' : 'ok'})
		else:
			return render_to_response("principal.html",{ 'mensaje' : 'usuario invalido'})
