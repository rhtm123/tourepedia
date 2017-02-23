from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blogs.models import Title, PlaceDescribedInBlog, Tag, TagForBlog



class TagForBlogInline(admin.TabularInline):
	model = TagForBlog
	extra = 0

class PlaceDescribedInBlogInline(admin.TabularInline):
	model = PlaceDescribedInBlog
	extra= 0 

class TitleAdmin(SummernoteModelAdmin):
	fieldsets = [
		(None, {
			'fields' : ['header', 'publisher', 'expected_time', 'head_img', 'blog_type'],
			}),
		('Date information', {
            'fields': ['pub_date'],
            
        }),
        ('Content', {
        	'fields':['content'],
        	}),
	]
	inlines = [TagForBlogInline, PlaceDescribedInBlogInline ]

admin.site.register(Title, TitleAdmin)

admin.site.register(Tag)
#admin.site.register(Detail)
#admin.site.register(Category)


