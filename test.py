import extract_emails

url = 'http://' +  'www.ihq.com'
# print(url)
em = extract_emails.ExtractEmails(url, depth=10, print_log=True, ssl_verify=True, user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0', request_delay=0.0)

print(em.emails)


# http://ww1.ihq.com/?sub1=157c433a-6694-11ea-9bd6-d94c5237a6de

# http://ww1.ihq.com/?sub1=157c433a-6694-11ea-9bd6-d94c5237a6de