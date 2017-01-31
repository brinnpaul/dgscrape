import requests

from bs4 import BeautifulSoup


class ParseDG(object):

    def __init__(self, keywords):
        self.keywords = keywords
        self.base = 'http://www.dgcoursereview.com/forums/'
        self.path = 'search.php?do=getdaily'
        self.results = None

    def __get_daily(self):
        url = self.base + self.path
        r = requests.get(url)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find_all('a')
        links = []
        for l in body:
            if 'thread_title' in str(l):
                link = self.base+l.get('href')
                link_title = l.get_text()
                links.append({'title': link_title, 'link': link})
        return links

    @staticmethod
    def __parse_for_keyword(obj, keyword):
        if not isinstance(obj, object):
            raise ValueError("Link must be object")
        r = requests.get(obj['link'])
        page_result = r.text
        if keyword in page_result.lower():
            return True

    def __match(self, obj_list):
        keywords = self.keywords
        if not isinstance(keywords, list):
            raise ValueError("Keywords must be array")
        matches = {}
        parse = self.__parse_for_keyword
        for key in keywords:
            list_of_links = list(filter(lambda x: parse(x, key), obj_list))
            if len(list_of_links) == 0:
                list_of_links = ['No Results!']
            matches[key] = list_of_links
        return matches

    def __format(self, match_list):
        text = ""
        for key in match_list:
            matches = match_list[key]
            text += 'Keyword: {} \n'.format(key.upper())
            for match in matches:
                text += 'Article: {} \n\tLink: {} \n'.format(match['title'], match['link'])
            text += '\n'
        return text

    def run(self):
        try:
            links = self.__get_daily()
            matches = self.__match(links)
            formatted_matches = self.__format(matches)
            self.results = formatted_matches
        except Exception as e:
            print e

