from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyCustomUser(User):
    phone_number = models.CharField(max_length=15)  
    store_name = models.CharField(max_length = 200, null = True)
    store_location = models.CharField(max_length = 300, null = True)
    city = models.CharField(max_length = 100, null = True)
    area = models.CharField(max_length = 100, null = True)
    user_type =  models.CharField(max_length=20)  
    verifi = models.CharField(max_length = 100, null=True)
    wallet = models.IntegerField( null=True)

    def __str__(self):
        return self.username
    
    
class Topup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=150)
    amount = models.IntegerField()
    payment_verification = models.CharField(max_length=10)
    
class store_image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img1 = models.FileField(upload_to='uploads',null= True)

    
class games(models.Model):
    Game_name = models.CharField(max_length = 200)
    pic1 = models.FileField(upload_to='product_images', null= True)
  



    
class BilliardsGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_billiards = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class biillardsgamme_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20)
    

class add_games(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_game = models.CharField(max_length=15)  



class Snookergame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_snooker = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Snookergame_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20)
    



class Vrgame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_vr_device = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

class Vrgame_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20)

class BowlingGame_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20) 

class BowlingGame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_billiards = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class psgame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_ps_device = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class psgame_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20)
    
class pcgame_booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datte = models.CharField(max_length=100)
    number_of_billiards = models.CharField(max_length=100)
    in_time = models.CharField(max_length=100)
    out_time = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    store_location = models.CharField(max_length=300)
    mins = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    booking_id = models.CharField(max_length=100)
    time_of_booking = models.CharField(max_length=100)
    book_sta =  models.CharField(max_length=20)

class pcgame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_ps_device = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()


class kidsgame(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    open_time = models.TimeField()
    close_time = models.TimeField()
    description = models.TextField()