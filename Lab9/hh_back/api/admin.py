from django.contrib import admin

from .models import Company, Vacancy

@admin.register(Company)

class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Vacancy)
class CategoryAdmin(admin.ModelAdmin):
    pass
