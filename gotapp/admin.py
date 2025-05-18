from django.contrib import admin
from .models import MyCustomUser,games,add_games,pcgame,pcgame_booking ,BowlingGame_booking,BowlingGame,BilliardsGame,Snookergame,Vrgame,kidsgame,psgame,store_image,biillardsgamme_booking,Snookergame_booking,Vrgame_booking,psgame_booking
# Register your models here.



admin.site.register((MyCustomUser,
                     games,
                     add_games,
                     BilliardsGame,
                     Snookergame,
                     Vrgame,
                     kidsgame,
                     psgame,
                     store_image,
                     biillardsgamme_booking,
                     psgame_booking
                     ))
