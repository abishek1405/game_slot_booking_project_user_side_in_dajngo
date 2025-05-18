from django.shortcuts import render,redirect
from .models import MyCustomUser,games,add_games,pcgame,pcgame_booking ,BowlingGame_booking,BowlingGame,BilliardsGame,Snookergame,Vrgame,kidsgame,psgame,store_image,biillardsgamme_booking,Snookergame_booking,Vrgame_booking,psgame_booking
from django.contrib.auth import authenticate as auth_authenticate 
from django.contrib.auth import  login as auth_login 
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log
from django.contrib import messages
from datetime import timedelta,datetime,time
from django.http import JsonResponse
import random
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

# import razorpay
# razorpay_client = razorpay.Client(auth=("rzp_test_ZojpdQzln8sxDW", "0PTHh9RHoXBeoZFlU8CJCZGe"))
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def tournament(request):
    return render(request, 'tournament.html')

def our_service(request):
    return render(request, 'our_service.html')


def billiards_cancelation(request,id):
    data = biillardsgamme_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')

def pc_cancelation(request,id):
    data = pcgame_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')

def bowling_cancelation(request,id):
    data = BowlingGame_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')

def snooker_cancelation(request,id):
    data = Snookergame_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')

def vr_cancelation(request,id):
    data = Vrgame_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')

def ps_cancelation(request,id):
    data = psgame_booking.objects.get(id = id)
    store_det = MyCustomUser.objects.get(store_name = data.store_name)
    # store_det.wallet += 5
    # store_det.save() 
    data.book_sta = 'canceled'
    data.save()
    return redirect('/your_order')


def galler(request,id):
    data = MyCustomUser.objects.get(store_name = id)
    image_data = store_image.objects.filter(user_id = data.id)
    return render(request, 'images.html', {'data': data,'image_data':image_data})


def history_order(request):
    user = request.user
    today = timezone.now().date()
    
    try:
       if request.user.is_authenticated:
            biillardsgamme_booking_data = biillardsgamme_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            Snookergame_booking_data = Snookergame_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            Vrgame_booking_data = Vrgame_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            psgame_booking_data = psgame_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            bowling_booking_data = BowlingGame_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            pcgame_booking_data = pcgame_booking.objects.filter(user = user.id, datte__lt=today).order_by('datte','in_time')
            return render(request,'history_orders.html',{'pcgame_booking_data':pcgame_booking_data,'bowling_booking_data':bowling_booking_data,'biillardsgamme_booking_data' : biillardsgamme_booking_data,'Snookergame_booking_data' : Snookergame_booking_data,'Vrgame_booking_data' : Vrgame_booking_data,'psgame_booking_data' : psgame_booking_data})
       else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/history_orders')
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (Vrgame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'Kids game or user not found.'})


from datetime import timedelta
from django.utils import timezone

def your_order(request):
    user = request.user
    today = timezone.now().date()
    
    try:
        if request.user.is_authenticated:
            biillardsgamme_booking_data = biillardsgamme_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            Snookergame_booking_data = Snookergame_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            Vrgame_booking_data = Vrgame_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            psgame_booking_data = psgame_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            pcgame_booking_data = pcgame_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            bowling_booking_data = BowlingGame_booking.objects.filter(user=user.id, datte__gte=today, book_sta='booked').order_by('datte', 'in_time')
            return render(request, 'your_orders.html', {
                'pcgame_booking_data': pcgame_booking_data,
                'bowling_booking_data': bowling_booking_data,
                'biillardsgamme_booking_data': biillardsgamme_booking_data,
                'Snookergame_booking_data': Snookergame_booking_data,
                'Vrgame_booking_data': Vrgame_booking_data,
                'psgame_booking_data': psgame_booking_data
            })
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type='user')
                
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    
                    return redirect('/your_order')
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (Vrgame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'Kids game or user not found.'})




def logout(request):
    log(request)
    return redirect('/')  


def terms(request):
    return render(request, 'terms.html')







