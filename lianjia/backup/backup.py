#encoding=utf-8

#一个初级版本，使用自己的cookie，爬.cn下的数据。cookie请自行获取谢谢。


import scrapy
import time
from lianjia.LianjiaItems import LianjiaItem
import logging


logger = logging.getLogger('LianjiaLogger')
class LianjiaSpider(scrapy.Spider):
        name = "lianjia"


        #必须感谢想出这个办法的人，模仿搜索引擎，爬取pc版有效，但是pc版要解析js
        user_agent = {'User-agent': 'spider'}



        def start_requests(self):
            return [scrapy.FormRequest("http://txdai.com/",
                                   headers=self.user_agent)]

        def parse(self, response):
            #css方式选取元素
            #注意爬取手机版，.cn后缀
            for  page in range(1,2):
                time.sleep(2)
                url = "http://txdai.com/zhongchou/NewHouseList/Index.do?page=" + str(page)
                yield scrapy.Request(url,headers=self.user_agent,callback=self.parse_dir_contents)

        def parse_dir_contents(self, response):
            #xpath方式选取元素
            #encode('utf-8')修改编码方式  解析出的部分是子html文件，可以继续解析
            all = {}
            for sel in response.xpath('//div[@class="mainwrap tf"]/div/div[@class="parents w1000 tf"]/ul/li[@class="p_li clearfix"]'):
                item = LianjiaItem()
                #strip(),清除空白；匹配字符串用的不太好
                all['title'] = sel.xpath('//li/div/div[@class="pj_info"]/a/span/text()').extract()
                all['location'] = sel.xpath('//li/div/div[@class="pj_info"]/span/text()').extract()
                all['amount'] = sel.xpath('//li/div/ul/li/div[@class="d_num"]/text()').extract()
                all['start'] = sel.xpath('//li/div/div[@class="tzje"]/text()').extract()
                #去除空白，并过滤掉
                progress = sel.xpath('//li/div/ul/li/div[@style="margin: 6px auto 0;"]/text()').extract()
                progress = [x.strip() for x in  progress]
                all['progress'] = filter(None,progress)
                logger.info(all['start'])
                for k in range(len(all['title'])):
                    item['title'] = all['title'][k].strip()
                    item['location'] = all['location'][k].strip()
                    item['amount'] = all['amount'][k * 3].strip()
                    item['start'] = all['start'][k].strip()
                    item['progress'] = all['progress'][k].strip()

                    yield  item


        #获取相关熟悉参数用@
        # for href in response.xpath('//a[@bpfilter="page"]/@href'):
            #     url = response.urljoin(href.extract())
            #     # yield scrapy.Request(url, callback=self.parse_dir_contents)
            #     print url




