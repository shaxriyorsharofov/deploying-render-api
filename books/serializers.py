from .models import Books
from rest_framework import serializers


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'body', 'author', 'isbn']