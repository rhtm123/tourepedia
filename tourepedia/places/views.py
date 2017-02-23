
from django.conf import settings
from django.contrib import messages

from django.core.mail import send_mail


from django.shortcuts import render
from django.http import HttpResponse, Http404

from tours.models import TourDetail

from blogs.models import PlaceDescribedInBlog, Title
from interested.forms import PlaceForm


from places.models import PlaceDetail, PlaceToVisit, PlaceToEat, HowToReach

def place(request, slug):

	context_dict = {}

	interested = False

	if request.method == 'POST':

		place_form = PlaceForm(data=request.POST)

		if place_form.is_valid():
			place = place_form.save(commit=False)
			placedetail= PlaceDetail.objects.get(slug=slug)			
			place.placedetail = placedetail
			place.save()
			subject = 'Thank you'
			message = 'Welcome to Tourepedia'
			from_email = settings.EMAIL_HOST_USER
			to_list = [place.email]

			send_mail(subject, message, from_email, to_list, fail_silently=True)

			interested = True
	else:
		place_form = PlaceForm()


	try:
		placedetail = PlaceDetail.objects.get(slug=slug)
		placetovisit = PlaceToVisit.objects.filter(placedetail=placedetail)
		placetoeat = PlaceToEat.objects.filter(placedetail=placedetail)
		howtoreach = HowToReach.objects.filter(placedetail=placedetail)

		relatedblogs = PlaceDescribedInBlog.objects.filter(placedetail=placedetail)[:6]

		tours =TourDetail.objects.filter(placedetail=placedetail)[:3]
		blogs = Title.objects.all().order_by('-pub_date')[:5]
		context_dict['blogs'] = blogs

		context_dict['tours'] = tours
		context_dict['relatedblogs'] = relatedblogs
		
		context_dict['placedetail'] = placedetail
		context_dict['placetovisit'] = placetovisit
		context_dict['placetoeat'] = placetoeat
		context_dict['howtoreach'] = howtoreach
		context_dict['place_form'] = place_form
		context_dict['interested'] = interested

	except PlaceDetail.DoesNotExist:
		raise Http404("Page does not exist")

	return render(request, 'places/place.html', context_dict)

def tourforplace(request, slug):

	context_dict = {}

	try:
		placedetail = PlaceDetail.objects.get(slug=slug)

		tourdetails = TourDetail.objects.filter(placedetail=placedetail)
		blogs = Title.objects.all().order_by('-pub_date')[:5]
		context_dict['blogs'] = blogs

		context_dict['placedetail'] = placedetail
		context_dict['tourdetails'] = tourdetails

	except PlaceDetail.DoesNotExist:
		raise Http404("Page does not exist")

	return render(request, 'places/tourforplace.html', context_dict)
# Create your views here.
