from django.contrib import admin
from .models import Post,Category,Donation,Rating

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Rating)
