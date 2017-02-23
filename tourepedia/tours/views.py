from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from django.contrib.auth.models import User
from accounts.models import UserProfile

from interested.forms import PeopleForm
from general.models import TourInclusion, TourExclusion, TermNCondition

from tours.models import TourDetail, TourImage, TourCategory, TourItinerary, ImportantPoint
from blogs.models import Title

from review.forms import ReviewForm
from review.models import ReviewForTours, ReviewForSchoolTrip

def home(request):

	blogs = Title.objects.all().order_by('-pub_date')[:6]

	review_tour = ReviewForTours.objects.all().order_by('-pub_date')[:5]

	review_school = ReviewForSchoolTrip.objects.all().order_by('-pub_date')[:5]



	context_dict = {}

	context_dict['blogs'] = blogs
	context_dict['review_tour'] = review_tour
	context_dict['review_school'] = review_school

	return render(request, 'tours/home.html', context_dict)

def main_search(request):

	if request.method == 'POST':
		search_text = request.POST['search_text']

	else:
		search_text = ''

	searchs = TourDetail.objects.filter(tour_name__icontains = search_text)
	return render(request, 'tours/main_search.html', {'searchs':searchs})

def adventure(request):
	context_dict= {}

	tourcategorys = TourCategory.objects.filter(category='Adventure')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/adventure.html', context_dict)

def family(request):
	context_dict = {}

	tourcategorys = TourCategory.objects.filter(category='Family')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs
	context_dict['tourcategorys'] = tourcategorys


	return render(request, 'tours/family.html', context_dict)

def nature(request):
	context_dict = {}

	tourcategorys = TourCategory.objects.filter(category='Nature')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/nature.html', context_dict)

def honeymoon(request):
	context_dict = {}
	tourcategorys = TourCategory.objects.filter(category='Honeymoon')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/honeymoon.html', context_dict)

def wildlife(request):

	context_dict = {}

	tourcategorys = TourCategory.objects.filter(category='Wildlife')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/wildlife.html', context_dict)

def hill_station(request):
	context_dict= {}

	tourcategorys = TourCategory.objects.filter(category='Hill-Station')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/hill-station.html', context_dict)

def religious(request):
	context_dict = {}

	tourcategorys = TourCategory.objects.filter(category='Religious')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys
	return render(request, 'tours/religious.html', context_dict)

def beaches(request):
	context_dict = {}

	tourcategorys = TourCategory.objects.filter(category='Beaches')
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourcategorys'] = tourcategorys

	return render(request, 'tours/beaches.html', context_dict)



def tour_packages(request):

	context_dict = {}
	tourdetails = TourDetail.objects.all()
	blogs = Title.objects.all().order_by('-pub_date')[:5]
	context_dict['blogs'] = blogs

	context_dict['tourdetails'] = tourdetails

	return render(request, 'tours/tour_list.html', context_dict,)

def tour(request, slug):
	context_dict = {}

	interested = False

	if request.method == 'POST':

		people_form = PeopleForm(data=request.POST)

		if people_form.is_valid():
			people = people_form.save(commit=False)
			tour= TourDetail.objects.get(slug=slug)			
			people.tourdetail = tour
			people.save()			

			interested = True
	else:
		people_form = PeopleForm()

	reviewed = False

	if request.method == 'POST':
		review_form = ReviewForm(data=request.POST)
		if review_form.is_valid():
			review = review_form.save(commit=False)
			tourdetail = TourDetail.objects.get(slug=slug)
			
			userprofile = UserProfile.objects.get(user=request.user)

			review.tourdetail= tourdetail
			review.user = request.user
			review.user_image = userprofile.picture

			




			review.save()
			reviewed = True

			return redirect('tour', slug=review.tourdetail.slug)

	else:
		review_form = ReviewForm()

	try:

		tourdetail = TourDetail.objects.get(slug=slug)

		tourinclusions = TourInclusion.objects.filter(inclusion=tourdetail.inclusion_type)
		tourexclusions = TourExclusion.objects.filter(exclusion=tourdetail.exclusion_type)

		terms = TermNCondition.objects.filter(term = tourdetail.term_type)
		

		touritinerarys = TourItinerary.objects.filter(tourdetail=tourdetail)

		tourimages = TourImage.objects.filter(tourdetail=tourdetail)

		tourcategorys = TourCategory.objects.filter(tourdetail=tourdetail)

		importantpoints = ImportantPoint.objects.filter(tourdetail=tourdetail)

		reviews = ReviewForTours.objects.filter(tourdetail=tourdetail)

		context_dict['importantpoints'] = importantpoints

		context_dict['terms'] = terms
		blogs = Title.objects.all().order_by('-pub_date')[:5]
		context_dict['blogs'] = blogs

		context_dict['tourinclusions'] = tourinclusions
		context_dict['tourexclusions'] = tourexclusions
		context_dict['interested'] = interested
		context_dict['people_form'] = people_form

		context_dict['tourdetail'] = tourdetail

		context_dict['touritinerarys'] = touritinerarys
		context_dict['tourimages'] = tourimages
		context_dict['tourcategorys']= tourcategorys

		context_dict['reviews'] = reviews
		context_dict['reviewed'] = reviewed
		context_dict['review_form'] = review_form

	except TourDetail.DoesNotExist:
		raise Http404("Page does not exist")

	return render(request, 'tours/tour.html', context_dict,)
