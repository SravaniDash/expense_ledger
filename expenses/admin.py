from django.contrib import admin
from .models import Category, Transaction, Rule

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_income')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'description', 'amount', 'category', 'is_synthetic')
    list_filter = ('category', 'is_synthetic', 'date')
    search_fields = ('description',)

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('pattern', 'category')
    search_fields = ('pattern',)