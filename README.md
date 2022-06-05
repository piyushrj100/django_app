# django_app

Change the seret_key present in settings.py. Do the following to generate the secret key :

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
