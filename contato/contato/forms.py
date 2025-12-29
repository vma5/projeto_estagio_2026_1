from django import forms
from .models import Mensagem

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full p-3 rounded bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 rounded bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none'}),
            'assunto': forms.TextInput(attrs={'class': 'w-full p-3 rounded bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none'}),
            'mensagem': forms.Textarea(attrs={'class': 'w-full p-3 rounded bg-gray-50 border border-gray-300 focus:ring-2 focus:ring-blue-500 outline-none', 'rows': 4}),
        }