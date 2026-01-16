from django import forms
from django.forms import ModelForm, DateInput

from apps.emprestimos.models import Emprestimo

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        exclude = ('data_emprestimo',)
        fields = '__all__'
        widgets = {
<<<<<<< HEAD
        'data_devolucao': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        ),

        'data_prevista_devolucao': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        ),
}
=======
            'data_devolucao': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),

            'data_prevista_devolucao': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
            ),
        }

>>>>>>> ea554921e9dabd40a9de3c45d9cb0b02b83c6faf
