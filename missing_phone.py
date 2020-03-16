from psycopg2 import connect, sql
import sys
import re
from tqdm import tqdm
import signal
import requests
from lxml import html
from bs4 import BeautifulSoup
import certifi
import urllib3

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where())

def convertTuple(tup): 
    str =  ';'.join(tup) 
    return str

if __name__ == '__main__':
    try:
        conn = connect (
            dbname = "grant",
            user = "aravt",
            host = "localhost",
            password = "Pass123"
        )
        cursor = conn.cursor()
        cursor1 = conn.cursor()
    except Exception as err:
        cursor = None
        print ("psycopg2 error:", err)
    if cursor != None:
        query = """
        select 
            id, project_url 
        from grant_crawled_new_missing
        ;
            """
        cursor.execute(query)
        result =cursor.fetchall()
        count = 0
        for num, row in tqdm(enumerate(result)):
            print('url', count, row[0], row[1])
            count += 1
            id = row[0]
            url = row[1]
            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}, verify=False, timeout = 30)
            # print(count, ". request done: ", url)
            soup = BeautifulSoup(r.text, "html.parser")
            phones = soup.select("#detail-page > div:nth-child(2) > div > div.row.hidden-xs > div > div:nth-child(3) > ol > li:nth-child(2) > a:nth-child(2) > div")
            if phones:
                print("found phone", phones[0].get_text())
                phone = phones[0].get_text()
                update_query = "update grant_crawled_new_missing set researcher = '{}' where id = {}".format(phone, id)

                cursor1.execute(update_query)
                conn.commit()

        cursor.close()
        conn.close()