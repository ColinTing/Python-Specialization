# Python for Everybody Specialization

此源码为Coursera上“零基础入门专项课程”课后测试及视频练习题的Python实现。
科学的学习方法是通过不同场景下对知识应用达到对知识的掌握。
这里通过听课，自己的刻意练习及课后的小测验来实践科学的学习方法。


## Using Databases with Python课程中的结业测试成果

![image](https://github.com/ColinTing/Python-for-Everybody-Specialization/blob/master/ex_16_geo/myLocationHtmlScreenshot.png)

## Capstone: Retrieving, Processing, and Visualizing Data with Python课程中的Page Rank算法实践

### 豆瓣商业图书板块(https://book.douban.com/tag/%E5%95%86%E4%B8%9A) 经过我的小型pagerank算法排序后根据受欢迎度和声望两维度排名，前6名图书见图示


#### 在爬取了25个页面时图书排名顺序如下

![image](https://github.com/ColinTing/Python-for-Everybody-Specialization/blob/master/pagerank/douban/doubanBookPageRank.jpg)

#### 在爬取了100个页面时图书排名顺序如下

![image](https://github.com/ColinTing/Python-for-Everybody-Specialization/blob/master/pagerank/douban/doubanBookPageRank100.jpg)

两图相对照可以看出《穷查理宝典》异军突起，可谓是真正的好书，《决策与判断》与《影响力》也还算保住了先发优势，也值得一看。而在第二幅图中排名4、5、6的节点，排名第6的《邓普顿教你逆向投资》由于声望凸显，也可以优先拿来一看

PS:这里的爬取指把这个html页面内容都存储进了数据库而不仅仅是存储了一个网页地址


