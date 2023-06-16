# tasks.py

from celery import shared_task
from .models import Proposta
from .proposals import avaliar_proposta

@shared_task
def processar_proposta(proposta_id):
    # Recupera a proposta do banco de dados
    proposta = Proposta.objects.get(id=proposta_id)

    # Realiza o processamento da proposta
    avaliar_proposta(proposta_id)

    # Aqui você pode adicionar a lógica para enviar a proposta para a fila RabbitMQ
    # ...

    # Exemplo de retorno
    return f"Proposta {proposta_id} processada com sucesso"
