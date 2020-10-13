from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Here you'll only find the photos which have a human face on it, and "
                        "some means of filtering: by the person identified, date and camera, unverified.")
