'''posts models'''

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    '''Post'''
    tittle = models.CharField(max_length=255)
    photo = models.ImageField(upload_to= 'posts/photos')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    definition = models.TextField()

    sub_tittle = models.CharField(max_length=100, null=True)
    sub_definition = models.TextField(null=True)

    classification = models.CharField(max_length=20)
    color = models.CharField(max_length=40, default='white')
    recolector_avaliable = models.IntegerField()


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        ''' return tittle'''
        return '{} by @{}'.format(self.tittle, self.user.username)