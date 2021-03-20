from rest_framework import serializers
from main.models import Book, BookJournalBase, Journal


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(write_only=True)

    class Meta:
        model = Book
        fields = ('id', 'num_pages', 'title',)


class JournalSerializer(serializers.ModelSerializer):
    publisher = serializers.CharField(write_only=True)

    class Meta:
        model = Journal
        fields = ('id', 'type', 'publisher',)

