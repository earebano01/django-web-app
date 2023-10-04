from django.db import models

class Products(models.Model):
    title       = models.fields.CharField(max_length=10)
    description = models.fields.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    stock       = models.IntegerField(default=0)
    date        = models.DateField(auto_now_add=True)
    time        = models.TimeField(auto_now_add=True)
    status      = models.BooleanField(null=True)
    lastorder   = models.FloatField(max_length=10, default=10.10)
    s_website   = models.URLField(max_length=200, default="www.supplier.com")
    s_contact   = models.EmailField(max_length=50, default="email@supplier.com")


