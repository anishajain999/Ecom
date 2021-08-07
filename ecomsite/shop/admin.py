from django.contrib import admin
from .models import Product, Order

# Register your models here.

admin.site.site_header = "E-commerce Site" #for heading the admin pannel
admin.site.site_title = "Shopping Site"
admin.site.index_title = "Manage Shopping Site"

# Display more than one name in Product itmes
class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="defualt")

    change_category_to_default.short_description = "Defualt Category"
    list_display = ('title','category','price','discont_price')  #to display items
    search_fields = ('category',)   #to search items
    actions = ("change_category_to_default",)  #to chnge in action field
    fields = ("title", "price", "category",)   #to not display all fields
    list_editable = ("price","discont_price")  # to edit the field outside

admin.site.register(Product, ProductAdmin)  #to connect class to model
admin.site.register(Order)