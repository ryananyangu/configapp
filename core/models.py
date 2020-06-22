from django.db import models

class ClientApiSetup(models.Model):
    API_CONNECTION_TYPE = [
        ('CUSTOM_SOCKET', 'CUSTOM_SOCKET'),
        ('HTTP', 'HTTP(S)'),
    ]

    REQUEST_TYPE = [
        ('JSON','JSON'),
        ('XML','XML/SOAP')
    ]


    class Meta:
        db_table = 'ClientApiSetups'
        managed = True
        verbose_name = "ClientApiSetups"
        verbose_name_plural = "ClientApiSetups"


    requestType = models.CharField(max_length=32,blank=False, null=False,db_index=True,choices=REQUEST_TYPE)
    hasCertificate = models.BooleanField(default=False)
    certificate = models.FileField(upload_to=".", max_length=100,null=True,blank=True)
    clientName = models.CharField(max_length=32,blank=False, null=False,unique=True,db_index=True)
    apiConnection = models.CharField(max_length=32,blank=False, null=False,db_index=True,choices=API_CONNECTION_TYPE)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.clientName
class HttpHeaders(models.Model):
    
    

    class Meta:
        db_table = 'httpheaders'
        managed = True
        verbose_name = "httpheaders"
        verbose_name_plural ="httpheaders"

    key = models.CharField(max_length=32,blank=False, null=False,db_index=True)
    value = models.CharField(max_length=32,blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key +" : "+ self.value

class Requests(models.Model):
    class Meta:
        db_table = 'Requests'
        managed = True
        verbose_name = "Requests"
        verbose_name_plural = "Requests"
    requestDestinationClient = models.ForeignKey(ClientApiSetup,on_delete=models.CASCADE)
    uri = models.CharField(max_length=160,blank=False, null=False)
    requestTemplate = models.TextField(blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)
    successResponseKey = models.CharField(max_length=160,blank=False, null=False)
    successExpectedValue = models.CharField(max_length=160,blank=False, null=False)



    def __str__(self):
        return self.requestDestinationClient.clientName


class PayloadKeys(models.Model):
    
    class Meta:
        db_table = 'PayloadKeys'
        managed = True
        verbose_name ="payloadkeys"
        verbose_name_plural = "payloadkeys"

    KeyName = models.CharField(max_length=32,blank=False, null=False,db_index=True)
    Description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.KeyName

class PayloadKeyRequestMapping(models.Model):
    class Meta:
        db_table = 'PayloadKeyRequestMapping'
        managed = True
        unique_together = (('request', 'payloadkey','placeholder'),)
        verbose_name = "payloadkeyrequestmapping"
        verbose_name_plural = "payloadkeyrequestmappings"
    request = models.ForeignKey(Requests,on_delete=models.CASCADE)
    payloadkey = models.ForeignKey(PayloadKeys,on_delete=models.CASCADE)
    placeholder = models.CharField(max_length=32,blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payloadkey.KeyName +":"+self.placeholder

class RequestHeaderMapping(models.Model):
    class Meta:
        db_table = 'RequestHeaderMapping'
        managed = True
        unique_together = (('request', 'headers'),)
        verbose_name = "RequestHeaderMapping"
        verbose_name_plural = "RequestHeaderMappings"

    request =  models.ForeignKey(Requests,on_delete=models.CASCADE)
    headers = models.ForeignKey(HttpHeaders,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.headers.key



class Response(models.Model):
    request = models.ForeignKey(Requests,on_delete=models.CASCADE)
    KeyName = models.CharField(max_length=160,blank=False, null=False)
    isArray = models.BooleanField(default=False) # Key name becomes the check param and value is extraxted from
    valueKeyName = models.CharField(max_length=160,blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('request', 'KeyName'),)
        verbose_name = "reponse"
        verbose_name_plural = "reponses"

    def __str__(self):
        return self.KeyName

class RequestExtraData(models.Model):
    
    response = models.ForeignKey(Response,on_delete=models.CASCADE)
    placeholder = models.CharField(max_length=32,blank=False, null=False,db_index=True)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'RequestExtraData'
        managed = True
        verbose_name = "RequestExtraData"
        verbose_name_plural = "RequestExtraDatas"

    def __str__(self):
        return self.KeyName
class ProcessFlow(models.Model):
    
    request = models.ForeignKey(Requests,on_delete=models.CASCADE)
    serviceID = models.CharField(max_length=32,blank=False, null=False,unique=True)
    serviceCode = models.CharField(max_length=32,blank=False, null=False,unique=True,db_index=True)
    priority = models.PositiveIntegerField(default=0)
    processname = models.CharField(max_length=32,blank=False, null=False)
    processDesc = models.TextField()
    isFinal = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'ProcessFlow'
        managed = True
        unique_together = (('request', 'serviceID','serviceCode'),)
        verbose_name = "processflow"
        verbose_name_plural = "processflows"

    def __str__(self):
        return self.serviceCode

class ClientStaticConfsPair(models.Model):
    client = models.ForeignKey(ClientApiSetup,on_delete=models.CASCADE)
    key = models.CharField(max_length=32,blank=False, null=False)
    value = models.CharField(max_length=32,blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ClientStaticConfs'
        managed = True
        unique_together = (('client', 'key','value'),)
        verbose_name = "clientstaticconfs"
        verbose_name_plural = "clientstaticconfs"

    def __str__(self):
        return self.key +" : "+ self.value