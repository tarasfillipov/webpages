from annoying.decorators import render_to
from models import Note

@render_to('home.html')
def home(request):
    notes = Note.objects.all()

    return {'notes': notes}