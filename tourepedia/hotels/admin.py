from django.contrib import admin

from hotels.models import Hotel, FacilityType, Facility, HotelRoomImg, HotelViewImg, HotelPrice, HotelSeason

class FacilityInline(admin.TabularInline):
	model = Facility
	extra= 0 

class FacilityTypeAdmin(admin.ModelAdmin):
	fieldsets = [
		('facility_type', {
			'fields' : ['facility_type'],
			}),
	]
	inlines = [FacilityInline]

admin.site.register(FacilityType, FacilityTypeAdmin)


class HotelSeasonInline(admin.TabularInline):
	model =HotelSeason
	extra = 0


class HotelRoomImgInline(admin.TabularInline):
	model = HotelRoomImg
	extra = 0


class HotelViewImgInline(admin.TabularInline):
	model = HotelViewImg
	extra = 0

class HotelPriceInline(admin.TabularInline):
	model = HotelPrice
	extra = 0

class HotelAdmin(admin.ModelAdmin):
	fieldsets= [
		('Hotel Basic Info', {
			'fields' : ['hotel_name', 'city', 'email_id', 'concerned_person', 'mobile_number1','mobile_number2','hotel_address', 'star_rating','placedetail','starting_price','main_img'],
			}),
		('Hotel Details', {
			'fields' : ['about_hotel', 'facility_type' ,'map_link']
			}),
	]
	inlines = [HotelRoomImgInline, HotelViewImgInline, HotelPriceInline, HotelSeasonInline]

admin.site.register(Hotel, HotelAdmin)


# Register your models here.
