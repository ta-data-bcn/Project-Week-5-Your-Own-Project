import requests
from bs4 import BeautifulSoup

class WebRequest:
    def __init__(self, base_url, ext_get='', ext_post=''):
        self.status = 404
        self.response = False
        self.session = requests.Session()
        self.base_url = base_url
        self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        self.res = ''
        self.soup = ''
        self.ext_get = ext_get
        self.ext_post = ext_post

    def POST_url(self, ext, data):
        print(self.base_url + ext)
        self.response = self.session.post(self.base_url + ext, data=data)
        print(self.response)
        self.status = self.response.status_code
        if self.status == 200:
            self.res = self.response.text
            self.soup = BeautifulSoup(self.res, 'html.parser')

    def GET_url(self, ext):
        self.response = self.session.get(self.base_url + ext, headers=self.header)
        self.status = self.response.status_code
        if self.status == 200:
            self.res = self.response.text
            self.soup = BeautifulSoup(self.res, 'html.parser')
    
    def get_elements(self, soup, elem_name):
        elems = soup.find_all(elem_name)
        return [elem.extract() for elem in elems]

    def get_text_in_elements_from_list(self, res, elem_name):
        elems = []
        for elem in res:
            tmp = elem.find_all(elem_name)
            for t in tmp:
                elems.append(t.text)
        return elems
