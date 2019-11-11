import re
import cfscrape
from bs4 import BeautifulSoup
import json
cfscrape.DEFAULT_CIPHERS += ':!SHA'
scraper = cfscrape.create_scraper()


# Fetch links from a category
# base_url = "https://mcumovieshome.com/category/animated/page/"
# links = []
# for i in range(1, 12):
#     response = (scraper.get(base_url+str(i)).content)
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('h2', class_="entry-title"):
#         children = anchor.findChildren("a", recursive=False)
#         links.append(children[0].get('href'))
# print(links)


# ACTUAL CODE TO FETCH LINKS
# links = []
# final_links = {}
# unfinished_links = []
# regexList = ['linkshub.me/view/',
#              'linkshub.live/view/',
#              'linkshub.co/view/',
#              'linkshub.trade/view/',
#              'miniurl.pw/',
#              'linksad.net/',
#              'clk.link/',
#              'clk.ink/',
#              'mcupaste.com/',
#              '4shrink.com/',
#              'ashr.ink/',
#              'acefile.co/',
#              'yuudrive.me/',
#              'za.gl/']
# for link in links:
#     response = (scraper.get(link).content)
#     soup = BeautifulSoup(response, 'html.parser')
#     try:
#         value = final_links[soup.title.text]
#     except KeyError:
#         cur_link = {}

#         for a in soup.find_all('a'):
#             for regex in regexList:
#                 href = re.findall(r'https?://'+regex +
#                                   r'[a-z0-9A-Z]{3,15}', str(a))
#                 # href = re.findall(r'https://'+regex+r'.([a-z]*/)+[a-z0-9A-Z]{3,15}', str(a))
#                 if len(href) > 0:
#                     for link in href:
#                         try:
#                             value = cur_link[a.text]
#                             cur_link[a.text].append(link)
#                         except KeyError:
#                             cur_link[a.text] = [link]
#         if len(cur_link) > 0:
#             final_links[soup.title.text] = cur_link
#         else:
#             unfinished_links.append(link)
# # print(final_links)
# print(unfinished_links)

# json = json.dumps(final_links)
# f = open("animated3.json", "a")
# f.write(json)
# f.close()

# f = open("unfin_animated.js", "w")
# f.write("\n".join(str(item) for item in unfinished_links))
# f.close()


# OLD VERSION
# link = 'https://mcumovieshome.com/the-death-of-superman-2018-1080p-10bit-bluray-english-6ch-x265-hevc-570-mb-google-drive-mega/'
# response = (scraper.get(link).content)
# soup = BeautifulSoup(response, 'html.parser')
# # urls = re.findall(r'href=[\'\"]?https://miniurl.pw/[a-z0-9A-Z]{5,6}[\'\"]?', response)
# final_links = []
# # for link in links:
# response = (scraper.get(link).content)
# soup = BeautifulSoup(response, 'html.parser')
# cur_link = {}
# regexList = [r'href=[\'\"]https://linkshub.me/view/[a-z0-9A-Z]{3,15}[\'\"]',
#              r'href=[\'\"]https://miniurl.pw/view/[a-z0-9A-Z]{3,15}[\'\"]']
# for div in soup.find_all('div', class_="entry-inner"):
#     for p in div.find_all('p'):
#         for a in p.find_all('a'):
#             for regex in regexList:
#                 href = re.findall(regex, str(a))
#                 if(len(href) > 0 and len(href[0])):
#                     link = href[0][6:-1]
#                     try:
#                         value = cur_link[a.text]
#                         cur_link[a.text].append(link)
#                     except KeyError:
#                         cur_link[a.text] = [link]
# cur = {}
# cur[soup.title.text] = cur_link
# final_links.append(cur)
# print(final_links)


# Regex syntax
# re.findall(r'href=[\'\"]https://miniurl.pw/[a-z0-9A-Z]{5,6}[\'\"]', str(hreff))


# TO FIND HOST LINKS
# for a in soup.find_all('a'):
#     res = re.findall(r'mcu', str(a.get('href')))
#     res2 = re.findall(r'www', str(a.get('href')))
#     if len(res)>0 or len(res2)>0:
#         continue
#     else:
#         print(a.get('href'))


