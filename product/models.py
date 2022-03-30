from django.db import models
from django.core.validators import *
from account.models import Store

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return (self.cat_name)


class Size(models.Model):
    sz_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return (self.sz_name)


class Color(models.Model):
    cl_name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return (self.cl_name)


class Product(models.Model):
    owner = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='owner')
    pr_name = models.CharField(max_length=50, validators=[RegexValidator(regex='[A-Za-z]', message='Please Enter Correct Name')])
    pr_description = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pr_name


class ProductDetail(models.Model):

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'size'),
        ('Color', 'color'),
        ('Size-Color', 'size-color')
        )
    pr_type = models.CharField(max_length=40, choices=VARIANTS, default="None")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="detail")
    pr_price = models.DecimalField(decimal_places=2, validators=[MinValueValidator(0.0), RegexValidator(regex='^[0-9]*$', message='Enter Correct Price')], max_digits=1000)
    pr_qunatity = models.IntegerField(default=1, validators=[MinValueValidator(1.0), RegexValidator(regex='^[0-9]*$', message='Enter Correct Value')])
    in_stock = models.BooleanField(default=False)
    pr_img = models.ImageField(upload_to='product/')
    pr_size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="size")
    pr_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="color", null=True, blank=True)

    def __str__(self) :
        return str(self.product.pr_name)    
