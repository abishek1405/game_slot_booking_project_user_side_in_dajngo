"""
URL configuration for got_target project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gotapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('Billiards/',views.Billiards),
    path('Bowling/',views.Bowling),
    path('Snooker/',views.Snooker),
    path('VR_games/',views.VR_games),
    path('KIDS GAMES/',views.Kids_game),
    path('PS_GAMES/',views.PS_GAMES),
    path('PC_Games/',views.PC_GAMES),
    path('Billiards_booking/<id>',views.Billiards_booking),
    path('Bowling_booking/<id>',views.Bowling_booking),
    path('Snooker_booking/<id>',views.snookers_booking),
    path('VR_games_booking/<id>',views.VR_games_booking),
    path('Kids_game_booking/<id>',views.Kids_game_booking),
    path('PS_GAMES_booking/<id>',views.PS_GAMES_booking),
    path('PC_Games_booking/<id>',views.PC_Games_booking),
    path('contact_more',views.contact_more),
    path('support_more',views.support_more),
    path('contact_more',views.contact_more),
    path('contact_more',views.contact_more),
    path('singup/',views.signup),
    path('logout/',views.logout),
    path('order_sucess/',views.order_sucess),
    path('terms/',views.terms),
    path('filter-data/', views.billard_filter_data, name='filter_data'),
    path('snookers_filter_data/', views.snookers_filter_data, name='snookers_filter_data'),
    path('VR_games_filter_data/', views.VR_games_filter_data, name='VR_games_filter_data'),
    path('ps_games_filter_data/', views.ps_games_filter_data, name='ps_games_filter_data'),
    path('pc_games_filter_data/', views.pc_games_filter_data, name='pc_games_filter_data'),
    path('bowling_filter_data/', views.bowling_filter_data, name='bowling_filter_data'),
    path('your_order/',views.your_order),
    path('history_order/',views.history_order),
    path('galler/<id>/',views.galler),
    path('billiards_cancelation/<id>/',views.billiards_cancelation),
    path('snooker_cancelation/<id>/',views.snooker_cancelation),
    path('vr_cancelation/<id>/',views.vr_cancelation),
    path('ps_cancelation/<id>/',views.ps_cancelation),
    path('pc_cancelation/<id>/',views.pc_cancelation),
    path('bowling_cancelation/<id>/',views.bowling_cancelation),
    path('our_service/',views.our_service),
    path('tournament/',views.tournament)
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'gotapp.views.custom_404'