@csrf_exempt
def  pc_games_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = pcgame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = pcgame_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)



def PC_Games_booking(request, id):
    try:
        billiards_game_instance = pcgame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = (billiards_game_instance.price) * 100
        
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_ps_device
            num_of_table_list = range(1, (int(no_table) + 1))
            
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')



                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/PC_Games_booking/{id}')
                
                current_time = datetime.now()
                if current_time.date() > datetime.strptime(date, "%Y-%m-%d").date() or (current_time.date() == datetime.strptime(date, "%Y-%m-%d").date() and current_time.time() >= in_timee.time()):
                    messages.error(request, "Please choose a different time as the selected time has passed.")
                    return redirect(f'/PC_Games_booking/{id}')
                
                conflicting_bookings = pcgame_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    book_sta = 'booked',
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )
                
                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    return redirect(f'/PC_Games_booking/{id}')
                
                time_difference = (out_timee - in_timee).total_seconds() / 60
                mins = int(time_difference)
                
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = 'GOT' + str(no_4_random)
                user = request.user
                
                pcgame_booking.objects.create(book_sta='booked',store_location=store_details.store_location,user=user,datte=date,number_of_billiards=number_of_billiards,in_time=in_time,out_time=out_time,store_name=store_name,mins=mins,cost=cost,booking_id=booking_id,time_of_booking=time_of_booking)
                
                store_details.wallet -= 20
                store_details.save()
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            
            return render(request, 'Pc_booking_slot.html', {'id': id, 'currency_change': currency_change, 'table': store_details, 'game_details': billiards_game_instance, 'num_billiards_list': num_of_table_list})
        
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')
                
                user = auth_authenticate(request, username=username, password=password, user_type='user')
                
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30))
                    
                    return redirect(f'/PC_Games_booking/{id}')
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')
    
    except (pcgame.DoesNotExist, MyCustomUser.DoesNotExist):
        return render(request, 'error.html', {'error_message': 'PS game or user not found.'})











@csrf_exempt
def  ps_games_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = psgame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = psgame_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)


def PS_GAMES_booking(request, id):
    try:
        billiards_game_instance = psgame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = (billiards_game_instance.price)*100
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_ps_device
            num_of_table_list = range(1, (int(no_table)+1)) 
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')

                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/PS_GAMES_booking/{id}')

                
                

                conflicting_bookings = psgame_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    book_sta = 'booked',
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )
                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    print('hi')
                    return redirect('/PS_GAMES_booking/{}'.format(id))
                time_difference = int((in_timee - out_timee).total_seconds() / 60)
                mins = time_difference
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = 'GOT'+str(no_4_random)
                user = request.user

                psgame_booking.objects.create(book_sta = 'booked', store_location = store_details.store_location,user = user,datte = date,number_of_billiards = number_of_billiards,in_time = in_time,out_time = out_time,store_name = store_name,mins = mins,cost = cost,booking_id = booking_id,time_of_booking = time_of_booking)
                store_details.wallet -= 20
                store_details.save()
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            return render(request, 'Ps_booking_slot.html', {'id':id,'currency_change':currency_change,'table': store_details,'game_details':billiards_game_instance,'num_billiards_list':num_of_table_list})

            
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/PS_GAMES_booking/{}'.format(id))
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (psgame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'PS game or user not found.'})



def Kids_game_booking(request, id):
    try:
        billiards_game_instance = kidsgame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        
        
        if request.user.is_authenticated:


            return render(request, 'Kids_booking_slot.html', {'table': store_details,'game_details':billiards_game_instance})
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/Kids_game_booking/{}'.format(id))
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (Vrgame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'Kids game or user not found.'})


