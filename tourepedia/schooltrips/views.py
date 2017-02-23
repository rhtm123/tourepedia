from django.shortcuts import render, redirect
from django.http import HttpResponse

from interested.forms import SchoolForm
from general.models import SchoolTourInclusion, SchoolTourExclusion, TermNCondition
from schooltrips.models import SchoolTourDetail, SchoolTourCategory, SchoolTourItinerary, SchoolTourImage

from review.forms import SchoolReviewForm
from review.models import ReviewForSchoolTrip

from accounts.models import UserProfile

def school_home(request):
	context_dict = {}
	schooltourdetails = SchoolTourDetail.objects.all()

	context_dict['schooltourdetails'] = schooltourdetails

	return render(request, 'schooltrips/school_home.html', context_dict,)


def school_trip(request, slug):
	context_dict = {}
	interested = False

	if request.method == 'POST':

		school_form = SchoolForm(data=request.POST)

		if school_form.is_valid():
			school = school_form.save(commit=False)
			schooltour= SchoolTourDetail.objects.get(slug=slug)			
			school.schooltour = schooltour
			school.save()			

			interested = True

	else:
		school_form = SchoolForm()


	reviewed = False

	if request.method == 'POST':
		review_form = SchoolReviewForm(data=request.POST)
		if review_form.is_valid():
			review = review_form.save(commit=False)
			tourdetail = SchoolTourDetail.objects.get(slug=slug)
			
			userprofile = UserProfile.objects.get(user=request.user)

			review.school_tour= tourdetail

			review.user = request.user
			review.user_image = userprofile.picture

			review.save()
			reviewed = True

			return redirect('school_trip', slug=review.school_tour.slug)
	else:
		review_form = SchoolReviewForm()

	try:

		schooltourdetail = SchoolTourDetail.objects.get(slug=slug)
		
		schooltourinclusions = SchoolTourInclusion.objects.filter(inclusion=schooltourdetail.inclusion_type)
		schooltourexclusions = SchoolTourExclusion.objects.filter(exclusion=schooltourdetail.exclusion_type)
		terms = TermNCondition.objects.filter(term = schooltourdetail.term_type)

		schooltouritinerarys = SchoolTourItinerary.objects.filter(tourdetail=schooltourdetail)

		schooltourimages = SchoolTourImage.objects.filter(tourdetail=schooltourdetail)

		schooltourcategorys = SchoolTourCategory.objects.filter(tourdetail=schooltourdetail)

		reviews = ReviewForSchoolTrip.objects.filter(school_tour=schooltourdetail)

		context_dict['schooltourdetail'] = schooltourdetail

		context_dict['interested'] = interested

		context_dict['school_form'] = school_form
		context_dict['schooltouritinerarys'] = schooltouritinerarys
		context_dict['schooltourimages'] = schooltourimages
		context_dict['schooltourcategorys']= schooltourcategorys

		context_dict['schooltourinclusions'] = schooltourinclusions
		context_dict['schooltourexclusions'] = schooltourexclusions
		context_dict['terms'] = terms


		context_dict['reviews'] = reviews
		context_dict['reviewed'] = reviewed
		context_dict['review_form'] = review_form


	except SchoolTourDetail.DoesNotExist:
		raise Http404("Page does not exist")

	return render(request, 'schooltrips/school_tour.html', context_dict,)


# Create your views here.
