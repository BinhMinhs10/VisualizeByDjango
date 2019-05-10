from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    # tell Django which model should use to create form
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', )
