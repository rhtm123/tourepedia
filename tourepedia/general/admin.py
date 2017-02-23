from django.contrib import admin
from general.models import TermNCondition, Term, PrivacyPolicy, CancellationPolicy, Inclusion, Exclusion, TourInclusion, TourExclusion, SchoolTourInclusion, SchoolTourExclusion


admin.site.register(PrivacyPolicy)
admin.site.register(CancellationPolicy)

class TermNConditionInline(admin.TabularInline):
	model = TermNCondition
	extra = 0

class TermAdmin(admin.ModelAdmin):
	fieldsets = [
		('Term_type', {
			'fields': ['term_type'],
			}),
	]
	inlines = [TermNConditionInline]

admin.site.register(Term, TermAdmin)



class TourInclusionInline(admin.TabularInline):
	model = TourInclusion
	extra = 0

class SchoolTourInclusionInline(admin.TabularInline):
	model = SchoolTourInclusion
	extra = 0

class InclusionAdmin(admin.ModelAdmin):
	fieldsets = [
		
		('Inclusion Type', {
            'fields': ['inclusion_type'],
            
        }),
	]
	inlines = [TourInclusionInline, SchoolTourInclusionInline]

admin.site.register( Inclusion, InclusionAdmin)


class TourExclusionInline(admin.TabularInline):
	model = TourExclusion
	extra = 0

class SchoolTourExclusionInline(admin.TabularInline):
	model = SchoolTourExclusion
	extra = 0

class ExclusionAdmin(admin.ModelAdmin):
	fieldsets = [
		
		('Exclusion Type', {
            'fields': ['exclusion_type'],
            
        }),
	]
	inlines = [TourExclusionInline, SchoolTourExclusionInline]

admin.site.register( Exclusion, ExclusionAdmin)



