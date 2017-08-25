from datetime import datetime
import re
import scrapy
from ..items import TeamScoreItem


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            # 'file:///Users/mcscruf61/Dropbox%20(Personal)/Code/FFLPython/2016/ScoreTracker/BTLS_161027_1953.html',
            'file:///Users/jessemcclure/Dropbox%20(Personal)/Code/FFLPython/2016/ScoreTracker/BTLS_161027_1953.html',
            # 'http://games.espn.com/ffl/scoreboard?leagueId=212635&matchupPeriodId=1',
            # 'http://games.espn.com/ffl/scoreboard?leagueId=212635&matchupPeriodId=9&seasonId=2016',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        now = datetime.utcnow()
        weekText = response.xpath(
            '//div[@class="games-pageheader"]').xpath(
            './/em/text()').extract_first()
        weekNum = re.search(r'Week (\d+)', weekText).group(1)
        oppList = []
        teams = {}
        selTeamList = response.xpath('//a[@target="_top"]')
        if(len(selTeamList) == 13):
            selTeamList = selTeamList[1:]
        for selTeam in selTeamList:
            name = selTeam.xpath('.//text()').extract_first()
            abbv = selTeam.xpath(
                './/../span[@class="abbrev"]/text()').extract_first()[1:-1]
            href = selTeam.xpath('.//@href').extract_first()
            teamId = re.search(r'teamId=([^&]*)', href).group(1)
            oppList.append(teamId)
            teamScore = response.xpath(
                f'//tr[@id="teamscrg_{teamId}_activeteamrow"]').xpath(
                './/td[contains(@class,"score")]/text()').extract_first()
            teams[teamId] = {
                'name': name,
                'teamId': teamId,
                'abbv': abbv,
                'time': now,
                'week': weekNum,
                'tmTotalPts': teamScore,
            }
            # print(oppList)
        for teamId, data in teams.items():
            # teamId = data['teamId']
            oppIndex = oppList.index(teamId)
            if(oppIndex % 2 == 0):
                # print(oppIndex)
                teams[teamId]['oppId'] = oppList[oppIndex + 1]
            else:
                teams[teamId]['oppId'] = oppList[oppIndex - 1]
            elementIds = ['team_ytp', 'team_ip', 'team_pmr',
                          'team_liveproj', 'team_topscorer']
            for eId in elementIds:
                tmp = response.xpath(
                    f'//*[@id="{eId}_{teamId}"]/text()').extract_first()
                if tmp is None:
                    tmp = 0.0
                teams[teamId][eId] = tmp
        for teamId, data in teams.items():
            teamScore = TeamScoreItem(
                name=teams[teamId]['name'],
                abbv=teams[teamId]['abbv'],
                teamId=teams[teamId]['teamId'],
                oppId=teams[teamId]['oppId'],
                oppAbbv=teams[teams[teamId]['oppId']]['abbv'],
                oppName=teams[teams[teamId]['oppId']]['name'],
                time=teams[teamId]['time'],
                week=teams[teamId]['week'],
                tmTotalPts=teams[teamId]['tmTotalPts'],
                oppTotalPts=teams[teams[teamId]['oppId']]['tmTotalPts'],
                team_pts_diff=float(teams[teamId]['tmTotalPts']) -
                float(teams[teams[teamId]['oppId']]['tmTotalPts']),
                team_ytp=teams[teamId]['team_ytp'],
                team_ip=teams[teamId]['team_ip'],
                team_pmr=teams[teamId]['team_pmr'],
                team_liveproj=teams[teamId]['team_liveproj'],
                opp_liveproj=teams[teams[teamId]['oppId']]['team_liveproj'],
                team_proj_diff=float(teams[teamId]['team_liveproj']) -
                float(teams[teams[teamId]['oppId']]['team_liveproj']),
            )
            yield teamScore
        print(oppList)
