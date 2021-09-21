from django.contrib import admin

from .models import Author, Quote


class QuoteInlineModelAdmin(admin.TabularInline):
    model = Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'birthday', 'birth_loc', 'description']
    list_filter = ['name', 'birth_loc']
    search_fields = ['name']
    inlines = [QuoteInlineModelAdmin]


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['text', 'author']
    list_filter = ['author']
