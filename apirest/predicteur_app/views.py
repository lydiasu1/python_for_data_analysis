from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Incident
from .serializers import IncidentSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # This is a view
    return HttpResponse("Your are on the main page: isn't it beautiful ?")

@csrf_exempt
def i_want_a_list(request):
    if request.method == "GET":
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        content = JSONParser().parse(request)
        serializer = IncidentSerializer(data = content)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def incident_detail(request, house_id):
    try:
        house = Incident.objects.get(pk=house_id)
    except Incident.DoesNotExist:
        return HttpResponse(str(incident_id), status=404)
    if request.method == "GET":
        serializer = IncidentSerializer(house)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        # je recup le content du request et parse en JSON
        content = JSONParser().parse(request)
        # je serialise le JSON en instance de House
        serializer = IncidentSerializer(house) # , data = content)
        #if serializer.is_valid():
        #    serializer.save()
        #    return JsonResponse(serializer.data, status=201)

        #return JsonResponse(serializer.errors, status=400)
        serializer.update(incident, content)

        return JsonResponse(serializer.data, status=201)
    elif request.method == "DELETE":
        incident.delete()
        return HttpResponse("Suppression faite!", status=204)

def predict_timecompletion(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = [
        "time_sys" ,         
        "active"   ,         
        "reassignment_count",
        "reopen_count"      ,
        "sys_mod_count"     ,
        "made_sla"          ,
        "impact"            ,
        "urgency"           ,
        "priority"          ,
        "knowledge"
    ]
    path_to_model   = "../../Projet_final/catboost.sav"
    path_for_scaler = "../../Projet_final/scaler.sav"
    unscaled_data   = [unscaled_data[colonne] for colonne in colonnes]
    model           = joblib.load(path_to_model)
    scaler          = joblib.load(path_for_scaler)
    print("GUTEN TAG")
    print([unscaled_data])
    donnees_scalees = scaler.transform([unscaled_data])
    print(donnees_scalees)
    timecompletion            = model.predict(donnees_scalees)
    print(timecompletion)
    return timecompletion

@csrf_exempt
def predict(request):
    """
    Renvoie une house avec la MEDV completee
    (Attend une MEDV innexistante == null)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        print("Rebonjour")
         
        data        = JSONParser().parse(request)
        

        serializer  = IncidentSerializer(data=data)

        if serializer.is_valid():
            print("HELLO")
            print(data)
            data["time_completion"]        = predict_timecompletion(data)
            print("COMO estas")
            print(data["time_completion"])
            serializer          = IncidentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)