from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
import requests
from requests.exceptions import HTTPError
import logging
from .models import Repo
from .forms import RepoForm

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': '/tmp/debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
})

logger = logging.getLogger(__name__)


def repos(request):
    if request.method == 'POST':
        form = RepoForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            url = f'https://api.github.com/users/{author}/repos'
            try:
                response = requests.get(url)
                response.raise_for_status()
            except HTTPError as http_err:
                logger.error(f'HTTP error occurred: {http_err}')
                messages.info(request, 'Author not found')

            except Exception as err:
                logger.error(f'Other error occurred: {err}')
            if response:
                response = response.json()
                for repo in response:
                    try:
                        data = {
                            'name': repo['name'],
                            'html_url': repo['html_url'],
                            'description': repo['description'],
                            'private': repo['private'],
                            'created_at': repo['created_at'],
                            'watchers': repo['watchers'],
                            'body': repo
                        }
                        Repo.objects.update_or_create(**data)
                        messages.success(request, f'repo {repo["name"]} processed')
                    except (ValueError, IntegrityError) as e:
                        messages.error(request, 'wrong data')
                        logger.error('{e}, data: {repo}')
            else:
                messages.info(request, 'no data processed')
    else:
        form = RepoForm()
    return render(request, 'repos/index.html', {'form': form})
