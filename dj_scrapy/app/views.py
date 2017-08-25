from django.http import HttpResponse

from .tasks import scrap_btls_scoreboard


def test_view(request):
    scrap_btls_scoreboard()
    html = "<html><body>It is now.</body></html>"
    return HttpResponse(html)
