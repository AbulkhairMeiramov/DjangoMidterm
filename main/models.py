from django.db import models
from utils.constants import JOURNAL_TYPES


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, blank=True, verbose_name='Name')
    price = models.IntegerField(verbose_name='Price')
    description = models.TextField(blank=True, verbose_name='Description')
    created_at = models.DateField(verbose_name='Created at')

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name='Number of pages')
    genre = models.CharField(max_length=255, blank=True, verbose_name='Genre')


class Journal(BookJournalBase):
    type = models.IntegerField(choices=JOURNAL_TYPES)
    publisher = models.CharField(max_length=255, blank=True, verbose_name='Publisher')



