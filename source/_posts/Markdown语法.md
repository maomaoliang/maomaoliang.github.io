---
title: "Markdown语法"
date: 2015-12-05T23:04:38+08:00
categories:
  - 技术笔记
tags:
  - Markdown
---

[Markdown 语法快速入门](https://www.appinn.com/markdown/basic.html)
[Markdown 常用语法笔记](https://ouweiya.gitbooks.io/markdown)
[Markdown 编辑器语法指南](https://segmentfault.com/markdown/)
[Markdown 在线编辑器](https://www.zybuluo.com/mdeditor)

## 概述

概述宗旨
Markdown 的目标是实现「易读易写」。

可读性，无论如何，都是最重要的。一份使用 Markdown 格式撰写的文件应该可以直接以纯文本发布，并且看起来不会像是由许多标签或是格式指令所构成。

Markdown 语法受到一些既有 text-to-HTML 格式的影响，包括 Setext、atx、Textile、reStructuredText、Grutatext 和 EtText，而最大灵感来源其实是纯文本电子邮件的格式。

总之， Markdown 的语法全由一些符号所组成，这些符号经过精挑细选，其作用一目了然。比如：在文字两旁加上星号，看起来就像`*强调*`。Markdown 的列表看起来，嗯，就是列表。Markdown 的区块引用看起来就真的像是引用一段文字，就像你曾在电子邮件中见过的那样。
兼容 HTML
Markdown 语法的目标是：成为一种适用于网络的书写语言。

Markdown 不是想要取代 HTML，甚至也没有要和它相近，它的语法种类很少，只对应 HTML 标记的一小部分。Markdown 的构想不是要使得 HTML 文档更容易书写。在我看来， HTML 已经很容易写了。Markdown 的理念是，能让文档更容易读、写和随意改。HTML 是一种发布的格式，Markdown 是一种书写的格式。就这样，Markdown 的格式语法只涵盖纯文本可以涵盖的范围。

不在 Markdown 涵盖范围之内的标签，都可以直接在文档里面用 HTML 撰写。不需要额外标注这是 HTML 或是 Markdown；只要直接加标签就可以了。
要制约的只有一些 HTML 区块元素――比如 `<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行与其它内容区隔开，还要求它们的开始标签与结尾标签不能用制表符或空格来缩进。Markdown 的生成器有足够智能，不会在 HTML 区块标签外加上不必要的 `<p>` 标签。

例子如下，在 Markdown 文件里加上一段 HTML 表格：

这是一个普通段落
md-code:

1

2

3

4

5

6

7

<table>

    <tr>

        <td>姓名</td>

        <td>年龄</td>

        <td>日期</td>

    </tr>

</table>

输出结果：

    

        
姓名

        
年龄

        
日期

    

## 标题

类 Setext 形式是用底线的形式，利用 = （最高阶标题）和 - （第二阶标题），例如：

md-code:

```
This is an H1
=============

This is an H2
-------------

```

任何数量的 `=` 和 `-` 都可以有效果。

类 Atx 形式则是在行首插入 1 到 6 个 # ，对应到标题 1 到 6 阶，例如：

md-code:

```
#一级标题(H1)

##二级标题(H2)H2标题自动会增加分隔符

######六级标题(H6)

```

如果你是个代码洁癖者，你可以选择性地「闭合」类 atx 样式的标题，这纯粹只是美观用的，若是觉得这样看起来比较舒适，你就可以在行尾加上 `#`，而行尾的 `#`数量也不用和开头一样（行首的井字符数量决定标题的阶数）：

md-code:

```
#一级标题(H1)#

##二级标题(H2)##

######六级标题(H6)######

```

## 区块引用

Markdown 标记区块引用是使用类似 email 中用 `>` 的引用方式,自己先断好行，然后在每行的最前面加上 `>`：

md-code:

1

2

3

4

5

6

>This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,

> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.

> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> 

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse

> id sem consectetuer libero luctus adipiscing.

Markdown 也允许你偷懒只在整个段落的第一行最前面加上 `>` ：

md-code:

1

2

3

4

5

6

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,

consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.

Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse

id sem consectetuer libero luctus adipiscing.

效果如下：

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisseid sem consectetuer libero luctus adipiscing.

区块引用可以嵌套（例如：引用内的引用），只要根据层次加上不同数量的 > ：

md-code:

1

2

3

4

5

> This is the first level of quoting.

>

> > This is nested blockquote.

>

> Back to the first level.

效果如下:

> This is the first level of quoting.
> 
> This is nested blockquote.

Back to the first level.

## 列表

### 无序列表

无序列表使用星号、加号或是减号作为列表标记：

md-code:

1

2

3

*   Red

*   Green

*   Blue

等同于：

1

2

3

+   Red

+   Green

+   Blue

也等同于：

1

2

3

-   Red

-   Green

-   Blue

效果:

- Red

- Green

- Blue

### 有序列表

有序列表则使用数字接着一个英文句点：
md-code:

1

2

3

1.  Bird

2.  McHale

3.  Parish

效果:

- Bird

- McHale

- Parish

很重要的一点是，你在列表标记上使用的数字并不会影响输出的 HTML 结果，上面的列表所产生的 HTML 标记为：

```

- Bird

- McHale

- Parish

```

如果你的列表标记写成：

```
1.  Bird
1.  McHale
1.  Parish

```

或甚至是：

```
3. Bird
1. McHale
8. Parish

```

你都会得到完全相同的 HTML 输出。重点在于，你可以让 Markdown 文件的列表数字和输出的结果相同，或是你懒一点，你可以完全不用在意数字的正确性。

如果你使用懒惰的写法，建议第一个项目最好还是从 1. 开始，因为 Markdown 未来可能会支持有序列表的 start 属性。

列表项目标记通常是放在最左边，但是其实也可以缩进，最多 3 个空格，项目标记后面则一定要接着至少一个空格或制表符。

要让列表看起来更漂亮，你可以把内容用固定的缩进整理好：
md-code:

1

2

3

4

5

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.

    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,

    viverra nec, fringilla in, laoreet vitae, risus.

*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.

    Suspendisse id sem consectetuer libero luctus adipiscing.

如果列表项目间用空行分开，在输出 HTML 时 Markdown 就会将项目内容用 `<p>` 标签包起来，举例来说：

1

2

*   Bird

*   Magic

会被转换为：

```

- Bird

- Magic

```

但是这个：

1

2

3

*   Bird

*   Magic

会被转换为：

```

- Bird

- Magic

```

如果要在列表项目内放进引用，那 > 就需要缩进：
md-code:

1

2

3

4

*   A list item with a blockquote:

    > This is a blockquote

    > inside a list item

效果：

- A list item with a blockquote:

This is a blockquoteinside a list item

如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 2 个制表符：

1

2

3

*   一列表项包含一个列表区块：

        <代码写在这>

效果：

- 一列表项包含一个列表区块：

```

```

当然，项目列表很可能会不小心产生，像是下面这样的写法：

1

1986. What a great season.

结果:

- What a great season.

换句话说，也就是在行首出现数字-句点-空白，要避免这样的状况，你可以在句点前面加上反斜杠。

1

1986\. What a great season.

      
    

    

    
    
    

    
      

        

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
