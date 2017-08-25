import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task

from btls_test.btls_test.spiders.test_spider import TestSpider
from scrapyscript import Job, Processor
from scrapy.settings import Settings


@shared_task
def create_random_user_accounts():
    for i in range(10):
        username = 'user_{}'.format(
            get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(
            username=username, email=email, password=password)
    return '{} random users created with success!'.format(10)


@shared_task
def scrap_btls_scoreboard():
    settings = Settings()
    settings.set("USER_AGENT", "Jesse McClure (+http://jrmcclure.github.io)")
    settings.set("BOT_NAME", "btls_test")
    settings.set("ROBOTSTXT_OBEY", False)
    settings.set("ITEM_PIPELINES", {
                 'btls_test.btls_test.pipelines.BtlsTestPipeline': 1000, })
    job = Job(TestSpider())
    Processor(settings).run(job)
    return 'Return from scrapy {}'.format(10)
