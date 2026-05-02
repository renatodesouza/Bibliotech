import os
from celery import Celery


# defini as configurações padrão do Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Cria o app do Celery
app = Celery('config')

# Lê as configurações do Django, tudo que começa com CELERY_ vai para o celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Procura automaticamente por tarefas (tasks.py) nos apps
app.autodiscover_tasks()