from django.db import models


class TeamScore(models.Model):
    teamId = models.SmallIntegerField(db_index=True)
    abbv = models.CharField(max_length=16, db_index=True)
    name = models.CharField(max_length=255)
    oppId = models.SmallIntegerField(db_index=True)
    oppAbbv = models.CharField(max_length=16, db_index=True)
    oppName = models.CharField(max_length=255)
    time = models.DateTimeField(null=True)
    week = models.SmallIntegerField(db_index=True)
    tmTotalPts = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    oppTotalPts = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    team_pts_diff = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    team_ytp = models.SmallIntegerField(default=0)
    team_ip = models.SmallIntegerField(default=0)
    team_pmr = models.SmallIntegerField(default=0)
    team_liveproj = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    opp_liveproj = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    team_proj_diff = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=4)
    final = models.BooleanField(default=False)

    def __str__(self):
        return self.abbv
