import requests
from lxml.html import etree
import tkinter
import numpy

# 每隔N（10-20）分钟查询校园网页是否更新关于奖学金的信息，若更新则在界面显示文章标题，否则继续查询
# 注意：对于不同网页需要获取不同的网页结构，该程序只针对特定页面
def getData():
    flag = True
    url = "http://***.***.edu.cn/"
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    etree_html = etree.HTML(html.text)
    for i in [1, 3, 5, 7, 9]:
        content = etree_html.xpath('//*[@id="xinwen2"]/div/ul[1]/li[' + str(i) + ']/a/text()')

        if "奖学金" in content[0]:
            flag = False
            info = content[0]
            break
        else:
            info = "No Scholarship Information, Continue..."

    lb.configure(text=info)
    if flag:
        num2 = numpy.random.randint(600, 1200, 1)
        timeInterval = int(num2 * 1000)
        root.after(timeInterval, getData)

root = tkinter.Tk()
root.title('Get Scholarship Information')
root.geometry('350x30')

lb = tkinter.Label(root, text='', fg='Red', font=("微软雅黑", 12))
lb.pack()
getData()
root.mainloop()
