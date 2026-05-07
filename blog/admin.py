from django.contrib import admin

from blog.models import Post, User, Commentary

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Commentary)