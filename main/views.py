from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from main.models import Book, Journal
from main.serializers import BookSerializer, JournalSerializer
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


class BookViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()

    @action(methods=['GET'], detail=False, url_path='books', url_name='books', permission_classes=(AllowAny,))
    def not_active(self, request):
        serializer = BookSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class JournalViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = JournalSerializer

    def get_queryset(self):
        return Journal.objects.all()

    @action(methods=['GET'], detail=False, url_path='journals', url_name='journals', permission_classes=(AllowAny,))
    def not_active(self, request):
        serializer = JournalSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
