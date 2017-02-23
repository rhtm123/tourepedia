from django.contrib import admin

from interested.models import InterestedPeople, InterestedForSchool, InterestedForPlace, Interested

admin.site.register(InterestedPeople)

admin.site.register(InterestedForSchool)

admin.site.register(InterestedForPlace)

admin.site.register(Interested)
