from django.contrib import admin
from service.models import SKILL
from service.models import login
from service.models import tweet
class SKILLAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc']

admin.site.register(SKILL, SKILLAdmin)

class loginadmin(admin.ModelAdmin):

    list_display=['name','email','password']

admin.site.register(login,loginadmin)

class tweetadmin(admin.ModelAdmin):
    list_display=['title','desc','image']

admin.site.register(tweet,tweetadmin)

    

# Register your models here.
