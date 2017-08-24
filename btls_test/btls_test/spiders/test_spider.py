from datetime import datetime
import re
import scrapy
from btls_test.items import TeamScoreItem


class TestSpider(scrapy.Spider):
    name = "test"

    def start_requests(self):
        urls = [
            'file:///Users/mcscruf61/Dropbox%20(Personal)/Code/FFLPython/2016/ScoreTracker/BTLS_161027_1953.html',
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
        for selTeam in response.xpath('//a[@target="_top"]')[1:]:
            name = selTeam.xpath('.//text()').extract_first()
            abbv = selTeam.xpath(
                './/../span[@class="abbrev"]/text()').extract_first()[1:-1]
            href = selTeam.xpath('.//@href').extract_first()
            teamId = re.search(r'teamId=([^&]*)', href).group(1)
            oppList.append(teamId)
            teamScore = response.xpath(
                f'//tr[@id="teamscrg_{teamId}_activeteamrow"]').xpath(
                './/td[contains(@class,"score")]/text()').extract_first()
            teams[abbv] = {
                'name': name,
                'teamId': teamId,
                'abbv': abbv,
                'time': now,
                'week': weekNum,
                'tmTotalPts': teamScore,
            }
        for team, data in teams.items():
            teamId = data['teamId']
            oppIndex = oppList.index(teamId)
            if(oppIndex % 2 == 0):
                teams[team]['oppId'] = oppList[oppIndex + 1]
            else:
                teams[team]['oppId'] = oppList[oppIndex - 1]
            elementIds = ['team_ytp', 'team_ip', 'team_pmr',
                          'team_liveproj', 'team_topscorer']
            for eId in elementIds:
                tmp = response.xpath(
                    f'//*[@id="{eId}_{teamId}"]/text()').extract_first()
                teams[team][eId] = tmp
            teamScore = TeamScoreItem(
                name=teams[team]['name'],
                abbv=teams[team]['abbv'],
                teamId=teams[team]['teamId'],
                oppId=teams[team]['oppId'],
                time=teams[team]['time'],
                week=teams[team]['week'],
                tmTotalPts=teams[team]['tmTotalPts'],
                team_ytp=teams[team]['team_ytp'],
                team_ip=teams[team]['team_ip'],
                team_pmr=teams[team]['team_pmr'],
                team_liveproj=teams[team]['team_liveproj'],
            )
            yield teamScore
        print(oppList)
