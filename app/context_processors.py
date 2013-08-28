from models import Note


def count_notes(request):
    amount = Note.objects.all().count()
    return {'amount': amount}
