from django.contrib import admin
from app.models import TeamScore
# Register your models here.


class TeamScoreAdmin(admin.ModelAdmin):
    list_display = ('abbv', 'time', 'week',
                    'tmTotalPts', 'oppTotalPts', 'oppId')
    list_filter = ('abbv', 'week', 'oppId')

admin.site.register(TeamScore, TeamScoreAdmin)
