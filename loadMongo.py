from common.Mongo_client import Mongo
import csv
mongo = Mongo()
collections = mongo.get_db().get_collection('news')

BASKET_BALL = [
    'NBA', 'Lebron', 'playoffs', 'Nuggets', 'Lakers', 'basketball', 'Clippers', 'playoffs',
    'Harden', 'Rockets', ''
]
with open("labeled_news.csv", "a") as f:
    condition = { "$or": [{"classify": "Football"}, {"classify": "NFL"},
                          {"classify": "F1"}]}
    csv_writer = csv.writer(f)
    for x in collections.find({"classify":"China"}).sort([('publishedAt', -1)]):
        title = x['title']
        desc = x['description']
        if title:
            title = title.replace('\\', '')
            title = title.replace(',', '\\,')
            title = title.replace('<li>', '')
            title = title.replace('</li>', '')
            title = title.replace('<ol>', '')
            title = title.replace('</ol>', '')
            title = title.replace('<ul>', '')
            title = title.replace('</ul>', '')
            title.strip()
        source = x['source']
        if desc:
            csv_writer.writerow([6, title])
        # if 'iPhone' in title or 'iPhone' in desc or 'Apple' in title or 'Apple' in desc or 'iPad' in title:
        #     csv_writer.writerow([5, title, desc, source])
        # if x['source'].lower() == 'espn' or x['source'] == 'espn':
        #     isBasket = False
        #     for basket in BASKET_BALL:
        #         if basket in title or basket in desc:
        #             isBasket = True
        #             break
        #     if 'nba' in url:
        #         isBasket = True
        #     if isBasket:
        #        csv_writer.writerow([1, title, desc, source])
        #     else:
        #         csv_writer.writerow([3, title, desc, source])
        # if 'covid' in title or 'covid' in desc or 'covid' in x['text'] or 'Coronavirus' in title or 'Coronavirus' in desc:
        #     csv_writer.writerow([2, title, desc, source])
        # elif 'Trump' in x['title'] or 'Trump' in x['description']:
        #     csv_writer.writerow([4, title, desc, source])

# import pandas as pd
#
# DATA_SET_FILE = './labeled_news.csv'
#
# df = pd.read_csv(DATA_SET_FILE, header=None)