from datetime import datetime
from itertools import chain
from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
# Create your models here.

usernameValidator = UnicodeUsernameValidator()
class User(AbstractUser, UserManager):
    
    GENDER_OPTION = (
     ('male', 'male'),
     ('female', 'female'),   
    )
    def profile_picture_url(self,user,filename):
        user =AbstractUser.username
        return f'profile_pictures/{user}/profile{filename}'
    
    id = models.UUIDField(default=uuid.uuid4, db_index=True,unique=True, editable=False, primary_key=True)
    username = models.CharField(_('username'),unique=True, max_length=20, validators=[usernameValidator])
    email = models.EmailField(_('email address'), unique=True, null=False, blank=False)
    first_name = models.CharField(_('first name'), max_length=30, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_OPTION, max_length=6, null=True, blank=True)
    profile_picture = models.FileField(upload_to=profile_picture_url, null=True, blank=True)
    
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','gender']
    
    
    