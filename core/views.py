from django.shortcuts import render, redirect
from .models import Proposta
from .serializers import PropostaSerializer
from .proposals import avaliar_proposta
from rest_framework import generics
from rest_framework.response import Response

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


class PropostaUpdateAPIView(generics.UpdateAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer


class PropostaListAPIView(generics.ListAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer


class PropostaCreateAPIView(generics.CreateAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def perform_create(self, serializer):
        proposta = serializer.save()
        avaliar_proposta.delay(proposta.id)


class PropostaDeleteAPIView(generics.DestroyAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Proposta excluída com sucesso.'})

    def perform_destroy(self, instance):
        instance.delete()