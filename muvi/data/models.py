from django.db import models
from datetime import datetime

class content(models.Model):
    movie_id=models.IntegerField(default=00)
    movie_name=models.CharField(max_length=20,default="")
    store_id=models.IntegerField(default=00)
    alie_customer_id=models.IntegerField(default=00)

    def __str__(self):
        return self.movie_name

class User_data(models.Model):
    movie_id=models.IntegerField(default=00,null=True)
    user_id=models.IntegerField(default=00,null=True)
    timestamp=models.DateTimeField(default=datetime.now,null=True)
    user_email=models.EmailField(default="",null=True)
    user_name=models.CharField(max_length=20,default="")
    no_of_views=models.IntegerField(default=00,null=True)
    alie_customer_id=models.IntegerField(default=00,null=True)
    store_id=models.IntegerField(default=00,null=True)
    
    def __str__(self):
        return self.user_name

