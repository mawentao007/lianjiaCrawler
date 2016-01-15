#encoding=utf-8

#一个初级版本，使用自己的cookie，爬.cn下的数据。cookie请自行获取谢谢。


import scrapy
import time
from lianjia.BankItems import BankItem
import logging
from scrapy.selector import Selector

logger = logging.getLogger('BankLogger')
class GoldSpider(scrapy.Spider):
        name = "bank"


        #必须感谢想出这个办法的人，模仿搜索引擎，爬取pc版有效，但是pc版要解析js
        #user_agent = {'User-agent': 'spider'}




        def start_requests(self):
            return [scrapy.FormRequest("http://www.fanglbb.com")]

        def parse(self, response):
            #css方式选取元素
            #注意爬取手机版，.cn后缀
            for  page in range(1,11):
                time.sleep(1)
                url = "http://www.fanglbb.com/front/homeAction/ajaxFundList"
                body70 = {'id':"12",'pageSize':"10",'currPage':str(page)}
                body90 = {'id':'14','pageSize':'10','currPage':str(page)}
                body95 = {'id':'16','pageSize':'10','currPage':str(page)}
                #注意请求的格式，用FormRequest
                yield scrapy.FormRequest(url,method="POST",formdata=body95,callback=self.parse_dir_contents)

        def parse_dir_contents(self, response):
            sel = response.xpath('//table/tr[@height="42"]')
            for data in sel:
                item = BankItem()
                allData = data.xpath('td').extract()
                item['name'] = Selector(text=allData[0]).xpath('//td/span/a/text()').extract()[0].strip()
                item['amount'] = Selector(text=allData[1]).xpath('//td/em/text()').extract()[0].strip()
                item['personNum'] = Selector(text=allData[2]).xpath('//td/em/text()').extract()[0].strip()
                item['benefit'] = Selector(text=allData[3]).xpath('//td/em/text()').extract()[0].strip()
                item['allBenefit'] = Selector(text=allData[4]).xpath('//td/b/text()').extract()[0].strip()
                state = Selector(text=allData[5]).xpath('//td/input/@value').extract()
                if state == []:
                    item['state'] = Selector(text=allData[5]).xpath('//td/text()').extract()[0].strip()
                else:
                    item['state'] = state[0].strip()
                yield item




        #获取相关参数用@
        # for href in response.xpath('//a[@bpfilter="page"]/@href'):
            #     url = response.urljoin(href.extract())
            #     # yield scrapy.Request(url, callback=self.parse_dir_contents)
            #     print url




