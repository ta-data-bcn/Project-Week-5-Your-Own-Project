from WebRequest import WebRequest

date_range = '/1.1.2006_15.2.2020'
sites = {
    'ibex_35':'/index/historical-prices/ibex_35'
}
ajax_call = {
    'ibex_35':'/Ajax/IndicesController_HistoricPriceList/ibex_35/1.1.2006_15.2.2020/true'
}

if __name__ == '__main__':
    wr = WebRequest('https://markets.businessinsider.com')
    
    wr.GET_url(sites['ibex_35'] + date_range)
    if wr.status == 200:
        atcrvs = wr.soup.find_all('input',{'name':'__atcrv'})
        aths = wr.soup.find_all('input',{'name':'__ath'})
        atts = wr.soup.find_all('input',{'name':'__atts'})

        print(eval(atcrvs[0]['value']))
        print(aths[0]['value'])
        print(atts[0]['value'])
        data = {
            ":authority":"markets.businessinsider.com",
            ":method":"POST",
            ":path":"/Ajax/IndicesController_HistoricPriceList/ibex_35/1.1.2006_15.2.2020/true",
            ":scheme":"https",
            "__atcrv":eval(atcrvs[0]['value']),
            "__ath":aths[0]['value'],
            "__atts":atts[0]['value'],
            "accept":"*/*",
            "accept-encoding":"gzip, deflate, br",
            "accept-language":"es,ca;q=0.9,en;q=0.8",
            "content-length":"0",
            "cookie":wr.response.cookies.get_dict(),
            "origin":"https://markets.businessinsider.com",
            "referer":"https://markets.businessinsider.com/index/historical-prices/ibex_35/1.1.2006_15.2.2020",
            "sec-fetch-mode":"cors",
            "sec-fetch-site":"same-origin",
            "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
            "x-requested-with":"XMLHttpRequest"
        }
        
        wr.POST_url(ajax_call['ibex_35'], data)
        print(wr.soup.find_all('table'))
