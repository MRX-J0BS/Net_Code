大家好，欢迎来到我的‘密码管理器’
以下是帮助手册



--如何正确使用--
1.用前准备：电脑要有python解释器，然后把密码管理器的python主文件单独存一个文件夹，里面再新建一个data.txt（这个文件还需要再源代码里绑定一下，具体看源代码’********‘的部分）

2.在第一次运行程序时，输入psw，回复一个1-50的数字，并且 牢记！！！！！ 主密钥忘了就完犊子了
  在每次重新（准确来讲进程关闭后又重新启动）运行程序时请再次输入psw（注意是一开始的那个，输入新的会出错哦）

--加密算法--
总共经历了两层加密
首先是凯撒加密，换位数字就是输入的psw
然后还会将凯撒加密后的密码二次顺序颠倒
（如果以后精力充足我会改进成进行多次加密的形式）先立个flag


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
