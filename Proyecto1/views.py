from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

import datetime

import firebase_admin
from firebase_admin import credentials,   db

archivoJson = {
  "type": "service_account",
  "project_id": "login01-95537",
  "private_key_id": "30db6deac4a17892fb5e4f2c646586afb7883cd2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQClIYyYGS1GM/Io\nj7tRHrn30v7nk47XipF05vahGFxNYZ2iaMyxoG2duq+wqgU98/5gYcYiU64MuFpv\nPePTaXxYa8n/khlUGhAmjtxBIfIjFc4Rna7i60C/h3MGyrPMl7o/vorBDq02sVC/\ncgm+IpdInG2U0AVby8pxTs02CmTx5IWI139GVIkch6pVDZCeq3zsJZhXeG9Ed96c\ndlxtVt8OBUTKeEwhOoHVT0dSPYcyGtEKwH7dwHCqTU8k4h0f8b33AnaLbk/q69vF\nvjHd4V28tO5k/5FXub3O0yEEoUe6R7dqxRmE/TKCb9Ra156jFBHUl2QENiIeFabg\nGhyO/YpNAgMBAAECggEACxWAaWkvN8oe1Agpy50jYHYiNAsciG09rDogjdmjwHHv\n8cnVC4s4MGEqj9IpvenVxkRp1z4ErcfmEhd2ZmdrOEgr6+KznoiNUvk94YVUynQZ\nO+d4qLSfyPtfhjIu9Wmtz7+Lcr/4cnZedCtEaiXKP854MIfyBCJeuVJPxfPWqMHR\nRYSbcmlxHGfvwbKU6RhPFRgWGo9rxVGY37RgAgJsIpiKH82un1ZF2PLMqp/zUroy\nU0zLilGZz5lkXNMlkwpbloDgB0VMqVE5KMMQfKGYGJpLHNz7j9i6s5OeD+3fMY6F\nC4AUk5Rr7hGdSYw/nfNbFpP+WwlK8eAjA6ZEj7v3YQKBgQDnVuy7r3f3Ac2+J9u8\nD13XOcdXbIgPNPr03KkDJGhhERZhWoXmhT0jkksjT/P1Y758/sAYBcWFTbJG//Yy\naN53JNUaekBJlVCqfuYRjdgwrqpDI1M7J1wtrBqzpDjHFws60dbMO7ui6R/oNx4e\nO2JUfhet78MdHM5ZtNFj9+umBQKBgQC2u9iq2vTOwKM3j3dlbRJk9d1XDWsH9+XE\n89BkQumYaFJrEeo5jfiG/EWEH1lX67gKZrh7YUEJb9s5Ib/XCMj7swQRgsHm/VS/\nrk1RCiON4URbWHrngwsvZcz9ughMhzP0iUTkQ42XmeuwmLlCW4h6IF9qty7fzv5F\n6DoaERL9qQKBgHZAfKpDu3LLvTuibDPpNvK5WihaFgKP9mgME2jDx4c2kNYay69W\nFDaGpVnbmLyqy8hhABhHevv1B1g7psGF0ZHdhgEO1KXIaX99dmUquIPKBMZk3Dq0\nl+3Qt6V0IIHESb07Xizvq65OtDyjUAXsHQtLmRcUJAxRmTlJsG8FX7NxAoGBAIbh\nBL6oO4bYniEGnoSZC7jF2gjFeLk6+7hyluFKmo3KgvtRD+hHqKhKUS2CzjmdXg0f\nYRCA6raCf/gdtzKL434V1uzt7R4I46NQjvVAXJn/KquaFa4JBhqIM9Ucmb+TFIBt\nShKK4lqCXHvPXv9h/MzYVFW6vLiqWvlSvoA7Fh9xAoGBANSsJnZhFNlnx0+bRdU2\n75iAawM9SESiMr3r9wFTr/yL1MlPtN5AWaDkaJSsF1LD6UTEs0kuQ5QpUzi1/H8G\nry32LQMgXjcjuCt4ZY+q0l5pmWhFi6nEEb0IPtTkweay0cAECu/RzQHRKIZlN+tO\ntQBvqoCzmUNVoXybajbvpAKY\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-si8g1@login01-95537.iam.gserviceaccount.com",
  "client_id": "100510942606386207841",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-si8g1%40login01-95537.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
firebase_sdk = credentials.Certificate(archivoJson)
firebase_admin.initialize_app(firebase_sdk,{'databaseURL':'https://login01-95537-default-rtdb.firebaseio.com/'})


def busqueda_productos(request):
    return render(request, "busqueda_productos.html") 

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido


def saludo (request):

    p1=Persona("Profesor Juan","Diaz")

    temasDelCurso = ["01","02","03","04","05"]

    #nombre = "Juan"

    #apellido = "Diaz"

    ahora = datetime.datetime.now()

    doc_externo=open("C:/Users/davgz/OneDrive/Escritorio/proyecto1/Proyecto1/Proyecto1/plantillas/login02.html")
    
    plt = Template(doc_externo.read())
    
    doc_externo.close()

    #ctx = Context({"nombre_persona":nombre,"apellido_persona":apellido,"momento_actual":ahora})

    ctx = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":temasDelCurso})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Adios mundo")

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h1>
    Fecha y Hora actuales: %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad, agno):

    #edadActual = 18
    periodo = agno - 2019
    edadfutura = edad + periodo
    documento="<html><body><h1>En el año %s tendrás %s años</h1></body></html>" %(agno,edadfutura)

    return HttpResponse(documento)