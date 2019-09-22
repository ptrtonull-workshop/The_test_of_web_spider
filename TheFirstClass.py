# This is the first class of Web Spider.
# And I'm very glad to study this interest tech with all of yours.
# I recommand to learn about some HTML and regular expression.
# And I'm also a student. If this code have some problems, I'm very glad to hear your voice.
# 
# 这里是网络爬虫的第一课
# 我很高兴和你们一起学习这个有趣的技术
# 我个人建议在学习爬虫之前先去了解一下HTML与正则表达式的相关知识
# 我也只是一个学生，所以如果这个代码有任何的问题，我很高兴能听到你们的意见。
#  


# First of all, we need to know the creeper get the source from the HTML code.
# The code contains the IP of the source.
# So, the First step, we need to GET THE CODE from the Website.
#
# 首先，我们需要知道爬虫是从HTML代码中得到资源的。
# 代码中包含着资源的IP地址。
# 所以，第一步，我们需要得到这些代码。




import urllib
import urllib.request
#it's a individual module
import re

def geturl(url):
    url = urllib.request.urlopen(url)
    htmlcode = url.read()
    htmlcode = htmlcode.decode('utf-8')
    return htmlcode

def getsource(htmlcode):
    #regular expression
    #which means it can find out all the IP address which end with .jpg.
    reg = r'src="(.+?\.jpg)"'

    reg_img = re.compile(reg)
    imglist = reg_img.findall(htmlcode)

    for img in imglist:
        print (img)



if __name__ == "__main__":
    htmlcode = geturl('http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%8C%AB%E7%8C%AB')
    getsource(htmlcode)





