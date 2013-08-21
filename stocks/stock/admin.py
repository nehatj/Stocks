from django.contrib import admin
from stock.models import *

class StockAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        (None,               {'fields': ['title']}),
       # (None,               {'fields': ['keywords']}),
        (None,               {'fields': ['type']}),
        (None,               {'fields': ['contents']}),
        (None,               {'fields': ['pdf_link']}),
        ('Date information', {'fields': ['dt_posted'], 'classes': ['collapse',]}),
        ('Date information', {'fields': ['created_at'], 'classes': ['collapse',]}),
        ('Date information', {'fields': ['modified_at'], 'classes': ['collapse',]}),
    ]

    list_display = ('id', 'title', 'type', 'contents', 'pdf_link', 'dt_posted', 'created_at', 'modified_at')
   # list_filter = ['created_at']
    
class NewStockAdmin(admin.ModelAdmin):
     fieldsets = [
         (None,               {'fields': ['id']}),
          # (None,               {'fields': ['title']}),
         (None,               {'fields': ['keywords']}),
        # (None,               {'fields': ['type']}),
        # (None,               {'fields': ['contents']}),
         ('Date information', {'fields': ['dt_created'], 'classes': ['collapse',]}),
        # ('Date information', {'fields': ['modified_at'], 'classes': ['collapse',]}),
     ]

     list_display = ('id', 'keywords', 'dt_created')
    # list_filter = ['dt_created']
     




admin.site.register(NewStock,NewStockAdmin)
admin.site.register(Stock,StockAdmin)
