#encoding=utf-8



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
            test = response.xpath('//div/div[@class="pj_info"]/a/span/text()').extract()
            logger.info(test)
            data = response.xpath('//div[@class="mainwrap tf"]/div/div[@class="parents w1000 tf"]/ul/li[@class="p_li clearfix"]')
            for sel in data:
                item = LianjiaItem()
                #strip(),清除空白；匹配字符串用的不太好,注意多层次选择的用法，直接从上一个标签继续，不要加//
                all['title'] = sel.xpath('div/div[@class="pj_info"]/a/span/text()').extract()
                all['location'] = sel.xpath('div/div[@class="pj_info"]/span/text()').extract()
                all['start'] = sel.xpath('div/div[@class="tzje"]/text()').extract()
                details = sel.xpath('div/ul/li/div/text()').extract()
                #去除空白，并过滤掉
                details = [x.strip() for x in  details]
                all['details'] = filter(None,details)
                for k in range(len(all['title'])):
                    item['title'] = all['title'][k].strip()
                    item['location'] = all['location'][k].strip()
                    item['start'] = all['start'][k].strip()
                    item['amount'] = all['details'][k * 8 + 1]
                    item['num_person'] = all['details'][k * 8 + 5]
                    item['progress'] = all['details'][k * 8 + 7]
                    yield  item


        #获取相关熟悉参数用@
        # for href in response.xpath('//a[@bpfilter="page"]/@href'):
            #     url = response.urljoin(href.extract())
            #     # yield scrapy.Request(url, callback=self.parse_dir_contents)
            #     print url




