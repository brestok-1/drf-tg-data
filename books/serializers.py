from rest_framework import serializers

from books.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

