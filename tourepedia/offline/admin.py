from django.contrib import admin
from offline.models import TourInfo, Meeting, Deal, Operation 

class MeetingInline(admin.TabularInline):
	model = Meeting
	extra = 0

class DealInline(admin.TabularInline):
	model = Deal
	extra = 0

class OperationInline(admin.TabularInline):
	model = Operation
	extra = 0



class TourInfoAdmin(admin.ModelAdmin):
	fieldsets = [
		('Tour', {
			'fields' : ['tour_name','tour_date'],
			}),
		('Details', {
            'fields': ['number_of_adult', 'number_of_child', 'budget', 'needs'],
            
        }),
	]
	inlines = [MeetingInline, DealInline, OperationInline]

admin.site.register(TourInfo, TourInfoAdmin)
