from celery import shared_task
from .models import Proposta

@shared_task
def avaliar_proposta(proposta_id):
    proposta = Proposta.objects.get(proposta_id)
    proposta.save()