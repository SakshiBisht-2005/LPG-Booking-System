from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from .models import EmailOTP, Booking
from .utils import generate_otp


# 🏠 Home = Login Page
def home(request):
    if request.method == "POST":
        email = request.POST['email']

        # get or create user
        user, created = User.objects.get_or_create(
            username=email,
            email=email
        )

        # generate OTP
        otp_code = generate_otp()

        # save OTP
        EmailOTP.objects.create(user=user, otp=otp_code)

        # store correct user id ✅
        request.session['user_id'] = user.id

        # send email
        send_mail(
            'LPG Booking OTP',
            f'Your OTP is {otp_code}',
            'your_email@gmail.com',
            [email],
            fail_silently=False,
        )

        return redirect('verify_otp')

    return render(request, 'login.html')


# 🔐 OTP Verification
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST['otp']

        user_id = request.session.get('user_id')

        if not user_id:
            return redirect('home')

        user = get_object_or_404(User, id=user_id)

        otp_obj = EmailOTP.objects.filter(user=user).last()

        if otp_obj and otp_obj.otp == entered_otp:
            login(request, user)

            request.session.pop('user_id', None)

            return redirect('dashboard')

        else:
            return render(request, 'verify_otp.html', {'error': 'Invalid OTP'})

    return render(request, 'verify_otp.html')


# 🚪 Logout
def user_logout(request):
    logout(request)
    return redirect('home')


# 🏠 Dashboard
@login_required(login_url='/')
def dashboard(request):
    latest_booking = Booking.objects.filter(user=request.user).last()

    next_date = None

    if latest_booking:
        next_date = latest_booking.booking_date + timedelta(days=21)

    context = {
        'latest_booking': latest_booking,
        'next_date': next_date
    }

    return render(request, 'dashboard.html', context)

# ⛽ Book Gas
@login_required(login_url='/')
def book_gas(request):
    last_booking = Booking.objects.filter(user=request.user).last()

    # 🚫 Restriction: 21 days
    if last_booking:
        next_allowed_date = last_booking.booking_date + timedelta(days=21)

        if timezone.now() < next_allowed_date:
            return render(request, 'book.html', {
                'error': f'You can book next cylinder after {next_allowed_date.date()}',
                'next_date': next_allowed_date.date()
            })

    if request.method == "POST":
        address = request.POST['address']

        Booking.objects.create(
            user=request.user,
            address=address
        )

        return redirect('dashboard')

    return render(request, 'book.html')


# 📜 Booking History
@login_required(login_url='/')
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'history.html', {'bookings': bookings})