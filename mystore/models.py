from django.db import models
from django.contrib.auth.models import User

# Create your models here.# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=264,unique=True)
    fee = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return str(self.name)

#Tao class UserProfileInfor
class UserProfileInfo(models.Model):
    #create relationship from this class to User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #add any more attribute you want
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to = "images/", blank=True)

    def __str__(self):
        return self.user.username