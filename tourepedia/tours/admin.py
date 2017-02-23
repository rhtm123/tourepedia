from django.contrib import admin
from tours.models import TourDetail, TourCategory, TourItinerary, TourImage, ImportantPoint, PlacesInclude


class TourImageInline(admin.TabularInline):
	model = TourImage
	extra = 0

class TourItineraryInline(admin.TabularInline):
	model = TourItinerary
	extra = 0



class TourCategoryInline(admin.TabularInline):
	model = TourCategory
	extra = 0

class TourImageInline(admin.TabularInline):
	model = TourImage
	extra = 0

class ImportantPointInline(admin.TabularInline):
	model = ImportantPoint
	extra= 0

class PlacesInclideInline(admin.TabularInline):
	model = PlacesInclude
	extra = 0

class TourDetailAdmin(admin.ModelAdmin):
	fieldsets = [
		('TourName', {
			'fields' : ['tour_name', 'placedetail' , 'main_img', 'credit_name', 'licence_type', 'credit_url'],
			}),
		('Details', {
            'fields': ['tour_tagline', 'tour_price', 'number_days','tour_detail',],
            
        }),
        ('Term, Inclusions and Exclusion', { 
        	'fields': ['inclusion_type', 'exclusion_type', 'term_type'],
        	}),
	]
	inlines = [TourItineraryInline, TourCategoryInline, TourImageInline, ImportantPointInline, PlacesInclideInline]

admin.site.register(TourDetail, TourDetailAdmin)