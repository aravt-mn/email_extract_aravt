# from .extract_emails import extract_emails
import extract_emails
import re
import sys

if __name__ == '__main__':
    urls = [
    'fantasyfarm.ca/',
    'fountainblu.ca',
    'charlottemuseum.org',
    'www.hilton.com',
    'blackcreek.bypeterandpauls.com',
    'www.wyndhamhotels.com',
    'bravodjs.ca',
    'www.cceventcentre.ca',
    'skytek.ca',
    'www.signaturesrestaurant.com',
    'orangeartgallery.ca',
    'www.theaerieateaglelanding.com',
    'wabano.com',
    'www.marriott.com',
    'www.kingsarmsoakville.com',
    'www.turnberrygolf.ca',
    'www.marriott.com',
    'www.riverbendinn.ca',
    'hewwine.com',
    'www.mecknc.gov',
    'www.ramadainnlondon.com',
    'www.brooksidebanquetcentre.ca',
    'www.hilton.com',
    'losolemio.com',
    'kitchenerportugueseclub.com',
    'www.indiantrailsgc.org',
    'www.experiencegr.com',
    'www.lafontsee.us',
    'www.buffalowildwings.com',
    'www.newvintageplace.com',
    'www.jusushi.com',
    'thebullsheadtavern.com',
    'pietrosgr.com',
    'wheelhousegrandrapids.com',
    'oldgoatgr.com',
    'reservegr.com',
    'riograndsteakhouse.com',
    'speakezlounge.com',
    'www.mainstpub.com'
    ]

    for url in urls:
        url = 'http://' + url
        try:
            em = extract_emails.ExtractEmails(url, depth=20, print_log=True, ssl_verify=True, user_agent=None, request_delay=0.0)
            emails = em.emails
        except:
            if KeyboardInterrupt:
                sys.exit()
            print('error occured')
        print(url)
        print(emails)