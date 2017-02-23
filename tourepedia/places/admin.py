from django.contrib import admin

from places.models import StateDetail,ImpPoint,HowToReach, PlaceDetail, PlaceToVisit, PlaceToEat, PlaceImage


admin.site.register(StateDetail)

class HowToReachInline(admin.TabularInline):
	model = HowToReach
	extra = 0

class PlaceToVisitInline(admin.StackedInline):
	model = PlaceToVisit
	extra = 0

class PlaceToEatInline(admin.StackedInline):
	model = PlaceToEat
	extra = 0

class ImpPointInline(admin.TabularInline):
	model = ImpPoint
	extra = 0

class PlaceImageInline(admin.TabularInline):
	model = PlaceImage
	extra = 0

class PlaceDetailAdmin(admin.ModelAdmin):
	fieldsets= [
		('Place Detail', {
			'fields': ['place_name', 'place_tagline', 'place_detail','main_img']

			}),
		('State', {
			'fields' : ['statedetail']
			}),

	]
	inlines = [PlaceToVisitInline, PlaceToEatInline, ImpPointInline, PlaceImageInline, HowToReachInline]



admin.site.register(PlaceDetail, PlaceDetailAdmin)



# Register your models here.
