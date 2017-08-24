from django.db import models

# Create your models here.


class TeamScore(models.Model):
    name = models.CharField(max_length=255)
    abbv = models.CharField(max_length=16, db_index=True)
    teamId = models.SmallIntegerField(db_index=True)
    oppId = models.SmallIntegerField(db_index=True)
    time = models.DateTimeField(null=True)
    week = models.SmallIntegerField(db_index=True)
    tmTotalPts = models.FloatField(null=True, default=0.0)
    team_ytp = models.SmallIntegerField(null=True)
    team_ip = models.SmallIntegerField(null=True)
    team_pmr = models.SmallIntegerField(null=True)
    team_liveproj = models.FloatField(null=True, default=0.0)

    def __str__(self):
        return self.abbv
