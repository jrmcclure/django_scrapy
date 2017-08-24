from scrapy_djangoitem import DjangoItem
from app.models import TeamScore


class TeamScoreItem(DjangoItem):
    django_model = TeamScore
