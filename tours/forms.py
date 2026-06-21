from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'customer_phone', 'booking_date', 'number_of_people']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
        }