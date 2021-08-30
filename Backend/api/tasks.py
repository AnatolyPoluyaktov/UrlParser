import json
import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Tags_info
from celery import Celery
@shared_task
def save_item(id: str, item: dict):
    obj = Tags_info(task_id=id, info=item)
    obj.save()

@shared_task
def url_parse(url: str, id:str) -> dict:
    try:
        ans = requests.get(url)
        html = ans.text
        soup = BeautifulSoup(html, "lxml")
        tags = [tag for tag in soup.find_all()]
        d = {}
        for i in tags:
            nested = len(list(i.find_all()))
            val = d.get(i.name, {'count': 0, 'nested': 0})
            val['count'] += 1
            val['nested'] += nested
            d[i.name] = val
            save_item(id, d)
    except requests.exceptions.RequestException as e:
        d = {'error': e}
        save_item(id, d)
        exit(1)


