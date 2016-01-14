#encoding=utf-8

#一个初级版本，使用自己的cookie，爬.cn下的数据。cookie请自行获取谢谢。


import scrapy
import time
from lianjia.GoldItems import GoldItem
import logging


logger = logging.getLogger('GoldLogger')
class GoldSpider(scrapy.Spider):
        name = "gold"


        #必须感谢想出这个办法的人，模仿搜索引擎，爬取pc版有效，但是pc版要解析js
        user_agent = {'User-agent': 'spider'}



        def start_requests(self):
            return [scrapy.FormRequest("http://txdai.com/",
                                   headers=self.user_agent)]

        def parse(self, response):
            #css方式选取元素
            #注意爬取手机版，.cn后缀
            for  page in range(1,345):
                time.sleep(2)
                url = "http://txdai.com/AnJuJinIndex.html?page=" + str(page)
                yield scrapy.Request(url,headers=self.user_agent,callback=self.parse_dir_contents)

        def parse_dir_contents(self, response):
            sel = response.xpath('//ul[@class="alcomment"]')
            for data in sel:
                item = GoldItem()
                name =  data.xpath('li/span[@class="alcw1txt"]/a/text()').extract()
                if name != []:
                    item['name'] = name[0].strip()
                else:
                    item['name'] = data.xpath('li/a/text()').extract()[0].strip()
                item['amount'] = data.xpath('li[@class="alcw2"]/text()').extract()[0].strip()
                item['time'] = data.xpath('li[@class="alcw3"]/text()').extract()[0].strip()
                item['benefit'] = data.xpath('li[@class="alcw4"]/text()').extract()[0].strip()
                item['percentage'] = data.xpath('li/div/text()').extract()[0].strip()
                item['minium'] = data.xpath('li[@class="alcw5"]/text()').extract()[0].strip()
                yield item




        #获取相关参数用@
        # for href in response.xpath('//a[@bpfilter="page"]/@href'):
            #     url = response.urljoin(href.extract())
            #     # yield scrapy.Request(url, callback=self.parse_dir_contents)
            #     print url




