from django import forms

from review.models import ReviewForTours, ReviewForSchoolTrip


class ReviewForm(forms.ModelForm):

    class Meta:
        model = ReviewForTours
        fields = ('review_text',)

class SchoolReviewForm(forms.ModelForm):

	class Meta:
		model = ReviewForSchoolTrip
		fields= ('review_text', 'school_name')
