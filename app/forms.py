from django.forms import ModelForm
from django import forms
from models import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('Not enough symbols!')
        return text