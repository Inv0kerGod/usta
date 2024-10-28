# compat.py
from django.apps import apps
from django.contrib.auth import get_user_model

def get_user_model_lazy():
    if apps.ready:
        return get_user_model()
    else:
        return None  # или можно бросить исключение

User = get_user_model_lazy
