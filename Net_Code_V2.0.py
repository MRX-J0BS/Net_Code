import random
import time

def code_append(key):
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
    data = open('*********此处请放data.txt绝对路径，记得加上单引号**********','a')
    data.write(str(netname2))
    data.write(str(username2))
    data.write(str(password2))
    data.write('\n') #此处是为了换行，其实应该有更好的方法，这里就是单纯为了简单




def code_look(key):
    data = open('*********此处请放data.txt绝对路径，记得加上单引号**********','r')
    file=str(data.read())
    file2=''

    for y in file:
        n=ord(y)-key
        n=chr(n)
        file2=file2+n
    
    file2.replace('__', '\n')
    print(file2)




def code_append_ai(key):
    x=1
    while x>0:
        netname1=str(input('请输入域名/软件描述:'))
        username1=str(input('请输入账号名:'))
        password0=random.sample('''qwertyuiop[]/asdfghjkl;'zxcvbnm,./1234567890-=!@#$%^&*''',12) #这里是高强度密码可能出现的内容，可以自由更改
        #print(password0)
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
    data = open('*********此处请放data.txt绝对路径，记得加上单引号**********','a')
    data.write(str(netname2))
    data.write(str(username2))
    data.write(str(password2))
    data.write('\n') #此处是为了换行，其实应该有更好的方法，这里就是单纯为了简单

    
        
print('''
欢迎使用密码管理器 v2.0 MRX
回复数字获取对应内容（请先确定主密钥）
1.加入一个密码
2.读取所有的密码
3.生成一个高安全度的密码并存储
————————————————————后续功能正在开发————————————————————
x.帮助
y.开发者名单
''')
cheak=str(input('请输入：'))
while cheak != 'q':
    if cheak=='1':
        try:
            code_append(psw)
            print('Finish')
        except:
            print('出错！')
    elif cheak=='2':
        code_look(psw)
    elif cheak=='psw':
        psw=int(input('psw?'))
    elif cheak=='3':
        code_append_ai(psw)
    elif cheak=='x':
        print('''
        此处内容可能不完整，请看github里的readme
        https://github.com/MRX-J0BS/-
        
        
        以下是帮助手册
        --如何确定主密钥--
        在第一次运行程序时，输入psw，回复一个1-50的数字，并且 牢记！！！！！ 主密钥忘了就完犊子了
        在每次重新（准确来讲进程关闭后又重新启动）运行程序时请再次输入psw（注意是一开始的那个，输入新的会出错哦）

        --我的自述--
        我是一个初一的up，这是我自己凭借爱好和业余时间写的代码，可能会有很多bug，请您见谅
        目前有很多有意思的功能正在开发中，如果您有好的建议也可以给我发邮件 3538501048@qq.com（记得注明您的来源和意图，我抽时间看到一定会回复）
        如果有大佬想要看我的源代码也可以私信我

        --关于安全性--
        网络安全很重要！希望大家不要仅仅注意密码存储的是否安全，90%的密码都是被窃取的而非盗取（不过请相信我不会倒去您的密码，因为这个程序是完全不联网的）
        我们的密码使用了凯撒算法加密，虽然一个加密软件公开自己的算法会很危险，但是我觉得您有这个知情权和选择的权利，以我目前的水平我认为凯撒加密还是很安全的，请大家放心
        如果您实在过意不去可以私信我要源文件，改成您自己的算法

        --总结--
        可能以后学业繁重我单独完成作品的时间越来越少了，但我会保持好奇心,永远记得python带给我的快乐，永远记得第一次运行程序的喜悦，永远记得第一个支持者的赞赏。一直前进下去，也感谢大家的支持！
        
        我会永远记得你们！
        
        ''')
    elif cheak=='y':
        print('''
        ---制作者名单---
        MRX.jobs -3538501048@qq.com
        ''')
    else:
        print('不再范围内，请检查您输入的是否正确')
    time.sleep(1)
    
    print('''
欢迎使用密码管理器 v2.0 MRX
回复数字获取对应内容（请先确定主密钥）
1.加入一个密码
2.读取所有的密码
3.生成一个高安全度的密码并存储
————————————————————后续功能正在开发————————————————————
x.帮助
y.开发者名单
''')
    cheak=str(input('请输入'))





print('程序已结束,see you soon')

