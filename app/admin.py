from django.contrib import admin
from . models import ContactModel,Carousel,Menu,Logo,SubMenu
# Register your models here.

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display=['id','image','title','sub_title']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['id','title','url_field']

@admin.register(SubMenu)
class SubMenuAdmin(admin.ModelAdmin):
    list_display=['id','title','url_field']

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display=['logo']