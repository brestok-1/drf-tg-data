from django.contrib import admin

from books.models import Book, Author


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
