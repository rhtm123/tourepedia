from django.contrib import admin
from afterbook.models import BookedTrip, BookedTravel, BookedHotel, OtherBooking, BookedCar

admin.site.register(BookedTrip)
admin.site.register(BookedCar)
admin.site.register(BookedTravel)
admin.site.register(BookedHotel)
admin.site.register(OtherBooking)


# Register your models here.
