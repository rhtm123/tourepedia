from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage

from afterbook.forms import BookedTripForm, BookedTravelForm, BookedHotelForm, OtherBookingForm, BookedCarForm
from afterbook.models import BookedTrip, BookedTravel, BookedHotel, OtherBooking, BookedCar

from traveltriangle.models import TripDetail, Comment, CallDetail, Itinerary, ItineraryDayWise
from traveltriangle.forms import QuoteGenerationForm, CommentForm, CallDetailForm


@login_required
@staff_member_required
def quote_search(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']

	else:
		search_text = ''

	quotes = TripDetail.objects.filter(trip_id__icontains = search_text) | TripDetail.objects.filter(places__icontains = search_text) | TripDetail.objects.filter(person_name__icontains = search_text)

	return render(request, 'traveltriangle/quote_search.html', {'quotes':quotes})

@login_required
@staff_member_required
def itinerary_search(request):

	if request.method == 'POST':
		search_text = request.POST['search_text']

	else:
		search_text = ''

	itinerarys = Itinerary.objects.filter(place_name__icontains = search_text)
	return render(request, 'traveltriangle/itinerary_search.html', {'itinerarys':itinerarys})



@login_required
@staff_member_required
def itinerary_main(request):
	context_dict= {}
	return render(request, 'traveltriangle/itinerary_main.html', context_dict)




@login_required
@staff_member_required
def itinerary(request,slug):
	context_dict = {}

	try:
		itinerary = Itinerary.objects.get(slug=slug)
		itinerary_day_wise = ItineraryDayWise.objects.filter(itinerary=itinerary)

		context_dict['itinerary'] = itinerary
		context_dict['itinerary_day_wise'] = itinerary_day_wise

	except Itinerary.DoesNotExist:
		raise Http404("Page Does not Exist")

	return render(request, 'traveltriangle/itinerary.html', context_dict)



@login_required
@staff_member_required
def cancelled(request):

	context_dict = {}
	user = request.user
	comments = Comment.objects.filter(trip_status="Trip Cancelled").filter(staff_name=user.username).order_by('-pub_date')

	context_dict['comments'] = comments

	return render(request, 'traveltriangle/cancelled.html' ,context_dict)



@login_required
@staff_member_required
def booked(request):
	context_dict = {}
	user = request.user
	comments = Comment.objects.filter(trip_status="Booked With Us").filter(staff_name=user.username).order_by('-pub_date')

	context_dict['comments'] = comments

	return render(request, 'traveltriangle/booked.html' ,context_dict)



@login_required
@staff_member_required
def inprogress(request):
	context_dict = {}
	user = request.user
	comments = Comment.objects.filter(trip_status="Not Booked").filter(staff_name=user.username).order_by('-pub_date')

	context_dict['comments'] = comments

	return render(request, 'traveltriangle/inprogress.html' ,context_dict)
	



@login_required
@staff_member_required
def quote(request):

	context_dict = {}

	if request.method == 'POST':
		form = QuoteGenerationForm(request.POST)

		if form.is_valid():
			form_save = form.save(commit=False)

			user = request.user
			form_save.user = user

			form_save.staff_name = user.username

			form_save.save()
	else:
		form = QuoteGenerationForm()


	tripdetails = TripDetail.objects.all().order_by('-pub_date')[0:10]
	context_dict['form']= form
	context_dict['tripdetails'] = tripdetails

	return render(request,'traveltriangle/new_quote.html', context_dict)


@login_required
@staff_member_required
def info_edit(request,pk):
	context_dict = {}
	tripdetail = TripDetail.objects.get(trip_id=pk)

	if request.method == 'POST':
		form = QuoteGenerationForm(data=request.POST, instance=tripdetail)
		if form.is_valid():
			form_save = form.save(commit=False)

			user = request.user
			form_save.user = user
			form_save.save()
			return redirect('quote_view', pk=form_save.trip_id)
	else:
		form = QuoteGenerationForm(instance=tripdetail)

	context_dict['form'] = form
	return render(request,'traveltriangle/quote_edit.html', context_dict)



@login_required
@staff_member_required
def imp_edit(request, pk):
	context_dict = {}
	tripdetail = TripDetail.objects.get(trip_id=pk)
	comment = Comment.objects.get(tripdetail=tripdetail)

	if request.method == 'POST':
		form = CommentForm(data=request.POST, instance=comment)
		if form.is_valid():
			form_save = form.save(commit=False)

			form_save.save()
			return redirect('quote_view', pk=form_save.tripdetail.trip_id)
	else:
		form = CommentForm(instance=comment)

	context_dict['form'] = form
	return render(request,'traveltriangle/comment_edit.html', context_dict)




@login_required
@staff_member_required
def quote_view(request,pk):

	context_dict ={}


	if request.method == 'POST' and 'booked_trip_form' in request.POST:
		booked_trip_form = BookedTripForm(data=request.POST)

		if booked_trip_form.is_valid():
			booked_trip = booked_trip_form.save(commit=False)

			tripdetail = TripDetail.objects.get(trip_id=pk)
			booked_trip.tripdetail = tripdetail

			booked_trip.save()
			commit=True
			return redirect('quote_view', pk=booked_trip.tripdetail.trip_id)

	else:
		booked_trip_form = BookedTripForm()



	if request.method == 'POST' and 'booked_travel_form' in request.POST:
		booked_travel_form = BookedTravelForm(data=request.POST)

		if booked_travel_form.is_valid():
			booked_travel = booked_travel_form.save(commit=False)

			tripdetail = TripDetail.objects.get(trip_id=pk)
			booked_travel.tripdetail = tripdetail
			booked_travel.save()
			commit = True
			return redirect('quote_view', pk= booked_travel.tripdetail.trip_id)
	else:
		booked_travel_form = BookedTravelForm()


	if request.method == 'POST' and 'booked_car_form' in request.POST:
		booked_car_form = BookedCarForm(data=request.POST)

		if booked_car_form.is_valid():
			booked_car = booked_car_form.save(commit=False)
			tripdetail = TripDetail.objects.get(trip_id=pk)
			booked_car.tripdetail = tripdetail
			booked_car.save()
			commit = True

			return redirect('quote_view', pk= booked_car.tripdetail.trip_id)
	else:
		booked_car_form = BookedCarForm()


	if request.method == 'POST' and 'booked_hotel_form' in request.POST:
		booked_hotel_form = BookedHotelForm(request.POST, request.FILES)

		if booked_hotel_form.is_valid():
			booked_hotel = booked_hotel_form.save(commit=False)
			tripdetail = TripDetail.objects.get(trip_id=pk)
			booked_hotel.tripdetail = tripdetail
			booked_hotel.save()
			commit =True

			trip_id = tripdetail.trip_id
			concerned_person = booked_hotel.hotel.concerned_person
			hotel_name = booked_hotel.hotel.hotel_name
			person= tripdetail.person_name
			date = booked_hotel.date
			night= booked_hotel.hotel_nights
			room_type = booked_hotel.room_type
			room_number = booked_hotel.room_numbers
			price_paid = booked_hotel.price_paid

			adult= tripdetail.number_of_adults
			child = tripdetail.number_of_children
			hotel_email= booked_hotel.hotel.email_id
			confirmation = booked_hotel.booking_confirmation_received

			subject = "Bookings with Tourepedia for trip id {}".format(trip_id)
			subject1 = "Tourepedia Inquary for trip id {}".format(trip_id)
			message = 'Namaste {}, \n \nGreetings from Tourepedia!! \n \nPlease Look at this trip details and revert me. \n\nTraveler Name: {} Trip id: {} \nCheck in date: {}, Number of Nights:{}, Room Type:{}, \nNumber of Rooms:{}, Numbers of Adults:{}, Numbers of Children: {}. \n \nWe have made payment of {} INR for this trip. \n\nPlease acknowlede this and confirm this booking. \n\nChanging the way of traveling with you'.format(concerned_person, person, trip_id, date, night, room_type, room_number,adult, child, price_paid)
			message1 = 'Namaste {}, \n \nGreetings from Tourepedia!! \n \nPlease Look at this trip details.Let us know the availability for same. \n\nTraveler Name: {} Trip id: {} \nCheck in date: {}, Number of Nights:{}, Room Type:{}, \nNumber of Rooms:{}, Numbers of Adults:{}, Numbers of Children:{}.\n\nChanging the way of traveling with you'.format(concerned_person, person, trip_id, date, night, room_type, room_number,adult, child)
			from_email = 'maurya@akhileshmaurya.com'

			recipient_list = ['funmaurya@gmail.com', hotel_email]

			recipient_list1 = ['funmaurya@gmail.com']			

			if request.FILES:
				a = request.FILES['payment_reciept']
				mail = EmailMessage(subject, message, from_email, recipient_list)
				mail.attach(a.name, a.read(), a.content_type)
				mail.send()

			if confirmation == True:
				subject= "Hotel confirmation from {} has been recieved for trip trip id {}".format(hotel_name,trip_id)
				message = "{} has confirmed the payment and rooms for trip id{} ".format(hotel_name, trip_id)

				mail = EmailMessage(subject, message, from_email, recipient_list1)
				mail.send()

			if price_paid == 0:
				
				mail = EmailMessage(subject1, message1, from_email, recipient_list)
				mail.send()

			#send_mail(subject,message,from_email,recipient_list,fail_silently=False)

			return redirect('quote_view', pk=booked_hotel.tripdetail.trip_id)
	else:
		booked_hotel_form = BookedHotelForm()


	if request.method == 'POST' and 'otherbooking_form' in request.POST:
		otherbooking_form = OtherBookingForm(data=request.POST)

		if otherbooking_form.is_valid():
			otherbooking = otherbooking_form.save(commit=False)
			tripdetail = TripDetail.objects.get(trip_id=pk)
			otherbooking.tripdetail = tripdetail
			otherbooking.save()
			commit = True
			return redirect('quote_view', pk= otherbooking.tripdetail.trip_id)
	else:
		otherbooking_form = OtherBookingForm()



	
	if request.method == 'POST' and 'comment_form' in request.POST:
		
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)

			tripdetail = TripDetail.objects.get(trip_id=pk)
			
			user = request.user
			comment.user = user
			comment.tripdetail= tripdetail

			comment.staff_name = user.username
			comment.save()
			#messages.add_message(request, messages.SUCCESS, _('Article correctly saved.'))
			commit = True

			#return redirect('quote_view', pk=comment.tripdetail.trip_id)
	else:
		comment_form = CommentForm()



	if request.method == 'POST' and 'calldetail_form' in request.POST:
		calldetail_form = CallDetailForm(data=request.POST)

		if calldetail_form.is_valid():
			calldetail = calldetail_form.save(commit=False)
			tripdetail = TripDetail.objects.get(trip_id=pk)

			calldetail.tripdetail = tripdetail
			#calldetail.pub_date = datetime.now
			user = request.user
			calldetail.user = user

			calldetail.save()
			commit = True
			return redirect('quote_view', pk=calldetail.tripdetail.trip_id)

	else:
		calldetail_form = CallDetailForm()

	try:

		tripdetail = TripDetail.objects.get(trip_id=pk)
		#quotegeneration = QuoteGeneration.objects.filter(tripdetail=tripdetail)

		comment = Comment.objects.filter(tripdetail=tripdetail)

		bookedtrip = BookedTrip.objects.filter(tripdetail=tripdetail)
		bookedtravel = BookedTravel.objects.filter(tripdetail=tripdetail).order_by('-pub_date')
		bookedhotel = BookedHotel.objects.filter(tripdetail=tripdetail).order_by('-pub_date')
		otherbooking = OtherBooking.objects.filter(tripdetail=tripdetail).order_by('-pub_date')
		bookedcar = BookedCar.objects.filter(tripdetail=tripdetail).order_by('-pub_date')

		calldetail = CallDetail.objects.filter(tripdetail=tripdetail).order_by('-pub_date')

		context_dict['comment'] = comment
		context_dict['calldetail'] = calldetail
		context_dict['calldetail_form'] = calldetail_form

		context_dict['bookedtrip'] = bookedtrip
		context_dict['bookedtravel'] = bookedtravel
		context_dict['bookedhotel'] = bookedhotel
		context_dict['otherbooking'] = otherbooking
		context_dict['bookedcar'] = bookedcar

		#context_dict['quotegeneration'] = quotegeneration

		context_dict['tripdetail'] = tripdetail

		context_dict['comment_form'] = comment_form
		context_dict['booked_trip_form'] = booked_trip_form
		context_dict['booked_travel_form'] = booked_travel_form
		context_dict['booked_hotel_form'] = booked_hotel_form
		context_dict['otherbooking_form'] = otherbooking_form
		context_dict['booked_car_form'] = booked_car_form


	except TripDetail.DoesNotExist:
		raise Http404("Page does not exist")


	return render(request, 'traveltriangle/quote_view.html', context_dict)



@login_required
@permission_required('is_superuser',raise_exception=True)
def traveltriangle_index(request):

	context_dict = {}

	tripdetails = TripDetail.objects.all()

	total = TripDetail.objects.all().count()

	mama_tripdetails = TripDetail.objects.filter(staff_name="mamaji")
	mama_total = TripDetail.objects.filter(staff_name="mamaji").count()

	sharma_tripdetails = TripDetail.objects.filter(staff_name="sharmaji")
	sharma_total = TripDetail.objects.filter(staff_name="sharmaji").count()

	maurya_tripdetails = TripDetail.objects.filter(staff_name="mauryaji")
	maurya_total = TripDetail.objects.filter(staff_name="mauryaji").count()


	context_dict['tripdetails'] = tripdetails
	context_dict['mama_tripdetails'] = mama_tripdetails
	context_dict['sharma_tripdetails'] = sharma_tripdetails
	context_dict['maurya_tripdetails'] = maurya_tripdetails
	context_dict['total'] = total
	context_dict['mama_total'] = mama_total
	context_dict['sharma_total'] = sharma_total
	context_dict['maurya_total'] = maurya_total

	return render(request,'traveltriangle/index.html', context_dict)
# Create your views here.
