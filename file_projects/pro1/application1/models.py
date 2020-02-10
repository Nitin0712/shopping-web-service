from django.db import models
from django.contrib.auth.models import User


# Create your mdl_old here.
class product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.FloatField(blank=False, null=False)
    product_image = models.ImageField(upload_to="images/")
    product_createddate = models.DateTimeField(auto_now_add=True)
    product_updateddate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'

    def __self(self):
        return self.product_name


class product_cart(models.Model):
    cart_usr = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_quantity = models.IntegerField()
    cart_product = models.ForeignKey(product, on_delete=models.CASCADE)
    cart_createddate = models.DateTimeField(auto_now_add=True)
    cart_updateddate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_cart'


# Create your mdl_old here.
class product_quantity(models.Model):
    pro = models.ForeignKey(product, on_delete=models.CASCADE)
    pro_qnt_keep = models.IntegerField(blank=False, null=False)
    pro_qnt_in = models.IntegerField()
    pro_qnt_out = models.IntegerField()
    pro_createddate = models.DateTimeField(auto_now_add=True)
    pro_updateddate = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_quantity'


class testdb(models.Model):
    text = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        db_table = 'test'