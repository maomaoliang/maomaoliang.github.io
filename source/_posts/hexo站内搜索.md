---
title: hexo站内搜索
categories:
  - 技术笔记
tags:
  - hexo
abbrlink: 398017c7
date: 2018-10-13 14:45:23
---

### 参考资料

[hexo站内搜索教程](https://www.ezlippi.com/blog/2017/02/hexo-search.html)
[hexo站内搜索教程](https://15045120.github.io)
[作者亲自教程](http://www.hahack.com/codes/local-search-engine-for-hexo/)
[next主题官网](http://theme-next.iissnan.com/)
[next最新下载](https://github.com/theme-next/hexo-theme-next/releases)

<!-- more -->

### 安装 hexo-generator-search

1

$ npm install hexo-generator-search --save

### 安装 hexo-generator-searchdb

1

$ npm install hexo-generator-searchdb --save

### 站点配置文件配置启用搜索

编辑 站点配置文件，新增以下内容到任意位置：

1

2

3

4

5

search:

  path: search.xml

  field: post

  format: html

  limit: 10000

### 主题配置文件配置添加搜索按钮

1

2

3

4

5

6

7

8

9

local_search:

  enable: true

  # if auto, trigger search by changing input

  # if manual, trigger search by pressing enter key or search button

  trigger: auto

  # show top n results per article, show all results by setting to -1

  top_n_per_article: 1

  # unescape html strings to the readable one

  unescape: false

就是这么简单！

      
    

    

    
    
    

    
      

        

    ![萧寒 wechat](/images/wechatqcode.jpg)
    
如果喜欢我，欢迎订阅我的公众号，绝不更新~

      

    

    
      

        

  
各位小可爱，打发点，赏口饭吃咯~嘤嘤嘤

  
    
打赏

  
  

    
      

        ![萧寒 微信支付](/images/reward/wechatpay_1.jpg)
        
微信支付

      

    

    
      

        ![萧寒 支付宝](/images/reward/alipay_1.jpg)
        
支付宝

      

    

    
      

        ![萧寒 比特币](/images/reward/bitcoin_1.jpg)
        
比特币
