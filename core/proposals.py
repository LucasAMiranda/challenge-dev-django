from celery import shared_task
from .models import Proposta
import logging

@shared_task
def avaliar_proposta(id, status):
    logging.warning(f'Starting {id} task!')
    try:
        new_status = status.get('status')
        instance = Proposta.objects.get(id=id)
        instance.status = new_status
        instance.save()
    except Proposta.DoesNotExist:
        logging.warning(f'Proposta with id {id} does not exist.')
    except Exception as err:
        logging.error(f'Error processing task: {err}')
        raise err
    finally:
        logging.warning('Finished task!')