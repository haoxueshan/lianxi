import web
from urllib import parse
import time
urls = (
    "/", "html",
    "/hello", "hello",
    "/world", "world",
    "/haha", "haha",
    "/zhiji","zhiji"
)
app = web.application(urls, globals())
render = web.template.render('templates')
class html:
    def GET(self):
        d='./姓名和留言.txt'
        f=open(d,'r')
        s=f.read()
        return render.index(s)
class zhiji:
    def GET(self):
        render = web.template.render('./')
        d='./信息.txt'
        f=open(d,'r') 
        s=f.read()
        f.close
        return render.zhiji(s)
class hello:
#    def GET(self):
#       h='./index.html'
#       p=open(h,'rb')
#       j=p.read()
#       return j
    def GET(self):
        render = web.template.render('./')
        return render.index("")

class haha:
    def POST(self):
        j=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        m=web.input()
        y=j+'姓名'+':'+m['xingming']+'\n'+'留言'+':'+m['liuyan']+'\n'+'<br>'
        f1=open('姓名和留言.txt','a+')
        f1.write(y)
        f1.close
        d='./姓名和留言.txt'
        f=open(d,'r',)
        s=f.read()
        return '<h1 style="text-align:center">已保存</h1>'+s

class world:
    def GET(self):
        d='./姓名和留言.txt'
        f=open(d,'r')
        s=f.read()
        return s


# class redirect:
#     def GET(self, path):
#         web.seeother('/' + path)
#     def POST(self, path):
#         web.seeother('/' + path)
#         #web.template.render(self)
if __name__ == "__main__":
    app.run()
