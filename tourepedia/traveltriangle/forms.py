from django import forms

from django.contrib.admin import widgets

from traveltriangle.models import ItineraryDayWise, TripDetail, CallDetail, Comment
from hotels.models import Hotel, HotelPrice


from django.forms import extras




class QuoteGenerationForm(forms.ModelForm):

	#start_day = forms.DateField(widget=extras.SelectDateWidget(empty_label="Nothing"))

	class Meta:

		model = TripDetail

		exclude = ('user',)


class CommentForm(forms.ModelForm):

	class Meta:

		model = Comment
		
		exclude = ('tripdetail','user')


class ItineraryForm(forms.ModelForm):
	class Meta:
		model = ItineraryDayWise

		exclude = ('tripdetail','user')

class CallDetailForm(forms.ModelForm):

	class Meta:

		model = CallDetail
		exclude = ('tripdetail','user')
