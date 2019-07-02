import pandas as pd
import urllib.request
import os
from logzero import logger

DBURL_HEADER = "http://anzeninfo.mhlw.go.jp/anzen/shisyo_xls/sisyou_db_h"

def makeFilename(year, month):
    strmonth = str(month).zfill(2)
    ext = 'xls'
    if year >= 25:
        ext = 'xlsx'
    return f'{year}_{strmonth}.{ext}'

def downloadDatabase():
    os.makedirs('db', exist_ok=True)
    for year in range(18, 29):
        for month in range(1, 13):
            filename = makeFilename(year, month)
            title = f'db/{filename}'
            if os.path.exists(title):
                pass
                #logger.debug(f'skipped: {filename}')
            else:
                dbUrl = f'{DBURL_HEADER}{filename}'
                logger.debug(dbUrl)
                urllib.request.urlretrieve(dbUrl, "{0}".format(title))

def getDataframe():
    dfs = []
    for year in range(18, 29):
        for month in range(1, 13):
            filename = makeFilename(year, month)
            logger.debug(filename)
            dfs.append(pd.read_excel(f'db/{filename}'))
    return pd.concat(dfs, sort=False)



downloadDatabase()
df = getDataframe()

###### modify according to your purpose 
hoiku = df[df['災害状況'].str.contains('保育', na=False)]
hoiku.to_excel('rosai18-28.xlsx', sheet_name='hoiku')