@csrf_exempt
def  VR_games_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = Vrgame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = Vrgame_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def VR_games_booking(request, id):
    try:
        billiards_game_instance = Vrgame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = (billiards_game_instance.price)*100
        
        
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_vr_device
            num_of_table_list = range(1, (int(no_table)+1))  # Example list of billiard options
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')

                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/VR_games_booking/{id}')


                x = datetime.now()
                in_timeee = in_timee.time()
                if x.time() >= in_timeee and x.date() >= datetime.strptime(date, "%Y-%m-%d").date():
                    messages.error(request, "Please choose a different time as the selected time has passed.")
                    return redirect(f'/VR_games_booking/{id}')
                
                conflicting_bookings = Vrgame_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    book_sta = 'booked', 
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )

                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    print('hi')
                    return redirect('/VR_games_booking/{}'.format(id))
                time_difference = int((in_timee - out_timee).total_seconds() / 60)
                mins = time_difference
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = 'GOT'+str(no_4_random)
                user = request.user
                Vrgame_booking.objects.create(book_sta = 'booked',store_location = store_details.store_location,user = user,datte = date,number_of_billiards = number_of_billiards,in_time = in_time,out_time = out_time,store_name = store_name,mins = mins,cost = cost,booking_id = booking_id,time_of_booking = time_of_booking)
                store_details.wallet -= 20
                store_details.save()
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            return render(request, 'VR_booking_slot.html', {'id':id,'currency_change':currency_change,'table': store_details,'game_details':billiards_game_instance,'num_billiards_list':num_of_table_list})
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/VR_games_booking/{}'.format(id))
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (Vrgame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'VR game or user not found.'})


@csrf_exempt
def snookers_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = Snookergame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = Snookergame_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def snookers_booking(request, id):
    try:
        billiards_game_instance = Snookergame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = (billiards_game_instance.price)*100
        
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_snooker
            num_of_table_list = range(1, (int(no_table)+1))  # Example list of billiard options
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')

                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/Snooker_booking/{id}')



                x = datetime.now()
                in_timeee = in_timee.time()
                if x.time() >= in_timeee and x.date() >= datetime.strptime(date, "%Y-%m-%d").date():
                    messages.error(request, "Please choose a different time as the selected time has passed.")
                    return redirect(f'/Snooker_booking/{id}')
                
                conflicting_bookings = Snookergame_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    book_sta = 'booked',
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )
                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    print('hi')
                    return redirect('/Snooker_booking/{}'.format(id))
                time_difference = int((in_timee - out_timee).total_seconds() / 60)
                mins = time_difference
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = 'GOT'+str(no_4_random)
                user = request.user
                Snookergame_booking.objects.create(book_sta = 'booked',store_location = store_details.store_location,user = user,datte = date,number_of_billiards = number_of_billiards,in_time = in_time,out_time = out_time,store_name = store_name,mins = mins,cost = cost,booking_id = booking_id,time_of_booking = time_of_booking)
                store_details.wallet -= 20
                store_details.save()
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            return render(request, 'snookers_booking_slot.html', {'id':id,'currency_change':currency_change,'table': store_details,'game_details':billiards_game_instance,'num_billiards_list':num_of_table_list})
            #return render(request, 'snookers_booking_slot.html', {'table': store_details,'game_details':snookers_game_instance,'num_billiards_list':num_of_table_list})
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/Snooker_booking/{}'.format(id))
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (Snookergame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'Snooker game or user not found.'})













@csrf_exempt
def bowling_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = BowlingGame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = BowlingGame_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)




from datetime import datetime, timedelta


