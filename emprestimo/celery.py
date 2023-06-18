import os
from celery import Celery

# Definir o módulo Django padrão para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'emprestimo.settings')

# Criar uma instância do objeto Celery
app = Celery('emprestimo')

# Carregar as configurações do Django para o Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Localização dos tasks do Celery
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
