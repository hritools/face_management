from django.db import models


class Camera(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Person(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Photo(models.Model):
    shot_date = models.DateTimeField('when the shot was taken')
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)
    picture = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['shot_date']),
        ]

    def __str__(self):
        return 'Cam: "{}" Date: {}'.format(self.camera, self.shot_date.date())


class PhotoIdentification(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    left = models.IntegerField(default=None)
    right = models.IntegerField(default=None)
    top = models.IntegerField(default=None)
    bottom = models.IntegerField(default=None)

    verified = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['person']),
            models.Index(fields=['photo']),
            models.Index(fields=['verified']),
        ]

    def __str__(self):
        return 'Seen "{}" at ({})'.format(self.person, self.photo)
