from annoying.decorators import render_to
from models import Note
from forms import NoteForm
from django.shortcuts import get_object_or_404, redirect, render


@render_to('home.html')
def home(request):
    notes = Note.objects.all()
    return {'notes': notes}

def add(request):

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NoteForm()
    return render(request, 'add.html', {'form': form})