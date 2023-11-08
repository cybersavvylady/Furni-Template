from django.contrib import admin

from .models import Product, BlogPost, Testimonial, TeamMember, Service, ContactInfo


# Register your models here.

admin.site.register(Product)
admin.site.register(BlogPost)
admin.site.register(Testimonial)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(ContactInfo)