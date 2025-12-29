from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensagem
from .forms import MensagemForm

def landpage(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
            return redirect('landpage')
    else:
        form = MensagemForm()
    return render(request, 'landpage.html', {'form': form})

@login_required(login_url='login')
def painel_mensagens(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'painel.html', {'mensagens': mensagens})