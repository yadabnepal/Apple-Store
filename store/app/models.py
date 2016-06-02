from django.db import models

# Create your models here.

class products(models.Model):
	product=models.CharField(max_length=50)
	model=models.CharField(max_length=50)
	color=models.CharField(max_length=20)
	size=models.CharField(max_length=20)
	price=models.CharField(max_length=20)
	details=models.TextField()
	photo=models.ImageField(upload_to ='media/',default='images/default.jpg')
	
	def __str__(self) :
		return self.product

class payments(models.Model):
	prodmodel=models.CharField(max_length=50)
	productid=models.IntegerField(default=0)
	username=models.CharField(max_length=50)
	prodcolor=models.CharField(max_length=50)
	prodsize=models.CharField(max_length=50)
	prodprice=models.CharField(max_length=50)
	cardtype=models.CharField(max_length=50)
	cardnumber=models.IntegerField()
	expiryyear=models.CharField(max_length=50)
	expirymonth=models.CharField(max_length=50)
	cvv=models.IntegerField()
	cardname=models.CharField(max_length=50)
	country=models.CharField(max_length=50)
	address1=models.CharField(max_length=50)
	address2=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	postalcode=models.IntegerField()
	phonenumber=models.IntegerField()
	email=models.CharField(max_length=50)
	userid=models.IntegerField()
	date=models.DateTimeField()
	status=models.CharField(max_length=50)
	
	def __str__(self) :
		return self.prodmodel

	
class userprofiles(models.Model):
	userid=models.CharField(max_length=50)
	dob=models.DateField(null=True)
	country=models.CharField(max_length=50)
	state=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	phone=models.CharField(max_length=50)
	mobile=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	userphoto=models.ImageField(upload_to ='media/',default='images/default.jpg')
	
	def __str__(self) :
		return self.userid
		
class comments(models.Model):
	username = models.CharField(max_length=50)
	productid = models.IntegerField(blank=True, null=True)
	userid = models.IntegerField(blank=True, null=True)
	comment = models.TextField()
	
	def __str__(self) :
		return self.username