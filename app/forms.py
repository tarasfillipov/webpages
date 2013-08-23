from django.forms import ModelForm, TextInput, Textarea
from django import forms
from models import Note
from django.utils.html import conditional_escape, format_html
from django.utils.encoding import force_text
from django.forms.util import flatatt
class NoteWidget(Textarea):
    class Media:
        css = {
            'all': ('css/jquery-ui-1.8.21.custom.css', )
        }
        js = (
            'js/jquery.min.js',
            'js/jquery-ui-1.8.21.custom.min.js',
            'js/counter.js',
        )

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html('<div class="countered"><textarea{0}>\r\n{1}</textarea>'
                           '<span id="counter_area">Total: 0</span></div>',
                           flatatt(final_attrs),
                           force_text(value))

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ('text','photo')
        widgets = {
            'text': NoteWidget(),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 10:
            raise forms.ValidationError('Not enough symbols!')
        return text