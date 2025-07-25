from django.db import models
from accounts.models import User
from menu.models import FoodItem
from vendor.models import Vendor
# Create your models here.

class Payment(models.Model):
    PAYMENT_METHOD=(
        ('PayPal','PayPal'),
        ('RazorPay','RazorPay')
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_id=models.CharField(max_length=100)
    payment=models.CharField(choices=PAYMENT_METHOD,max_length=100)
    amount=models.CharField(max_length=10)
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id
    
class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Complete'),
        ('Cancelled','Cancelled'),
    )
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    payment=models.ForeignKey(Payment,on_delete=models.SET_NULL,blank=True,null=True)
    vendors=models.ManyToManyField(Vendor, blank=True)
    order_number=models.CharField(max_length=20)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,blank=True)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=100)
    country=models.CharField(max_length=15,blank=True)
    state=models.CharField(max_length=15,blank=True)
    city=models.CharField(max_length=50,blank=True)
    pin_code=models.CharField(max_length=10)
    total=models.FloatField()
    tax_data = models.JSONField(blank=True, help_text = "Data format: {'tax_type':{'tax_percentage':'tax_amount'}}", null=True)
    total_data = models.JSONField(blank=True, null=True)
    total_tax = models.FloatField()
    payment_method=models.CharField(max_length=25)
    status=models.CharField(choices=STATUS,max_length=15,default='New')
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def order_placed_to(self):
        return ", ".join([str(i) for i in self.vendors.all()])
    
    def __str__(self):
        return self.order_number
    
class OrderedFood(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem=models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fooditem.food_title    