from django.db import models

# Create your models here.
class BaseClass(models.Model):
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True

class User(models.Model):
	email = models.CharField(max_length=100)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	shipping_address = models.CharField(max_length=150)

class Cart(BaseClass):
	cart_code = models.IntergerField()
	total_price = models.FloatField()
	products = models.ForeignKey(Product, on_delete=models.CASCADE)
	is_paid = models.BooleanField()

class Product(models.Model):
	price = models.FloatField()
	name = models.CharField(max_length=100)
	desc = models.CharField(max_length=255)
