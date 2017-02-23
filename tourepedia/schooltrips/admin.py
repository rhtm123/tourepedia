from django.contrib import admin

from schooltrips.models import SchoolTourDetail, SchoolTourCategory, SchoolTourItinerary, SchoolTourImage


class SchoolTourImageInline(admin.TabularInline):
	model = SchoolTourImage
	extra = 0

class SchoolTourItineraryInline(admin.TabularInline):
	model = SchoolTourItinerary
	extra = 0


class SchoolTourCategoryInline(admin.TabularInline):
	model = SchoolTourCategory
	extra = 0

class SchoolTourDetailAdmin(admin.ModelAdmin):
	fieldsets = [
		('TourName', {
			'fields' : ['tour_name','statedetail', 'placedetail'],
			}),
		('Details', {
            'fields': ['tour_price','number_days','tour_detail' , 'main_img'],
            
        }),
        ('Term, Inclusions and Exclusion', { 
        	'fields': ['inclusion_type', 'exclusion_type', 'term_type'],
        	}),
	]
	
	inlines = [SchoolTourItineraryInline, SchoolTourCategoryInline, SchoolTourImageInline]

admin.site.register(SchoolTourDetail, SchoolTourDetailAdmin)

#admin.site.register(Detail)
#admin.site.register(Category)

# Register your models here.
