from django.db import models

class Register(models.Model):
	emailid= models.CharField(max_length=200)
	password= models.CharField(max_length=200)
	mobile= models.CharField(max_length=200)
	fullname= models.CharField(max_length=200)