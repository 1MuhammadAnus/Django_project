from django.contrib import admin
from .models import catagory , product

@admin.register(catagory)

class admincatagory(admin.ModelAdmin):
    list_display = ['name' , 'slug']

    prepopulated_fields = {'slug' :('name' , )}

@admin.register(product)
class adminregister(admin.ModelAdmin):
    list_display = ['title' ,'catagory', 'craeted_by','image','discription','price','created','updated'
                    ,'is_active','is_stock']
    list_filter = ['is_active' ,'is_stock' ]
    list_editable = ['price' , 'is_stock']
    prepopulated_fields = {'slug' , ('title', )}
# Register your models here.
