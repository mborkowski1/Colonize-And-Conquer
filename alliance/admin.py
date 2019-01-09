from django.contrib import admin
from .models import Alliance, Forum, SubForum, Topic, PostForum
# Register your models here.

admin.site.register(Alliance)
admin.site.register(Forum)
admin.site.register(SubForum)
admin.site.register(Topic)
admin.site.register(PostForum)
