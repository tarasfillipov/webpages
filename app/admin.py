from django.contrib import admin
from models import Note, Book
from forms import NoteForm

class BookAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Book, BookAdmin)

class NoteAdmin(admin.ModelAdmin):
    form = NoteForm

admin.site.register(Note, NoteAdmin)