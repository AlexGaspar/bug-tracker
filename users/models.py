from django.db import models
from parse_rest.datatypes import Object
from parse_rest.user import User as ParseUser

# Create your models here.
class User(ParseUser):
  pass