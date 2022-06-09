from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_puppies(request):
    puppies=[
        {
          'name':'Angela',
          'age':23
        },{
          'name':'Angela',
          'age':23
        }
    ]

    return JsonResponse(puppies,safe=False)