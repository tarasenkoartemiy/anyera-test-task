from django.db import models


def user_directory_path(instance, filename):
    return f'{instance.owner.username}/images/{filename}'


class Pet(models.Model):
    nickname = models.CharField(max_length=150)
    breed = models.CharField(max_length=150)
    image = models.ImageField(upload_to=user_directory_path)
    owner = models.ForeignKey('auth.User', related_name='pets', on_delete=models.CASCADE)