from celery import shared_task
from .models import Proposta
import logging

@shared_task
def avaliar_proposta(id, status):
    logging.warning(f'Iniciando tarefa {id}!')
    try:
        novo_status = status.get('status')
        instancia = Proposta.objects.get(id=id)
        instancia.status = novo_status
        instancia.save()
    except Proposta.DoesNotExist:
        logging.warning(f'Proposta com ID {id} não existe.')
    except Exception as err:
        logging.error(f'Erro ao processar tarefa: {err}')
        raise err
    finally:
        logging.warning('Tarefa finalizada!')


@shared_task
def verificar_propostas():
    logging.warning('Iniciando tarefa!')
    try:
        propostas = Proposta.objects.all()
        for proposta in propostas:
            if proposta.status != 'Aprovado' and proposta.status != 'Recusado':
                if proposta.valor_emprestimo >= 1000:
                    proposta.status = 'Aprovado'
                else:
                    proposta.status = 'Recusado'
                proposta.save()
    except Exception as err:
        logging.error(f'Erro ao processar tarefa: {err}')
        raise err
    finally:
        logging.warning('Tarefa finalizada!')
