from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.migrations import operations
from django.core.validators import MaxLengthValidator, RegexValidator


#validators=[RegexValidator(
            #regex=r'^@.$',
           # message= 'Email must consist of username followed by one at, one domain and at least one dot. '
       # )]
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, 
    unique=True,
    validators=[RegexValidator(
        regex = r'^@\w{3,}$',
        message = ' Username must consists of @ followed by at least 3 alphanumericals. '
    )])
    first_name = models.CharField(max_length=50, blank=False, unique= False)
    last_name = models.CharField(max_length=50, blank=False, unique= False)
    email= models.EmailField(unique=True,blank=False)
    bio = models.CharField(max_length=520, blank=True, unique=False)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=False)
    textline = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]





        

    

