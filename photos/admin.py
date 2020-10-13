from django.contrib import admin

from photos.models import Camera, Person, Photo, PhotoIdentification

admin.site.register(Camera)
admin.site.register(Person)
admin.site.register(Photo)
admin.site.register(PhotoIdentification)
