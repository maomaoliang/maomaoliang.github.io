---
title: 5分钟搭建HEXO博客
categories:
  - 技术笔记
tags:
  - Hexo
abbrlink: cf7806b
date: 2018-04-21 19:27:00
---

**说明：**

1.安装过程真的几乎不需要懂node.js、git的知识，像我这样的小白也能简单安装。
2.一定要注意搭建过程中的细节，否则各种报错。

### 参考资料

1.[官方教程](https://hexo.io/zh-cn/docs/)
2.[CSDN文章](https://blog.csdn.net/gdutxiaoxu/article/details/53576018)

### 搭建步骤

#### 步骤1：安装必要的环境

1.[下载并安装node.js](https://nodejs.org/en/)
2.[下载并安装git](https://git-scm.com/downloads)

注：以上两个软件安装过程，一路点击下一步即可。

#### 步骤2：创建博客项目的文件夹

比如，我自己在D盘创建了名为“hexo”的文件夹，那么这个hexo文件夹将会生成所有的hexo博客资源文件

#### 步骤3：安装hexo

1.进入hexo文件夹，右键选择`Git bash`
2.输入以下命令，按回车执行

1

npm install -g hexo-cli

#### 步骤4：在hexo文件夹中，创建所需要的文件

1

hexo init

#### 步骤5：在hexo文件夹中，创建所需要的文件

安装Node.js依赖包，输入命令，回车

1

npm install

#### 步骤6：本地查看网站是否可以正常访问

- 在`D:\Hexo`文件夹中，右键鼠标，选择Git bash，输入命令

1

2

hexo generate

hexo server

- 在浏览器中输入：localhost:4000，查看本地网站是否可以访问

7.本地网站搭建完成

        完成以上步骤，表示你已经成功建立了本地的网站，但是本地网站只有你能看到，我们怎么才能让全世界的同学也能访问博客呢？
这就要依靠Github这个知名的开（zhuang）发（bi）社区，我们需要将自己电脑的网站上传到Github上面，让Github免费为我们提供线上的服务器。

        接下来介绍，如何将本地网站文件，上传到Github上，以方便全世界，注意是全世界的朋友都来访问的博客（谁TM闲的蛋疼会来访问呢，额，管他呢，whatever  -。-）。

      
    

    

    
    
    

    
      

        

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
