from django.contrib import admin

from traveltriangle.models import TripDetail, Comment, CallDetail, ItineraryDayWise, Itinerary


#admin.site.register(ItineraryDayWise)




class ItineraryDayWiseInline(admin.TabularInline):
	model = ItineraryDayWise
	extra = 0

class ItinerayAdmin(admin.ModelAdmin):
	fieldsets = [
		('Place Name' , {
			'fields' : ['place_name',],
			}),
	]

	inlines = [ItineraryDayWiseInline]

admin.site.register(Itinerary, ItinerayAdmin)








class CallDetailInline(admin.TabularInline):
	model = CallDetail
	extra = 0



class TripDetailAdmin(admin.ModelAdmin):

	def save_model(self, request, obj, form, change):
		obj.user = request.user

		obj.save()

	fieldsets = [
		('trip detail' , {
			'fields': ['user','trip_id','number_of_adults', 'number_of_children', 'trip_nights', 'places','budget'],
				}),

		('person Detail' , {
			'fields' : ['person_name', 'email', 'mobile'],
			}),
	]


	inlines = [CallDetailInline,]


	

admin.site.register(TripDetail,TripDetailAdmin)

admin.site.register(Comment)

# Register your models here.
