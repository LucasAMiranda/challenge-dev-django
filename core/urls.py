from django.urls import path
from .views import (
    proposta_form_view,
    PropostaCreateAPIView,
    PropostaDeleteAPIView,
    #atualizar_campos_proposta,
    PropostaUpdateAPIView,
    PropostaListAPIView

)

urlpatterns = [
    # Rota para exibir o formulário de preenchimento da proposta
    path('proposta/', proposta_form_view, name='preencher_proposta'),
    path('propostas/create/', PropostaCreateAPIView.as_view(), name='create_proposta'),
    path('propostas/<int:pk>/delete/', PropostaDeleteAPIView.as_view(), name='delete_proposta'),
    path('propostas/<int:pk>/update/', PropostaUpdateAPIView.as_view(), name='update_proposta'),
    path('propostas/', PropostaListAPIView.as_view(), name='list_propostas'),

]
