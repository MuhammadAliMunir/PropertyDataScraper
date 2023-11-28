from urllib.request import urlopen
from bs4 import BeautifulSoup
from scraper_api import ScraperAPIClient
import json
# import urllib2
# import sendgrid
# from sendgrid.helpers.mail import *
# from textblob import TextBlob
def getData(url):
    html = urlopen(url).read()
    # client = ScraperAPIClient('a295937d4c9aed994cbef1e0df2273d3')
    # html = client.get(url = 'https://amazon.co.uk/dp/B07T44VVGF/').text
    # html = client.get(url = url).text
    soup = BeautifulSoup(html, 'lxml')
    data = json.loads(soup.find('script', type='application/json').string) #soup.find('script', type='application/json').string
    # print (data['props']['initialProps']['pageProps']['apolloState']['data']['$ROOT_QUERY.searchResults({\"path\":\"/for-sale/houses/newcastle-upon-tyne/?beds_min=3&price_max=160000&price_min=10000&q=Newcastle%20upon%20Tyne%2C%20Tyne%20%26%20Wear&results_sort=newest_listings&search_source=for-sale\"}).listings.regular.1'])
    print (data['props']['initialProps']['pageProps']['regularListingsFormatted'][0])
    # print(data)
    exit()
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text7
    text = soup.get_text()
    # print(type(text))
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # print(lines)
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    text = text.split('\n')
    # print(text)

    # for f in text:
    result = dict()
    result['Your responsibilities'] = ''
    result['Your background'] = ''
    for f in range(len(text)):
        # print(f, text[f])
        # print(f)Ihr Profil
        if 'Your responsibilities' in text[f]:
            checker = True
            counter = 1
            while(checker != False):
                # print(text[f],text[f+1])
                data = text[f + counter]
                result['Your responsibilities'] += data
                counter = counter + 1
                # print(data)
                # print('-------------------------------------------')
                # contant = TextBlob(data)
                # print(contant.noun_phrases)
                if  'Your background' in data:
                    checker = False
        if 'Your background' in text[f]:
            checker = True
            counter = 1
            while(checker != False):
                # print(text[f],text[f+1])
                data = text[f + counter]
                result['Your background'] += data
                counter = counter + 1
                # print(data)
                # print('-------------------------------------------')
                # contant = TextBlob(data)
                # print(contant.noun_phrases)
                if  'More about us' in data:
                    checker = False
    # print(result)
    print(result['Your responsibilities'])
    print('-------------------------------------------')
    contant = TextBlob(result['Your responsibilities'])
    contant.correct()
    print(contant.noun_phrases)
    # # # html = """
    # # #     <html>
    # # #     <head></head>
    # # #     <body>
    # # #         <p><b>Your Responsibilities:</b><br>
    # # #         """+ result['Your responsibilities'] +"""
    # # #         </p>
    # # #         <p><b>Your Background:</b><br>
    # # #         """+ result['Your background'] +"""
    # # #         </p>
    # # #     </body>
    # # #     </html>
    # # #     """

    # # # # print(result)
    # # # sg = sendgrid.SendGridAPIClient(api_key='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')
    # # # from_email = Email("mali.uoh@hotmail.com")
    # # # to_email = To("dagmawiassefaofc@gmail.com")
    # # # subject = "Sending with SendGrid is Fun"
    # # # content = Content("text/html", html)
    # # # # content = Content("text/plain", ''result['Your responsibilities']+ '/n'+ result['Your background'])
    # # # # content = Content("text/plain", "and easy to do anywhere, even with Python")
    # # # mail = Mail(from_email, to_email, subject, content)
    # # # response = sg.client.mail.send.post(request_body=mail.get())
    # # # print(response.status_code)
    # # # print(response.body)
    # # # print(response.headers)
    # # # if 'Price:' in text[f]:
    # # #     print(text[f],text[f+1])
    # # #     result['Price:'] = text[f+1]
    # # # # print(result)
    # # # # return result
# url = input("Please enter you url of ABB JObs: ")
url = 'https://www.zoopla.co.uk/for-sale/houses/newcastle-upon-tyne/?beds_min=3&price_max=160000&price_min=10000&q=Newcastle%20upon%20Tyne%2C%20Tyne%20%26%20Wear&results_sort=newest_listings&search_source=for-sale'
getData(url)
# getData('https://new.abb.com/jobs/details/AU75479199_E2')
# getData('url')