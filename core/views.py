from django.contrib.auth import get_user_model, login, authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets, permissions, authentication, generics
from rest_framework.views import APIView
from core.documents import update as es_insert
from rest_framework import response
from .serializers import (
    UserSerializer
)
from .models import *

# Create your views here.
User = get_user_model()
class DefaulSettings(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25

    paginate_by_param = 'page_size'
    max_paginate_by = 100


class UserViewSet(DefaulSettings, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =UserSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [
        # permissions.AllowAny # Or anon users can't register
        permissions.IsAdminUser
    ]

class Configuration(DefaulSettings,APIView):


    def get(self, request, format=None):
        """
        Initiate congiration cache
        """
        documents = dict()
        request_document = dict()

        process_flows = list(ProcessFlow.objects.all().values())

        for process in process_flows:
            # print(process)
            request = list(Requests.objects.filter(id=process["request_id"]).values())[0]
            request_document["client"] = list(ClientApiSetup.objects.filter(id=request["requestDestinationClient_id"]).values())[0]
            if process["serviceCode"] not in documents.keys():
                request_document["serviceID"] = process["serviceID"]
                request_document["serviceCode"]=process["serviceCode"]
                request_document["process"] = [{
                    "request":request,
                    "response":list(Response.objects.filter(request=process["request_id"]).values()),
                    "statics":list(ClientStaticConfsPair.objects.filter(client=request["requestDestinationClient_id"]).values()),
                    "headers":list(RequestHeaderMapping.objects.filter(request=process["request_id"]).values('headers__key','headers__value')),
                    "valueMaps":list(PayloadKeyRequestMapping.objects.filter(request_id=process["request_id"]).values('payloadkey__KeyName','placeholder')),
                    "priority": process["priority"],
                    "isFinal": process["isFinal"],
                    "processName": process["processname"],
                }]
                documents[process["serviceCode"]] = request_document
            else:
                documents[process["serviceCode"]][process["serviceCode"]]["process"].append(
                    {
                        "request":request,
                        "response":list(Response.objects.filter(request=process["request_id"]).values()),
                        "statics":list(ClientStaticConfsPair.objects.filter(client=request["requestDestinationClient_id"]).values()),
                        "headers":list(RequestHeaderMapping.objects.filter(request=process["request_id"]).values('headers__key','headers__value')),
                        "valueMaps":list(PayloadKeyRequestMapping.objects.filter(request_id=process["request_id"]).values('payloadkey__KeyName','placeholder')),
                        "priority": process["priority"],
                        "isFinal": process["isFinal"],
                        "processName": process["processname"],
                    }
                )

        es_insert(documents.values())
        return response.Response(data=documents,status=status.HTTP_200_OK)


    def post(self, request, format=None):
        # print(request.data)
        request_document = dict()
        process_flows = list(ProcessFlow.objects.filter(serviceCode=request.data["serviceCode"]).values())

        for process in process_flows:
            request = list(Requests.objects.filter(id=process["request_id"]).values())[0]
            request_document["client"] = list(ClientApiSetup.objects.filter(id=request["requestDestinationClient_id"]).values())[0]
            request_document["serviceID"] = process["serviceID"]
            request_document["serviceCode"] = process["serviceCode"]
            request_document["process"] = [{
                "request":request,
                "statics":list(ClientStaticConfsPair.objects.filter(client=request["requestDestinationClient_id"]).values()),
                "response":list(Response.objects.filter(request=process["request_id"]).values()),
                "headers":list(RequestHeaderMapping.objects.filter(request=process["request_id"]).values('headers__key','headers__value')),
                "valueMaps":list(PayloadKeyRequestMapping.objects.filter(request_id=process["request_id"]).values('payloadkey__KeyName','placeholder')),
                "priority": process["priority"],
                "isFinal": process["isFinal"],
                "processName": process["processname"],
            }]
        # print(request_document)
        es_insert([request_document])
        return response.Response(data=request_document,status=status.HTTP_200_OK)