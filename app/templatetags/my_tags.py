from django import template
from app.models import Note
register = template.Library()


@register.inclusion_tag("note_by_id.html")
def note_by_id(param):
    note = Note.objects.get(pk=param)
    return {'note': note}
