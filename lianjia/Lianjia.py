#encoding=utf-8

#一个初级版本，使用自己的cookie，爬.cn下的数据。cookie请自行获取谢谢。


import scrapy
import time
from lianjia.LianjiaItems import LianjiaItem

class LianjiaSpider(scrapy.Spider):
        name = "lianjia"

        #必须感谢想出这个办法的人，模仿搜索引擎，爬取pc版有效，但是pc版要解析js
        user_agent = {'User-agent': 'spider'}



        def start_requests(self):
            return [scrapy.FormRequest("http://www.baidu.com",
                                   headers=self.user_agent)]

        def parse(self, response):
            #css方式选取元素
            #注意爬取手机版，.cn后缀
            for  page in range(1,2):
                time.sleep(1)
                url = "http://txdai.com/zhongchou/NewHouseList/Index.do?page=" + str(page)
                yield scrapy.Request(url,headers=self.user_agent,callback=self.parse_dir_contents)

        def parse_dir_contents(self, response):
            #xpath方式选取元素
            #encode('utf-8')修改编码方式  解析出的部分是子html文件，可以继续解析
            all = {}
            for sel in response.xpath('//div[@class="mainwrap tf"]/div/div[@class="parents w1000 tf"]/ul/li[@class="p_li clearfixclearfix"]'):
                item = LianjiaItem()
                #strip(),清除空白；匹配字符串用的不太好
                all['title'] = sel.xpath('//li/div/div[@class="pj_info"]/a/span/text()').extract()
                all['location'] = sel.xpath('//li/div/div[@class="pj_info"]/span/text()').extract()
                # all['start'] = sel.xpath('//div/ul/li/div[@class="d_num"]/text()').extract()
                # all['amount'] = sel.xpath('//div/div[@class="tzje"]/text()').extract()
                # all['progress'] = sel.xpath('//div/ul/li/div[@class="ajjbfb"]/text()').extract()
                for k in range(len(all['title'])):
                    item['title'] = all['title'][k]
                    item['location'] = all['location'][k]
                    # item['start'] = all['start'][k]
                    # item['progress'] = all['progress'][k]
                    # item['amount'] = all['amount'][k]
                    yield  item


        #获取相关熟悉参数用@
        # for href in response.xpath('//a[@bpfilter="page"]/@href'):
            #     url = response.urljoin(href.extract())
            #     # yield scrapy.Request(url, callback=self.parse_dir_contents)
            #     print url