def Bowling_booking(request, id):
    try:
        billiards_game_instance = BowlingGame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = billiards_game_instance.price * 100
        
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_billiards
            num_billiards_list = range(1, int(no_table) + 1)
            
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')


                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/Bowling_booking/{id}')





                x = datetime.now()
                in_timeee = in_timee.time()
                if x.time() >= in_timeee and x.date() >= datetime.strptime(date, "%Y-%m-%d").date():
                    messages.error(request, "Please choose a different time as the selected time has passed.")
                    return redirect(f'/Bowling_booking/{id}')
                
                conflicting_bookings = BowlingGame_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    store_name=store_details.store_name,
                    book_sta='booked',
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )
                
                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    return redirect(f'/Bowling_booking/{id}')

                
                time_difference = int((out_timee - in_timee).total_seconds() / 60)
                mins = time_difference
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = f'got{no_4_random}'
                user = request.user
                
                BowlingGame_booking.objects.create(
                    book_sta='booked',
                    store_location=store_details.store_location,
                    user=user,
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    in_time=in_time,
                    out_time=out_time,
                    store_name=store_name,
                    mins=mins,
                    cost=cost,
                    booking_id=booking_id,
                    time_of_booking=time_of_booking
                )
                store_details.wallet -= 20
                store_details.save()
                
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            
            return render(request, 'bowling_booking_slot.html', {
                'id': id,
                'currency_change': currency_change,
                'table': store_details,
                'game_details': billiards_game_instance,
                'num_billiards_list': num_billiards_list
            })
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')
                user = auth_authenticate(request, username=username, password=password)
                
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30))
                    
                    return redirect(f'/Bowling_booking/{id}')
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')
    
    except (BowlingGame.DoesNotExist, MyCustomUser.DoesNotExist):
        return render(request, 'error.html', {'error_message': 'Billiards game or user not found.'})




















@csrf_exempt
def billard_filter_data(request):
    if request.method == "POST":
        try:
            print("Request body:", request.body)  
            data = json.loads(request.body.decode('utf-8'))
            selected_date = data['date']
            id = data['id']
            billiards_game_instance = BilliardsGame.objects.get(id=id)
            store_details = MyCustomUser.objects.get(id=billiards_game_instance.user_id)
            date = datetime.strptime(selected_date, '%Y-%m-%d').date()
            filtered_data = biillardsgamme_booking.objects.filter(datte=date, store_name=store_details.store_name,book_sta = 'booked')
            data_list = list(filtered_data.values(
                'user__username', 'datte', 'in_time', 'out_time', 'number_of_billiards'
            ))
            return JsonResponse(data_list, safe=False)
        except Exception as e:
            return JsonResponse({"error": "An error occurred while filtering data"}, status=500)
    return JsonResponse({"error": "Invalid request method"}, status=400)




