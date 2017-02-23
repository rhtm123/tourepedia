from django import forms

from subscribe.models import Subscriber

class SubscribeForm(forms.ModelForm):

	class Meta:
		model = Subscriber

		fields = ('subscriber_email',)