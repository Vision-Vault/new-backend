from django.contrib import admin
from .models import Comment,ChildComment

# Register your models here.
admin.site.register(Comment)
admin.site.register(ChildComment)