def Billiards_booking(request, id):
    try:
        billiards_game_instance = BilliardsGame.objects.get(id=id)
        user_id = billiards_game_instance.user_id
        store_details = MyCustomUser.objects.get(id=user_id)
        currency_change = (billiards_game_instance.price)*100
        
        if request.user.is_authenticated:
            no_table = billiards_game_instance.no_of_billiards
            num_billiards_list = range(1, (int(no_table)+1)) 
            if request.method == 'POST':
                date = request.POST.get('date')
                number_of_billiards = request.POST.get('number_of_billiards')
              
                in_time = request.POST.get('open-time')
                out_time = request.POST.get('close-time')
                store_name = request.POST.get('store_name')
                in_timee = datetime.strptime(in_time, "%H:%M")
                out_timee = datetime.strptime(out_time, "%H:%M")
                normalized_close_time = billiards_game_instance.close_time
                if normalized_close_time == time(0, 0):
                    normalized_close_time = time(23, 59, 59)
                if not (billiards_game_instance.open_time <= in_timee.time() <= normalized_close_time and
                        billiards_game_instance.open_time <= out_timee.time() <= normalized_close_time):
                    messages.error(request, f"Please choose a time between {billiards_game_instance.open_time.strftime('%H:%M')} and {normalized_close_time.strftime('%H:%M')}.")
                    return redirect(f'/Billiards_booking/{id}')
                x = datetime.now()
                in_timeee = in_timee.time()
                if x.time() >= in_timeee and x.date() >= datetime.strptime(date, "%Y-%m-%d").date():
                    messages.error(request, "Please choose a different time as the selected time has passed.")
                    return redirect(f'/Billiards_booking/{id}')
                

                conflicting_bookings = biillardsgamme_booking.objects.filter(
                    datte=date,
                    number_of_billiards=number_of_billiards,
                    store_name = store_details.store_name,
                    book_sta = 'booked',
                    in_time__lt=out_timee.strftime("%H:%M"),
                    out_time__gt=in_timee.strftime("%H:%M")
                )
                if conflicting_bookings.exists():
                    messages.error(request, "Please choose a different table or timing because the slot is already booked.")
                    print('hi')
                    return redirect('/Billiards_booking/{}'.format(id))
                time_difference = int((in_timee - out_timee).total_seconds() / 60)
                mins = time_difference
                cost = request.POST.get('cost')
                time_of_booking = datetime.now()
                no_4_random = random.randint(1000, 9999)
                booking_id = 'GOT' + str(no_4_random)
                user = request.user
                biillardsgamme_booking.objects.create(book_sta = 'booked',store_location = store_details.store_location, user = user,datte = date,number_of_billiards = number_of_billiards,in_time = in_time,out_time = out_time,store_name = store_name,mins = mins,cost = cost,booking_id = booking_id,time_of_booking = time_of_booking)
                store_details.wallet -= 20
                store_details.save()
                
                request.session['success_message'] = booking_id
                return redirect('/order_sucess')
            return render(request, 'billiards_booking_slot.html', {'id':id,'currency_change':currency_change,'table': store_details,'game_details':billiards_game_instance,'num_billiards_list':num_billiards_list})
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                remember_me = request.POST.get('remember_me')  
                user_type = 'user'
                user = auth_authenticate(request, username=username, password=password, user_type = 'user')
                if user is not None:
                    my_user = MyCustomUser.objects.get(username=username)
                    if my_user.user_type == 'user':
                        auth_login(request, user)
                    else:
                        return render(request, 'login.html', {'error': 'Invalid username or password'})
                    if not remember_me:
                        request.session.set_expiry(timedelta(days=30)) 
                    return redirect('/Billiards_booking/{}'.format(id))
                else:
                    return render(request, 'login.html', {'error': 'Invalid username or password'})
            else:
                return render(request, 'login.html')  
    except (BilliardsGame.DoesNotExist, MyCustomUser.DoesNotExist) as e:
        return render(request, 'error.html', {'error_message': 'Billiards game or user not found.'})


def order_sucess(request):
    success_message = request.session.pop('success_message', None)
    print(success_message)
    return render(request,'order_success.html',{'data':success_message})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('mail')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone_number = request.POST.get('number')

        if MyCustomUser.objects.filter(username=username).exists():
            error_message = 'Username is already taken. Please choose another one.'
            messages.error(request, error_message)
            return render(request, 'signup.html', {'error_message': error_message})
        
        if MyCustomUser.objects.filter(phone_number=phone_number).exists():
            error_message = 'number is already registered. Please choose another number.'
            messages.error(request, error_message)
            return render(request, 'signup.html', {'error_message': error_message})

        if not username or not email or not password1 or not password2:
            error_message = 'Please fill in all required fields.'
            messages.error(request, error_message)
            return render(request, 'signup.html', {'error_message': error_message})

        if password1 != password2:
            error_message = 'Passwords do not match.'
            messages.error(request, error_message)
            return render(request, 'signup.html', {'error_message': error_message})

        user = MyCustomUser.objects.create_user(username=username,user_type = 'user', email=email, password=password1, phone_number=phone_number)
        return redirect('/')
    return render(request, 'signup.html')



