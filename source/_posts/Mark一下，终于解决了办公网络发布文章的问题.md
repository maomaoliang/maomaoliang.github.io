---
title: "Mark一下，终于解决了办公网络发布文章的问题"
date: 2018-10-23T21:11:00+08:00
categories:
  - 技术笔记
tags:
  - Hexo
---

yo yo yo ,  I have solved the fucking oa-net…marked

修改的depoly的配置即可. 修改站点配置文件`.config.yml`

原配置：

1

2

3

4

deploy:

  type: git

  repository: git@github.com:maomaoliang/maomaoliang.github.io.git

  branch: master

修改后配置：

1

2

3

4

deploy:

  type: git

  repository:  https://github.com/maomaoliang/maomaoliang.github.io.git

  branch: master

总结一句话：

办公网络不支持：git 协议、ssh 方式 clone repo，需要用 https 协议，并且设置公司 http 代理。

所以,git测试肯定是不会通的。

1

$ ssh git@github.com

**PS：根本不需要设置git代理~**

      
    

    

    
    
    

    
      

        

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
