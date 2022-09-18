from cProfile import label
from ctypes import c_int
from dataclasses import dataclass
from email import message
from email.mime import image
from re import T
import tkinter as tk
import random
import time
import tkinter.messagebox



data_point='psw_data.txt'#根目录位置

def show():
    key=int(entry_usr_pwd.get())
    data = open(data_point,'r')
    file=str(data.read())
    file2=''

    for y in file:
        n=ord(y)-key
        n=chr(n)
        file2=file2+n
    
    file2.replace('__', '\n')
    window_show_output.insert('insert',file2)

#def clean():
    #window_show_output.delete('1.0','end')

def code_append():
    window_show_output.delete('1.0','end')
    key=int(entry_usr_pwd.get())
    a=1
    while a >0:
        netname1=str(input('请输入域名/软件描述:'))
        username1=str(input('请输入账号名:'))
        password1=input('请输入密码:')
        a=a-1
    
    #对密码进行加密
    password2=''
    for s in (password1+'\n'):
        a=ord(s)
        b=a+key
        password2=password2+chr(b)


    #对描述进行加密
    netname2=''
    for s in (netname1+'_'):
        a=ord(s)
        b=a+key
        netname2=netname2+chr(b)


    #对用户名进行加密
    username2=''
    for s in (username1+'_'):
        a=ord(s)
        b=a+key
        username2=username2+chr(b)
   


    #存储到文件里
    data = open(data_point,'a')
    data.write(str(netname2))
    data.write(str(username2))
    data.write(str(password2))
    data.write('\n') #此处是为了换行，其实应该有更好的方法，这里就是单纯为了简单

def code_append_ai():
    window_show_output.delete('1.0','end')
    key=int(entry_usr_pwd.get())
    x=1
    while x>0:
        netname1=str(input('请输入域名/软件描述:'))
        username1=str(input('请输入账号名:'))
        password0=random.sample('''AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890@#¥%''',12) #此处还有问题，下个版本应当支持自定义
        #列表转字符串
        password1=''
        for i in password0:
            password1=password1+str(i)
        print('请牢记您的密码'+password1)
        time.sleep(3)
        x=x-1
    
    
    
    #对密码进行加密
    password2=''
    for s in (password1+'\n'):
        a=ord(s)
        b=a+key
        password2=password2+chr(b)


    #对描述进行加密
    netname2=''
    for s in (netname1+'_'):
        a=ord(s)
        b=a+key
        netname2=netname2+chr(b)


    #对用户名进行加密
    username2=''
    for s in (username1+'_'):
        a=ord(s)
        b=a+key
        username2=username2+chr(b)
   


    #存储到文件里
    data = open(data_point,'a')
    data.write(str(netname2))
    data.write(str(username2))
    data.write(str(password2))
    data.write('\n') #此处是为了换行，其实应该有更好的方法，这里就是单纯为了简单

def readme():
    window_show_output.delete('1.0','end')
    text='''
以下是帮助手册
 GitHub链接：https://github.com/MRX-J0BS/Net_Code'
--如何确定主密钥--
在您第一次登录时，请在左侧的 ‘password’输入栏输入一个主密钥（这就是换位加密的关键值）
并且请您牢记此密码，一旦丢失那么您的所有密码将会无法复原（很难）

注：user name模块现在还没有正式调试完成，不用管

--关于安全性--
网络安全很重要！希望大家不要仅仅注意密码存储的是否安全，90%的密码都是被窃取的而非盗取（不过请相信我不会倒去您的密码，因为这个程序是完全不联网的）
我们的密码使用了凯撒算法加密，虽然一个加密软件公开自己的算法会很危险，但是我觉得您有这个知情权和选择的权利，以我目前的水平我认为凯撒加密还是很安全的，请大家放心
如果您实在过意不去，可以在github上看到我们开源的算法，并且自行修改

--作者自述--
我是一个初一的up，这是我自己凭借爱好和业余时间写的代码，可能会有很多bug，请您见谅
目前有很多有意思的功能正在开发中，如果您有好的建议也可以给我发邮件 3538501048@qq.com（记得注明您的来源和意图，我抽时间看到一定会回复）

        
感谢大家的支持
        '''

    window_show_output.insert('insert',text)







################################################################################################################


window = tk.Tk()
window.title('密码管理器GUI版')
window.geometry('686x471')

#canvas=tk.Canvas(window,height=580,width=580)
#main_image=tk.PhotoImage(file='??????????')
#main_image=canvas.create_image(0,0,anchor='nw',image=main_image)
#canvas.pack(side='top')

tk.messagebox.showerror(title='Hi', message='欢迎使用密码本 请仔细阅读使用说明') #欢迎

#设置一个名牌
logo=tk.Label(window,text='由MRX制作，GitHub链接：https://github.com/MRX-J0BS/Net_Code')
logo.pack(side=tk.BOTTOM)

tk.Label(window, text='User name: ').place(x=20, y= 30)
tk.Label(window, text='Password: ').place(x=20, y= 60)

var_usr_name = tk.StringVar()
var_usr_name.set('')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=140, y=30)
#entry_usr_name.pack()

var_usr_pwd = tk.StringVar()
var_usr_pwd.set('')
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=140, y=60)
#entry_usr_pwd.pack()

#var_usr_data = tk.StringVar()
#var_usr_data.set('')



#密钥输入界面
#window_input_key=tk.Entry(window,show='*',text='密钥')
#window_input_key.pack()


#总输出窗口
window_show_output=tk.Text(window,width=90)
window_show_output.place(x=20,y=100)

#读取所有密码的按钮
b=tk.Button(window,text='读取所有密码',command=show)
b.place(x=400,y=30)


#输入新密码的窗口
d=tk.Button(window,text='点我加入新密码',command=code_append)
d.place(x=550,y=30)

e=tk.Button(window,text='生成高强度密码',command=code_append_ai)
e.place(x=400,y=60)

#清空输出窗口的按钮
#c=tk.Button(window,text='清空',command=clean)
#c.pack()

f=tk.Button(window,text='使用手册',command=readme)
f.place(x=550,y=60)

window.mainloop()


