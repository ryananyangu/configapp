from django.contrib import admin
from .models import (
    HttpHeaders,
    RequestHeaderMapping,
    Requests,
    Response,
    RequestExtraData,
    PayloadKeyRequestMapping,
    PayloadKeys,
    ProcessFlow,
    ClientStaticConfsPair,
    ClientApiSetup,
    )

class ClientStaticConfsPairAdmin(admin.ModelAdmin):
    list_display =  ["client","key","value","date_created","date_modified"]
    list_filter = ("date_created",)
    search_fields = ("client__clientName","key","value","date_created","date_modified")
    
class ClientApiSetupAdmin(admin.ModelAdmin):
    list_display = ["requestType","hasCertificate","certificate","clientName","apiConnection","date_created","date_modified"]
    list_filter = ("date_created",)
    search_fields = ["requestType","hasCertificate","certificate","clientName","apiConnection","date_created","date_modified"]
    
# Register your models here.
class HttpHeadersAdmin(admin.ModelAdmin):
    list_display =  ["key","value","date_created","date_modified"]
    list_filter = ("date_created",)
    search_fields = ("key","value","date_created","date_modified")
class RequestHeaderMappingAdmin(admin.ModelAdmin):
    list_display =  ["request","headers","date_created","date_modified"]
    list_filter = ("date_created",)
    search_fields = ("request__requestDestinationClient","headers","date_created","date_modified")
    
class RequestsAdmin(admin.ModelAdmin):
    list_display =  ("requestDestinationClient",'uri',"successExpectedValue","successResponseKey",'requestTemplate','date_created','date_modified',)
    list_filter = ("date_created",)
    search_fields = ("requestDestinationClient",'uri',"successExpectedValue","successResponseKey",'requestTemplate','date_created','date_modified',)
    
class ResponseAdmin(admin.ModelAdmin):
    list_display =  ["request","KeyName","isArray","valueKeyName","date_created","date_modified"]
    list_filter = ("date_created",)
    search_fields = ["request__requestDestinationClient","KeyName","isArray","valueKeyName","date_created","date_modified"]

class RequestExtraDataAdmin(admin.ModelAdmin):
    list_display = ('response','placeholder','date_created','date_modified',)
    list_filter = ("date_created",)
    search_fields = ('response__KeyName','placeholder','date_created','date_modified',)
    
class PayloadKeyRequestMappingAdmin(admin.ModelAdmin):
    list_display = ("request","payloadkey","placeholder","date_created","date_modified",)
    list_filter = ("date_created",)
    search_fields = ("request__requestDestinationClient","payloadkey__KeyName","placeholder","date_created","date_modified",)

class PayloadKeysAdmin(admin.ModelAdmin):
    list_display = ["KeyName","Description","date_created","date_modified",]
    list_filter = ("date_created",)
    search_fields = ["KeyName","Description","date_created","date_modified",]
class ProcessFlowAdmin(admin.ModelAdmin):
    list_display = ("request","serviceID","serviceCode","priority","processname","processDesc","isFinal","date_created","date_modified",)
    list_filter = ("date_created",)
    search_fields = ("response__KeyName","serviceID","serviceCode","priority","processname","processDesc","isFinal","date_created","date_modified",)
    

admin.site.register(HttpHeaders,HttpHeadersAdmin)
admin.site.register(RequestHeaderMapping,RequestHeaderMappingAdmin)
admin.site.register(Requests,RequestsAdmin)
admin.site.register(Response,ResponseAdmin)
admin.site.register(RequestExtraData,RequestExtraDataAdmin)
admin.site.register(PayloadKeyRequestMapping,PayloadKeyRequestMappingAdmin)
admin.site.register(PayloadKeys,PayloadKeysAdmin)
admin.site.register(ProcessFlow,ProcessFlowAdmin)
admin.site.register(ClientApiSetup,ClientApiSetupAdmin)
admin.site.register(ClientStaticConfsPair,ClientStaticConfsPairAdmin)