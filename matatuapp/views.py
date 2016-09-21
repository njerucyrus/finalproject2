from django.shortcuts import *
from django.contrib.auth import authenticate, login, logout
from matatuapp.models import *
from matatuapp.forms import *


# def book_seat(request):
#     if request.method == 'POST':
#         form = BookSeatForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             source = cd['source']
#             destination = cd['destination']
#             amount = cd['amount']
#             # get the fare
#             route = Routes.objects.get(source=source, destination=destination)
#             fare = int(route.fare)
#             username = request.session.get('username', '')
#             vehicle = Vehicle.objects.get(route=route)
#             print username
#             user = User.objects.get(username=username)
#             passager = Passager.objects.get(user=user)
#             booking = Booking.objects.create(
#                 passager=passager,
#                 vehicle=vehicle,
#                 source=source,
#                 amount_paid=amount
#             )
#             booking.save()
#             message = "Booking Made Successfully"
#             return render(request, 'book_seat.html', {'message': message, })
#
#         # create booking
#     else:
#         form = BookSeatForm()
#     return render(request, 'book_seat.html', {'form': form, })


def register_passager(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        passager_form = PassagerForm(request.POST)

        if user_form.is_valid() and passager_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            cd = passager_form.cleaned_data

            passager = Passager.objects.create(
                user=new_user,
                gender=cd['gender'],
                national_id=cd['national_id'],
                age=cd['age'],
                phone=cd['phone']
            )
            passager.save()

            return HttpResponse('Account created successfully')
    else:
        user_form = UserRegistrationForm()
        passager_form = PassagerForm()
    return render(request, 'register.html', {'user_form': user_form, 'passager_form': passager_form})


def user_login(request):
    user = request.user
    if user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    request.session['username'] = cd['username']
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:

                message = 'Wrong username or password'
                form = LoginForm()
                return render(request, 'login.html', {'form': form, 'message': message, })
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form, })


def user_logout(request):
    logout(request)
    try:
        del request.session['username']
        request.session.modified = True
        return render(request, 'logout_then_login.html', {})
    except KeyError, e:
        pass
    return render(request, 'logout_then_login.html', {})


def index(request):
    return render(request, 'index.html', {})


def my_travel(request):
    vehicle = Vehicle.objects.all()
    return render(request, "my_travel.html", {'vehicles': vehicle, })


def book_seat(request, pk=None):
    vehicle = get_object_or_404(Vehicle, pk=pk, is_online=True)
    initial = {'amount': str(vehicle.route.fare), }
    if request.method == 'POST':

        form = SeatPaymentForm(request.POST, initial=initial)

        if form.is_valid():
            # create booking model instance and save it
            username = request.session.get('username', '')
            print username
            user = get_object_or_404(User, username=username)
            passager = get_object_or_404(
                Passager,
                user=user
            )

            source = vehicle.route.source
            destination = vehicle.route.destination
            amount_paid = form.cleaned_data['amount']

            booking = Booking.objects.create(
                passager=passager,
                vehicle=vehicle,
                source=source,
                destination=destination,
                amount_paid=amount_paid
            )
            booking.save()
            vehicle.available_capacity -= 1
            vehicle.save()
            message = "your booking was completed successfully"
            return HttpResponse(message)
            # return render(request, 'booking_successful.html', {'message': message, })

    else:
        form = SeatPaymentForm(initial=initial)
    return render(request, 'book_seat.html', {'form': form, })




