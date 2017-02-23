from django.shortcuts import render

from django.http import HttpResponse, Http404


from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required


from hotels.models import Hotel, HotelRoomImg, HotelViewImg, Facility, HotelPrice, HotelSeason

@login_required
@staff_member_required
def hotel_home(request):
	hotels= Hotel.objects.all()
	context_dict = {}

	context_dict['hotels'] = hotels

	return render(request, 'hotels/hotel_home.html', context_dict)


@login_required
@staff_member_required
def hotel_search(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']

	else:
		search_text = ''

	hotels = Hotel.objects.filter(hotel_name__icontains = search_text) | Hotel.objects.filter(city__icontains= search_text) | Hotel.objects.filter(hotel_address__icontains = search_text)
	

	return render(request, 'hotels/hotel_search.html', {'hotels':hotels})


def hotel_detail(request, slug):

	context_dict = {}

	try:
		hotel = Hotel.objects.get(slug=slug)

		hotelfacility = Facility.objects.filter(facilitytype=hotel.facility_type)
		hotelroomimg = HotelRoomImg.objects.filter(hotel=hotel)
		hotelviewimg = HotelViewImg.objects.filter(hotel=hotel)
		hotelprices = HotelPrice.objects.filter(hotel=hotel)
		hotelseason = HotelSeason.objects.filter(hotel=hotel)


		context_dict['hotel'] = hotel
		context_dict['hotelfacility'] = hotelfacility
		context_dict['hotelroomimg'] = hotelroomimg
		context_dict['hotelviewimg'] = hotelviewimg
		context_dict['hotelprices'] = hotelprices
		context_dict['hotelseason'] = hotelseason


	except Hotel.DoesNotExist:
		raise Http404("Page does not exist")

	return render(request, 'hotels/hotel_detail.html', context_dict)
