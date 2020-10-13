from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from photos.models import Photo, PhotoIdentification


def index(request):
    return render(request, 'management/index.html')


def photos(request):
    latest_photos = Photo.objects.order_by('-shot_date')[:4]
    not_verified = Photo.objects.filter(verified=False)[:4]
    context = {
        'latest_photos': latest_photos,
        'not_verified': not_verified,
    }
    return render(request, 'photos/index.html', context)


# def unlabeled(request):
    # latest_photos = Photo.objects.order_by('-verified')[:4]
    # context = {}
    # return render(request, 'photos/index.html', not_verified)
