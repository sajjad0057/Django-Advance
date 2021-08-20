from django.http import response
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from ipware import get_client_ip
import json,urllib


# Create your views here.


class UserLocationAPI(APIView):
    def get(self,request,format=None):
        client_ip ,is_routable = get_client_ip(request)
        if client_ip is None:
            client_ip = "0.0.0.0"
        else:
            if is_routable:
                ip_type = "public"
            else:
                ip_type = "private"
        #print("client_ip and ip_type ------>",client_ip,ip_type)

        ip_address = "103.106.239.94" # my public ip address
        url = "https://api.ipfind.com/?ip="+ip_address   # when deploy your site , use here client_ip instead of ip_address . 
        respon = urllib.request.urlopen(url)
        data_1 = json.loads(respon.read())

        data_1['client_ip'] = client_ip
        data_1['ip_type'] = ip_type

        #print('data_1 ----- >',data_1)


        
        return JsonResponse(data_1)





