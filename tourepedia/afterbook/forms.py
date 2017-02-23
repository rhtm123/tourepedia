from django import forms
from django.contrib.admin import widgets
from afterbook.models import BookedTrip, BookedTravel, BookedHotel, OtherBooking, BookedCar

class BookedCarForm(forms.ModelForm):
	class Meta:
		model = BookedCar
		exclude=('tripdetail',)


class BookedTripForm(forms.ModelForm):
	#start_day = forms.DateField(widget=extras.SelectDateWidget(empty_label="Nothing"))
	class Meta:

		model = BookedTrip

		exclude = ('tripdetail',)


class BookedTravelForm(forms.ModelForm):

	class Meta:
		model = BookedTravel
		
		exclude = ('tripdetail',)


class BookedHotelForm(forms.ModelForm):
	
	class Meta:
		model = BookedHotel

		exclude = ('tripdetail',)

class OtherBookingForm(forms.ModelForm):

	class Meta:

		model = OtherBooking
		exclude = ('tripdetail',)