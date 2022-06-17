from http.client import responses
from django.http import HttpResponse

class AuthMiddleWare():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        # print("My Cool Middle Ware is running")
        # response=self.get_response(request)
        # return HttpResponse(f"Some Cool Response") 
        try:
                print("My cool Middle ware is running") #Code to execute
               
                response=self.get_response(request)
                token=""
                print(request.headers)
                if 'token' in request.headers:
                    token=request.headers['token']
                    print("Found Token")
                else:
                    return HttpResponse("Provide Auth Token") 
                
                #JWT VERIY
                if token !="valid token":
                    
                    print("Token is not Valid")
                    return HttpResponse("Token Not Valid") 
                
                # return HttpResponse("Hey Middle Ware IS what you will find")
                return response
        except Exception as e:   
               print(e)
               return HttpResponse(f"Error :{e}") 
