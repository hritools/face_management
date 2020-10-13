from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Here goes all you'll need to label photos, "
                        "cluster photos, and retrain using new data.")
