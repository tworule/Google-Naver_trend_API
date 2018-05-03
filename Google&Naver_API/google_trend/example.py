from google_trend import TrendReq

""" Get input keyword to 'input_text' (ex. Burger king) """
kw_text = 'KFC'
kw_list = [kw_text]

""" Connect to Google """
pytrends = TrendReq()
                        #tz = Timezone Offset (ex. US CST = '360')

""" Build Payload """
pytrends.build_payload(kw_list, cat='0', timeframe='2018-03-17 2018-04-14', geo='US', gprop='youtube')
                        #cat       = category (ex. 'Fast Food' = '918') 
                        #             https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories

                        #timeframe = 1)'2017-12-12 2017-12-13' 시작일, 종료일 지정
                        #            2) 'now 7-d', 'today 3-m' 등 '오늘로부터 3개월전부터'로 기간설정 가능 

                        #geo = Two letter country abbreviation (ex. 'US')
                        #gprop = images, news, youtube, froogle (default = web search)

""" Interest_over_time """
print(pytrends.interest_over_time())