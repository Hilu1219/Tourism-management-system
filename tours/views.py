from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import TourPackage, Booking
from .forms import BookingForm

def home(request):
    packages = TourPackage.objects.all()
    return render(request, 'tours/home.html', {'packages': packages})

def package_detail(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id)
    return render(request, 'tours/package_detail.html', {'package': package})

def book_package(request, package_id):
    package = get_object_or_404(TourPackage, id=package_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.package = package
            booking.save()
            messages.success(request, f'Booking confirmed for {package.name}!')
            return redirect('package_detail', package_id=package_id)
    else:
        form = BookingForm()
    
    return render(request, 'tours/booking_form.html', {
        'form': form,
        'package': package
    })