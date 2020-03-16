from psycopg2 import connect, sql
import sys
import extract_emails
import re
from tqdm import tqdm
import signal

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
        # query = """
        #     select id, project_id_original 
        #     from grant_crawled_new_important1 
        #     where award_amount is null
        #         and project_id_original is not null;
        #     """
        query = """
select 
    id, project_id_original 
from grant_crawled_new_missing
where id between 24380 and 49358
    and award_amount is null
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
            if url != None:
                url = 'http://' + url
                if row[1] != None:
                    try:
                        em = extract_emails.ExtractEmails(url, depth=20, print_log=True, ssl_verify=True, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0', request_delay=0.0)
                    except KeyboardInterrupt:
                        raise
                    except:
                        em = None
                    if em:
                        emails = em.emails
                    else:
                        emails =[]
                    if emails != []:
                        emailstr = convertTuple(emails)
                        ins_query = "update grant_crawled_new_missing set researcher_en = '{}', award_amount = '2' where id = {}".format(emailstr, id)
                        cursor1.execute(ins_query)
                    else:
                        ins_query = "update grant_crawled_new_missing set award_amount = '2' where id = {}".format(id)
                        cursor1.execute(ins_query)
                    conn.commit()
                else:
                    ins_query = "update grant_crawled_new_missing set award_amount = '2' where id = {}".format(id)
                    cursor1.execute(ins_query)
                    conn.commit()
        cursor.close()
        conn.close()