# Fetch CATEGORIES
# base_url = "https://mcumovieshome.com/"
# links = {}
# for i in range(1, 12):
#     response = (scraper.get(base_url+str(i)).content)
#     soup = BeautifulSoup(response, 'html.parser')
#     for a in soup.find_all('a'):
#         link = re.findall(r'https://mcumovieshome.com/category/[a-z]{3,25}/', str(a.get('href')))
#         if(len(link)>0):
#             links[a.text] = link[0]
# print(links)
# json = json.dumps(links)
# f = open("categories.json", "a")
# f.write(json)
# f.close()


categories = {
    "Action": "https://mcumovieshome.com/category/action/",
    "Adventure": "https://mcumovieshome.com/category/adventure/",
    "Biography": "https://mcumovieshome.com/category/biography/",
    "Comedy": "https://mcumovieshome.com/category/comedy/",
    "Crime": "https://mcumovieshome.com/category/crime/",
    "Documentary": "https://mcumovieshome.com/category/documentary/",
    "Drama": "https://mcumovieshome.com/category/drama/",
    "Family": "https://mcumovieshome.com/category/family/",
    "Fantasy": "https://mcumovieshome.com/category/fantasy/",
    "History": "https://mcumovieshome.com/category/history/",
    "Horror": "https://mcumovieshome.com/category/horror/",
    "Musical": "https://mcumovieshome.com/category/musical/",
    "Mystery": "https://mcumovieshome.com/category/mystery/",
    "Romance": "https://mcumovieshome.com/category/romance/",
    "Sport": "https://mcumovieshome.com/category/sport/",
    "WWE": "https://mcumovieshome.com/category/wwe/",
    "Thriller": "https://mcumovieshome.com/category/thriller/",
    "War": "https://mcumovieshome.com/category/war/",
    "Western": "https://mcumovieshome.com/category/western/",
    "French": "https://mcumovieshome.com/category/french/",
    "German": "https://mcumovieshome.com/category/german/",
    "HBO": "https://mcumovieshome.com/category/hbo/",
    "Hulu": "https://mcumovieshome.com/category/hulu/",
    "Indonesian": "https://mcumovieshome.com/category/indonesian/",
    "Japenese": "https://mcumovieshome.com/category/japenese/",
    "Korean": "https://mcumovieshome.com/category/korean/",
    "Music": "https://mcumovieshome.com/category/musical/",
    "Netflix": "https://mcumovieshome.com/category/netflix/",
    "Russian": "https://mcumovieshome.com/category/russian/",
    "Uncategorized": "https://mcumovieshome.com/category/uncategorized/"
}

for category, curl in categories.items():
    base_url = curl
    print(base_url+'page/')
    links = []
    for i in range(1, 12):
        response = (scraper.get(base_url+'page/'+str(i)).content)
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('h2', class_="entry-title"):
            children = anchor.findChildren("a", recursive=False)
            links.append(children[0].get('href'))
    # print(links)

    final_links = {}
    unfinished_links = []
    regexList = ['linkshub.me/view/',
                 'linkshub.live/view/',
                 'linkshub.co/view/',
                 'linkshub.trade/view/',
                 'miniurl.pw/',
                 'linksad.net/',
                 'clk.link/',
                 'clk.ink/',
                 'mcupaste.com/',
                 '4shrink.com/',
                 'ashr.ink/',
                 'acefile.co/',
                 'yuudrive.me/',
                 'za.gl/']
    for link in links:
        response = (scraper.get(link).content)
        soup = BeautifulSoup(response, 'html.parser')
        try:
            value = final_links[soup.title.text]
        except KeyError:
            cur_link = {}

            for a in soup.find_all('a'):
                for regex in regexList:
                    href = re.findall(r'https?://'+regex +
                                      r'[a-z0-9A-Z]{3,15}', str(a))
                    # href = re.findall(r'https://'+regex+r'.([a-z]*/)+[a-z0-9A-Z]{3,15}', str(a))
                    if len(href) > 0:
                        for link in href:
                            try:
                                value = cur_link[a.text]
                                cur_link[a.text].append(link)
                            except KeyError:
                                cur_link[a.text] = [link]
            if len(cur_link) > 0:
                final_links[soup.title.text] = cur_link
            else:
                unfinished_links.append(link)
    print(category)
    print(final_links)
    print(unfinished_links)

    try:
        json = json.dumps(final_links)
        fname = str(category) + '.json'
        f = open(fname, "a")
        f.write(json)
        f.close()
    except AttributeError:
        pass

    fname = 'unfin_' + str(category) + '.js'
    f = open(fname, "a")
    f.write("\n".join(str(item) for item in unfinished_links))
    f.close()