def contact_more(request):
    data = '''
        <h3>1. Customer Support:</h3> <p>Our dedicated customer support team is here to assist you every step of the way. Whether you have a query, need assistance with booking slots, or require technical support, our knowledgeable representatives are just a message away. Reach out to us via live chat on our website, drop us an email, or give us a call. We strive to provide prompt and helpful responses to ensure your experience with us is smooth and hassle-free.</p> <h3>2. Social Media:</h3> <p>Stay connected with us on social media platforms to stay updated with the latest news, promotions, and announcements. Follow us on Facebook, Twitter, Instagram, and LinkedIn to join our community of users. Engage with us, share your experiences, and interact with other users. We value your feedback and suggestions, and social media is a great platform for us to stay connected with you on a more personal level.</p> <h3>3. Newsletter Subscription:</h3> <p>Sign up for our newsletter to receive exclusive offers, updates, and tips directly to your inbox. Be the first to know about new features, upcoming events, and special promotions. Our newsletter keeps you informed and engaged, ensuring you never miss out on any exciting developments or opportunities.</p> <h3>4. Feedback and Suggestions:</h3> <p>Your feedback is invaluable to us as we continuously strive to improve and enhance our services. Whether you have suggestions for new features or improvements to existing ones, we want to hear from you!  Share your thoughts, ideas, and concerns with us through our feedback form or email. Your input helps us tailor our services to better meet your needs and expectations.</p> <h3>5. Community Forums:</h3> <p>Join our community forums to connect with other users, share tips and tricks, and participate in discussions related to slot booking and gaming. Our forums provide a platform for users to interact, seek advice, and share their experiences. It's a vibrant community where users can come together to learn, collaborate, and engage with each other.</p>
    '''
    data_safe = mark_safe(data)
    return render(request, 'more.html', {'data': data_safe})



def support_more(request):
    data = '''
        <h3>1. Email:</h3>
        <p>Feel free to drop us an email at contact@example.com with any inquiries or concerns you may have. Our dedicated team will make sure to respond to your email promptly and provide you with the assistance you need.</p>

        <h3>2. Live Chat Support:</h3>
        <p>Need immediate assistance? Our live chat support feature allows you to chat with a member of our customer support team in real-time. Simply visit our website and look for the chat icon in the bottom corner. We're available to help you with any questions or issues you may encounter during your slot booking process.</p>

        <h3>3. Phone Support:</h3>
        <p>If you prefer speaking to someone directly, you can reach us via phone at +91 7200234540. Our friendly customer support representatives are available during business hours to address your concerns and provide you with personalized assistance.</p>

        <h3>4. Social Media:</h3>
        <p>Connect with us on social media platforms such as Facebook, Twitter, Instagram, and LinkedIn. Follow our pages to stay updated on the latest news, promotions, and announcements. It's also a great way to engage with us and share your experiences with our services.</p>

        <h3>5. Feedback Form:</h3>
        <p>We value your feedback as it helps us improve and enhance our services. If you have any suggestions, ideas, or feedback you'd like to share with us, please fill out our feedback form on our website. Your input is invaluable to us, and we appreciate you taking the time to help us better serve you.</p>
    '''
    data_safe = mark_safe(data)
    return render(request, 'more.html', {'data': data_safe})





def index(request):
    data = games.objects.all()
    city_data = MyCustomUser.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_add_games ON gotapp_mycustomuser.user_ptr_id = gotapp_add_games.user_id;")
    city_dataa = set()  
    for x in city_data:
        city_dataa.add(x.city)  
    
    # if request.method == 'POST':
    #     city = request.POST.get('city_name')
    #     if city:
    #         city_data = MyCustomUser.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_billiardsgame ON gotapp_mycustomuser.user_ptr_id = gotapp_billiardsgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
    #         location = city

    return render(request, 'index.html', {'data': data, 'city_data': city_dataa})




def PC_GAMES(request):
    data = pcgame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_pcgame ON gotapp_mycustomuser.user_ptr_id = gotapp_pcgame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'PC_Games')
    location = 'Location'
    game_name = 'PC_Games'  
    display_game_name ='PC Games' 
    filter_cancel = game_name
    print(data)
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = pcgame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_pcgame ON gotapp_mycustomuser.user_ptr_id = gotapp_pcgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})




