from django.shortcuts import render_to_response
from models import Note


def random_widget(request):
    note = Note.objects.order_by('?')[0]
    return render_to_response('widget.js', {'note': note},
                              mimetype='text/javascript')
