# -*- coding: utf-8 -*-
import scrapy
from tuniu.items import TuniuItem


# 创建一个爬虫类
class TuniuSpider(scrapy.Spider):
    # 爬虫名
    name = "tuniu"
    # 允许爬虫作用的范围
    allowed_domains =["http://www.tuniu.com/domestic/"]
    index = 0
    start_urls = ["http://www.tuniu.com/guide/d-sanya-906/?pcat=67",
           "http://www.tuniu.com/guide/v-wuzhizhoudao-4780/?pcat=67",
            "http://www.tuniu.com/guide/d-haikou-902/?pcat=67",
            "http://www.tuniu.com/guide/v-yalongwan-5823/?pcat=67",
            "http://www.tuniu.com/guide/v-tianyahaijiao-91/?pcat=67",
            "http://www.tuniu.com/guide/d-xisha-41865/",
            "http://www.tuniu.com/guide/d-linshuilizuzizhixian-784380/",
            "http://www.tuniu.com/guide/v-sanyawan-3271/",
            "http://www.tuniu.com/guide/v-dadonghai-5820/?pcat=67",
            "http://www.tuniu.com/guide/v-xiaodonghai-5962/",
            "http://www.tuniu.com/guide/v-haitangwan-46545/",
            "http://www.tuniu.com/guide/d-lijiang-3312/?pcat=82",
            "http://www.tuniu.com/guide/d-dali-3306/?pcat=82",
            "http://www.tuniu.com/guide/d-xishuangbanna-3318/?pcat=82",
            "http://www.tuniu.com/guide/v-luguhu-50068/?pcat=82",
            "http://www.tuniu.com/guide/d-kunming-3302/?pcat=82",
            "http://www.tuniu.com/guide/v-yulongxueshan-50067/?pcat=82",
            "http://www.tuniu.com/guide/v-erhai-1169184/",
            "http://www.tuniu.com/guide/v-puzhehei-6000/?pcat=82",
            "http://www.tuniu.com/guide/d-xianggelila-3322/?pcat=82",
            "http://www.tuniu.com/guide/d-tengchong-3323/?pcat=82",
            "http://www.tuniu.com/guide/d-shanghai-2500/?pcat=317",
            "http://www.tuniu.com/guide/v-shdsnly-1994829/?pcat=317",
            "http://www.tuniu.com/guide/d-hangzhou-3402/?pcat=317"
            "http://www.tuniu.com/guide/d-suzhou-1615/?pcat=317",
            "http://www.tuniu.com/guide/d-yangzhou-1622/?pcat=317",
            "http://www.tuniu.com/guide/v-huangshan-134/?pcat=317",
            "http://www.tuniu.com/guide/d-wuyuan-1715/?pcat=102",
            "http://www.tuniu.com/guide/v-wuzhen-50241/?pcat=317",
            "http://www.tuniu.com/guide/d-nanjing-1602/?pcat=317",
            "http://www.tuniu.com/guide/v-pts-8501/?pcat=317",
            "http://www.tuniu.com/guide/v-qdhfjmsq-47300/?pcat=317",
            "http://www.tuniu.com/guide/v-zhouzhuang-4467/?pcat=317",
            "http://www.tuniu.com/guide/v-lushan-374/?pcat=102",
            "http://www.tuniu.com/guide/v-xitang-50013/?pcat=317",
            "http://www.tuniu.com/guide/d-nanchang-1702/?pcat=102",
            "http://www.tuniu.com/guide/d-chengdu-2802/?pcat=163",
            "http://www.tuniu.com/guide/v-jzg-23/?pcat=163",
            "http://www.tuniu.com/guide/v-emeishan-9755/?pcat=163",
            "http://www.tuniu.com/guide/v-dujiangyan-39166/?pcat=163",
            "http://www.tuniu.com/guide/v-yading-143/",
            "http://www.tuniu.com/guide/d-sedaxian-42027/?pcat=163",
            "http://www.tuniu.com/guide/v-daxiongmaofanyuyanjiujidi-9132/?pcat=163",
            "http://www.tuniu.com/guide/v-xilingxueshan-1436/?pcat=163",
            "http://www.tuniu.com/guide/v-siguniangshan-754/?pcat=163",
            "http://www.tuniu.com/guide/d-xichang-2828/?pcat=163",
            "http://www.tuniu.com/guide/d-wulong-327/?pcat=302",
            "http://www.tuniu.com/guide/v-dazushike-658/?pcat=302",
            "http://www.tuniu.com/guide/d-chengdu-2802/?pcat=163",
            "http://www.tuniu.com/guide/v-jzg-23/?pcat=163",
            "http://www.tuniu.com/guide/v-emeishan-9755/?pcat=163",
            "http://www.tuniu.com/guide/v-dujiangyan-39166/?pcat=163",
            "http://www.tuniu.com/guide/v-yading-143/",
            "http://www.tuniu.com/guide/d-sedaxian-42027/?pcat=163",
            "http://www.tuniu.com/guide/v-daxiongmaofanyuyanjiujidi-9132/?pcat=163",
            "http://www.tuniu.com/guide/v-xilingxueshan-1436/?pcat=163",
            "http://www.tuniu.com/guide/v-siguniangshan-754/?pcat=163",
            "http://www.tuniu.com/guide/d-xichang-2828/?pcat=163",
            "http://www.tuniu.com/guide/d-zhangjiajie-1514/?pcat=181",
            "http://www.tuniu.com/guide/d-changsha-1502/?pcat=181",
            "http://www.tuniu.com/guide/v-fenghuanggucheng-1425/?pcat=181",
            "http://www.tuniu.com/guide/v-wudangshan-189/?pcat=255",
            "http://www.tuniu.com/guide/v-sxdb-1361/?pcat=255",
            "http://www.tuniu.com/guide/d-shennongjia-1412/?pcat=255",
            "http://www.tuniu.com/guide/d-enshi-1403/?pcat=255",
            "http://www.tuniu.com/guide/v-zhangjiajieguojiasenlingongyuan-10124/?pcat=181",
            "http://www.tuniu.com/guide/v-tianmenshan-992/?pcat=181",
            "http://www.tuniu.com/guide/v-zjjdxgblq-1925647/?pcat=181",
            "http://www.tuniu.com/guide/d-xian-2702/?pcat=247",
            "http://www.tuniu.com/guide/v-qshdlbmybwg-1351/?pcat=247",
            "http://www.tuniu.com/guide/v-huashan-20/?pcat=247",
            "http://www.tuniu.com/guide/v-sxhhhkpb-50196/?pcat=247",
            "http://www.tuniu.com/guide/v-huaqinggong-8127/?pcat=247",
            "http://www.tuniu.com/guide/d-kaifeng-1208/?pcat=211",
            "http://www.tuniu.com/guide/v-slsfjmsq-464/?pcat=211",
            "http://www.tuniu.com/guide/d-luoyang-1210/?pcat=211",
            "http://www.tuniu.com/guide/v-longmenshikujingqu-50148/?pcat=211",
            "http://www.tuniu.com/guide/d-eerduosi-2106/?pcat=193",
            "http://www.tuniu.com/guide/d-hulunbeier-2107/?pcat=193",
            "http://www.tuniu.com/guide/v-xilamurencaoyuan-50511/?pcat=193",
            "http://www.tuniu.com/guide/d-ejinaqi-40394/?pcat=193",
            "http://www.tuniu.com/guide/v-manzhouli-7007/",
            "http://www.tuniu.com/guide/v-aershan-3085/?pcat=193",
            "http://www.tuniu.com/guide/d-huhehaote-2102/?pcat=193",
            "http://www.tuniu.com/guide/v-wulanhaote-47515/",
            "http://www.tuniu.com/guide/d-rizhao-2415/?pcat=229",
            "http://www.tuniu.com/guide/d-qingdao-2413/?pcat=229",
            "http://www.tuniu.com/guide/d-weihai-2418/?pcat=229",
            "http://www.tuniu.com/guide/d-yantai-2419/?pcat=229",
            "http://www.tuniu.com/guide/v-penglai-2312/?pcat=229",
            "http://www.tuniu.com/guide/v-taishan-5242/?pcat=229",
            "http://www.tuniu.com/guide/d-jinan-2402/?pcat=229",
            "http://www.tuniu.com/guide/v-qufu-4765/?pcat=229",
            "http://www.tuniu.com/guide/d-xiamen-414/?pcat=133",
            "http://www.tuniu.com/guide/v-gulangyu-364/?pcat=133",
            "http://www.tuniu.com/guide/v-wuyishan-2781/?pcat=133",
            "http://www.tuniu.com/guide/v-yongdingtulou-2616/?pcat=133",
            "http://www.tuniu.com/guide/v-zzysy-37599/?pcat=133",
            "http://www.tuniu.com/guide/v-xunliaowan-3696/?pcat=272",
            "http://www.tuniu.com/guide/d-shen-619/?pcat=272",
            "http://www.tuniu.com/guide/d-guangzhou-602/?pcat=272",
            "http://www.tuniu.com/guide/v-zhuhaichanglonghaiyangwangguo-1791699/?pcat=272",
            "http://www.tuniu.com/guide/v-changlongyeshengdongwuyuan-38344/?pcat=272",
            "http://www.tuniu.com/guide/d-huizhou-609/?pcat=272",
            "http://www.tuniu.com/guide/d-guilin-705/?pcat=240",
            "http://www.tuniu.com/guide/d-beihai-704/?pcat=240",
            "http://www.tuniu.com/guide/d-yangshuo-716/?pcat=240",
            "http://www.tuniu.com/guide/d-nanning-702/?pcat=240",
            "http://www.tuniu.com/guide/v-lijiangyouchuan-160/?pcat=240",
            "http://www.tuniu.com/guide/v-tonglingdaxiagu-3298/?pcat=240",
            "http://www.tuniu.com/guide/v-zhoudao-6236/?pcat=240",
            "http://www.tuniu.com/guide/v-longjititian-161/?pcat=240",
            "http://www.tuniu.com/guide/v-cbsfjq-151/?pcat=382",
            "http://www.tuniu.com/guide/v-jingbohufengjingqu-1377/?pcat=382",
            "http://www.tuniu.com/guide/d-haerbin-1102/?pcat=382",
            "http://www.tuniu.com/guide/d-shenyang-1902/?pcat=382",
            "http://www.tuniu.com/guide/d-changchun-1802/?pcat=382",
            "http://www.tuniu.com/guide/d-dalian-1906/?pcat=382",
            "http://www.tuniu.com/guide/v-mohe-174/?pcat=382",
            "http://www.tuniu.com/guide/d-jilin-1808/?pcat=382",
            "http://www.tuniu.com/guide/v-zhalong-13325/",
            "http://www.tuniu.com/guide/v-wudalianchi-235/?pcat=382",
            "http://www.tuniu.com/guide/d-lasa-3202/?pcat=217",
            "http://www.tuniu.com/guide/d-linzhi-3205/?pcat=217",
            "http://www.tuniu.com/guide/v-budalagong-33/?pcat=217",
            "http://www.tuniu.com/guide/d-rikaze-3207/?pcat=217",
            "http://www.tuniu.com/guide/v-zhufengdabenying-34/?pcat=217",
            "http://www.tuniu.com/guide/v-namucuo-4222/?pcat=217",","
            "http://www.tuniu.com/guide/d-guiyang-802/?pcat=304",
            "http://www.tuniu.com/guide/v-huangguoshupubu-436/?pcat=304",
            "http://www.tuniu.com/guide/d-liboxian-42130/?pcat=304",
            "http://www.tuniu.com/guide/v-xijiangqianhumiaozhai-1367/?pcat=304",
            "http://www.tuniu.com/guide/v-jingshan-468/?pcat=304",
            "http://www.tuniu.com/guide/v-zhijindong-11943/?pcat=304",
            "http://www.tuniu.com/guide/v-wanfenglinjingqu-8153/?pcat=304",
            "http://www.tuniu.com/guide/d-wulumuqi-3102/?pcat=204",
            "http://www.tuniu.com/guide/v-tianshantianchifengjingqu-596/?pcat=204",
            "http://www.tuniu.com/guide/d-tulufan-3118/?pcat=204",
            "http://www.tuniu.com/guide/v-kanasijingqu-35566/?pcat=204",
            "http://www.tuniu.com/guide/v-nalaticaoyuan-5340/?pcat=204",
            "http://www.tuniu.com/guide/v-hemu-39785/?pcat=204",
            "http://www.tuniu.com/guide/d-kashi-3111/?pcat=204",
            "http://www.tuniu.com/guide/v-luobubo-47483/",
            "http://www.tuniu.com/guide/d-gansu-500/?pcat=365",
            "http://www.tuniu.com/guide/v-dunhuang-39203/?pcat=365",
            "http://www.tuniu.com/guide/v-qinghaihu-145/?pcat=365",
            "http://www.tuniu.com/guide/d-zhangye-515/?pcat=365",
            "http://www.tuniu.com/guide/d-ningxia-2200/?pcat=365",
            "http://www.tuniu.com/guide/d-yinchuan-2202/?pcat=365",
            "http://www.tuniu.com/guide/v-menyuan-38094/",
            "http://www.tuniu.com/guide/d-gannan-506/?pcat=365",
            "http://www.tuniu.com/guide/d-jiayuguan-516/?pcat=365",
            "http://www.tuniu.com/guide/d-xining-2302/?pcat=365",
            "http://www.tuniu.com/guide/v-chakayanhu-36231/?pcat=365",
            "http://www.tuniu.com/guide/v-mogaoku-695/?pcat=365",
            "http://www.tuniu.com/guide/v-yadanmoguicheng-698/?pcat=365",
            "http://www.tuniu.com/guide/v-qilianxian-42547/",
            "http://www.tuniu.com/guide/v-zhuoershan-1807428/?pcat=365",
            "http://www.tuniu.com/guide/v-yungangshiku-1442/?pcat=416",
            "http://www.tuniu.com/guide/v-pingyaogucheng-169/?pcat=416",
            "http://www.tuniu.com/guide/v-qiaojiadayuan-1565/?pcat=416",
            "http://www.tuniu.com/guide/d-taiyuan-2602/?pcat=416",
            "http://www.tuniu.com/guide/d-datong-2604/?pcat=416",
            "http://www.tuniu.com/guide/v-sxwtsfjmsq-1578/?pcat=416",
            "http://www.tuniu.com/guide/v-hyjds-3088045/"]

    def parse(self, response):
        block_list = response.xpath('//div[contains(@class,"listitem clearfix")]')
        # blockitem = []
        for block in block_list:
            item = TuniuItem()
            title = block.xpath('.//div[@class="product"]//a/@title').extract()
            traveltype = block.xpath('.//div[@class="extra"]/span[1]/text()').extract()
            travelway = block.xpath('.//div[@class="extra"]/span[contains(@class,"label_icon")][2]/text()').extract()
            startplace = block.xpath('.//span[@class="extra-startplace"]/text()').extract()
            extrashortdesc = block.xpath('.//span[@class="extra-shortdesc"]/text()').extract()
            tuanqi = block.xpath('.//div[@class="have_tuanqi"]/label/text()').extract()
            satisfactionrate = block.xpath('.//span[@class="rate"]/text()').extract()
            chuyou = block.xpath('.//span[@class="chuyou"]/text()').extract()
            comment = block.xpath('.//span[contains(@class,"comment")]/text()').extract()
            price = block.xpath('.//div[@class="part3 fl"]//span[@class="num"]/text()').extract()
            item['title'] = title[0]
            item['traveltype'] = traveltype
            item['travelway'] = travelway
            item['startplace'] = startplace
            item['extrashortdesc'] = extrashortdesc
            item['tuanqi'] = tuanqi
            item['satisfactionrate'] = satisfactionrate
            item['chuyou'] = chuyou
            item['comment'] = comment
            item['price'] = price
            yield item
        if self.index < 165:
            self.index += 1
        yield scrapy.Request(self.start_urls[self.index], callback=self.parse)
            # blockitem.append(item)
        # return blockitem
            # print(productname[0])
            # print(productshortdesc[0])
            # print(travelinfo[0])
            # print(tuanqi[0])
            # print(satisfactionrate[0])
            # print(chuyou[0])
            # print(comment[0])
            # print(price[0])

        # with open("sanya.html", "wb") as f:
        #     f.write(response.body)