def PS_GAMES(request):
    data = psgame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_psgame ON gotapp_mycustomuser.user_ptr_id = gotapp_psgame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'PS_GAMES')
    location = 'Location'
    game_name = 'PS_GAMES'  
    display_game_name ='PS Games' 
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = psgame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_psgame ON gotapp_mycustomuser.user_ptr_id = gotapp_psgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})


def Bowling(request):
    data = BowlingGame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_bowlinggame ON gotapp_mycustomuser.user_ptr_id = gotapp_bowlinggame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'Bowling')
    location = 'Location'
    game_name = 'Bowling' 
    display_game_name ='Bowling Games'  
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = BowlingGame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_bowlinggame ON gotapp_mycustomuser.user_ptr_id = gotapp_bowlinggame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})



def Kids_game(request):
    data = kidsgame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_kidsgame ON gotapp_mycustomuser.user_ptr_id = gotapp_kidsgame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'Kids_game')
    location = 'Location'
    game_name = 'Kids game'  
    display_game_name ='Kids Games' 
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = kidsgame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_kidsgame ON gotapp_mycustomuser.user_ptr_id = gotapp_kidsgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})

def VR_games(request):
    data = Vrgame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_vrgame ON gotapp_mycustomuser.user_ptr_id = gotapp_vrgame.user_id WHERE  wallet>=100;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'VR_games')
    location = 'Location'
    game_name = 'VR_games'  
    display_game_name ='VR Games'  
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = Vrgame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_vrgame ON gotapp_mycustomuser.user_ptr_id = gotapp_vrgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})


def Snooker(request):
    data = Snookergame.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_snookergame ON gotapp_mycustomuser.user_ptr_id = gotapp_snookergame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'Snooker')
    location = 'Location'
    game_name = 'Snooker' 
    display_game_name ='Snooker Games'  
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')        
        if city:  
            data = Snookergame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_snookergame ON gotapp_mycustomuser.user_ptr_id = gotapp_snookergame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})



def Billiards(request):
    data = MyCustomUser.objects.raw('SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_billiardsgame ON gotapp_mycustomuser.user_ptr_id = gotapp_billiardsgame.user_id;')
    city_data = MyCustomUser.objects.values('city').distinct()
    game_image = games.objects.get(Game_name = 'Billiards')
    location = 'Location'
    game_name = 'Billiards'
    display_game_name = 'Pool Table'  
    filter_cancel = game_name
    if request.method == 'POST':
        city = request.POST.get('city_name')
        print(city)        
        if city:  
            data = BilliardsGame.objects.raw("SELECT * FROM gotapp_mycustomuser INNER JOIN gotapp_billiardsgame ON gotapp_mycustomuser.user_ptr_id = gotapp_billiardsgame.user_id WHERE gotapp_mycustomuser.city = %s;", [city])
            location = city
    return render(request, 'game_slot.html', {'display_game_name':display_game_name,'data': data,'game_image':game_image, 'city_data': city_data, 'location': location, 'game_name': game_name,'filter_cancel':filter_cancel})









# def login(request):
#     try:
#         if request.user.is_authenticated:
#                 return redirect('/dashboard')
#         else:
#             if request.method == 'POST':
#                 username = request.POST.get('username')
#                 password = request.POST.get('password')
#                 remember_me = request.POST.get('remember_me')  
#                 user = auth_authenticate(request, username=username, password=password)
#                 if user is not None:
#                     print('hi')
#                     auth_login(request, user)
#                     if not remember_me:
#                        request.session.set_expiry(timedelta(days=30)) 
#                     return redirect('/dashboard')  
#                 else:          
#                     return render(request, 'login.html', {'error': 'Invalid username or password'})
#     except:     
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             print(username)
#             password = request.POST.get('password')
#             remember_me = request.POST.get('remember_me')  
#         user = auth_authenticate(request, username=username, password=password)
#         if user is not None:
#             auth_login(request, user)
#             if not remember_me:            
#                 request.session.set_expiry(timedelta(days=30)) 
#             return redirect('/dashboard')  
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
#     return render(request, 'login.html')




