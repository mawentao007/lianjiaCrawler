scrapy crawl <spider name> -o file.csv -t csv    输出特定类型

scrapy startproject  projectName        创建新项目

***

xpath中用"//"开头的标记匹配任何符合的片段，而不带"//"的则匹配当前selector已经选定的内容中符合的片段。

***

关于输出类型，可以通过继承相应的exporter来进行相关配置，自己定义输出规则。本项目主要涉及feedExporter.py和settings.py两个文件。

***

一些python小技巧

+   删除字符串中某些内容，可以使用替换策略，将相应内容替换为" "。


