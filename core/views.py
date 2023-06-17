from django.shortcuts import render, redirect
from .models import Proposta
from .serializers import PropostaSerializer
from .proposals import avaliar_proposta
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin


def proposta_form_view(request):
    if request.method == 'POST':
        nome_completo = request.POST.get('nome_completo')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        valor_emprestimo = request.POST.get('valor_emprestimo')

        proposta = Proposta(
            nome_completo=nome_completo,
            cpf=cpf,
            endereco=endereco,
            valor_emprestimo=valor_emprestimo
        )
        proposta.save()
        avaliar_proposta.delay(proposta.id)

        return redirect('preencher_proposta')

    propostas = Proposta.objects.all()
    context = {'propostas': propostas}
    return render(request, 'form_proposta.html', context)


class PropostaCreateAPIView(CreateModelMixin, generics.GenericAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()
        avaliar_proposta.delay(proposta.id)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class PropostaListAPIView(generics.ListAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer


class PropostaUpdateAPIView(UpdateModelMixin, generics.GenericAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class PropostaDeleteAPIView(DestroyModelMixin, generics.GenericAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)