from django import forms

from interested.models import InterestedPeople, InterestedForSchool, InterestedForPlace, Interested


class InterestedForm(forms.ModelForm):
	class Meta:
		model = Interested

		fields = ('name', 'email', 'mobile', 'place',)

class PeopleForm(forms.ModelForm):
    

    class Meta:
        model = InterestedPeople

        fields = ('name', 'email', 'mobile',)

class SchoolForm(forms.ModelForm):

	class Meta:

		model = InterestedForSchool

		fields = ('school_name','name', 'email', 'mobile',)

class PlaceForm(forms.ModelForm):

	class Meta:

		model = InterestedForPlace

		fields = ('name', 'email', 'mobile',)

			
