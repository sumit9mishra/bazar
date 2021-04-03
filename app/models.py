from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

STATE_CHOICES = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Assam','Assam'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'), 
    ('Goa','Goa'),
    ('Gujarat','Gujarat'), 
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'), 
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Chandigarh','Chandigarh'),
    ('Dadra and Nagar Haveli','Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Lakshadweep','Lakshadweep'),
    ('Ladakh and Puducherry','Ladakh and Puducherry')
)

class Customer(models.Model):
    user= models.ForeignKey(User,on_delete = models.CASCADE)
    name= models.CharField(max_length=200)
    locality=models.CharField(max_length=250)
    city=models.CharField(max_length=50)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)


def __str__(self):
    return(self.id)


CATEGORY_CHOICES = (
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear')
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand = models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')

def __str__(self):
    return(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

def __str__(self):
    return(self.id)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')


