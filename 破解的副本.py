#此文档用于尝试破解密码本
key=int(10) #括号里输入最大密钥尝试范围
def code_look(key):
    data = open('/Users/mrx/Desktop/Net_Code/data.txt','r')
    file=str(data.read())
    file2=''

    for y in file:
        n=ord(y)-key
        n=chr(n)
        file2=file2+n
    
    file2.replace('__', '\n')
    
    print(file2)


try_time=1
while try_time!=key:
    code_look(try_time)
    print('________此时密钥为'+str(try_time))
    try_time=try_time+1
    
print('进程已结束')

