#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  time

class Class1(object):  #初始化武松/西门庆的共有属性
    def __init__(self,Gender,martial_level,nickname,Weapon,age,Blood_values,Occupation,disposition): #self是实例本身,谁调用类,self就是谁
        self.Gender = Gender  #性别
        self.martial_level = martial_level #武功级别
        self.nickname = nickname #江湖外号
        self.Weapon = Weapon #个人武器
        self.age = age #年龄
        self.Blood_values = Blood_values #生命值
        self.Occupation = Occupation #职业
        self.disposition = disposition #性格

    def def1(self,name,address,phone=None):  #输出共有的基本信息,并定制个人信息
        print("\033[33;1m 初始化人物基本信息\033[1m".center(120,"#"))
        print("姓名:%s,性别:%s,年龄:%s,\n江湖绰号:%s,主要兵器:%s,生命值:%s,职业为:%s,性格为:%s" % (name,self.Gender,self.age,self.nickname,self.Weapon,self.Blood_values,self.Occupation,self.disposition))
        print("武功威力级别是:%s,家住地址:%s,电话号码是:%s" % (self.martial_level,address,phone))
        print("\033[31;1m人物%s的信息成功初始化完毕\033[1m" % name)
        print("\n")
        time.sleep(1)


class Class2(object): #初始化潘金莲/王婆的共有属性
    def __init__(self,Gender,age,address,Occupation,disposition,Blood_values,phone=None):
        self.Gender = Gender
        self.age = age
        self.address = address
        self.Occupation = Occupation
        self.disposition = disposition
        self.Blood_values = Blood_values
        self.phone = phone

    def def2(self,name):
        print("姓名:%s,性别:%s,住址:%s" % (name,self.Gender,self.address))
        print("职业:%s,性格:%s" % (self.Occupation,self.disposition))
        print("生命值为:%s,phone为:%s" % (self.Blood_values,self.phone))
        print("\033[31;1m人物%s的信息成功初始化完毕\033[1m" % name)
        print("\n")

    def talk(self,name,talk):
        print("%s说:%s" % (name,talk))


def Wusong():
    '''
    #武松公有信息和自己的信息
    '''
    p1 = Class1("男",10,"行者","双刀",34,100,"都头","为人豪爽")
    p1.def1("武松","老家在清河县北七环环永定门外,杀死西门庆后后改住水泊梁山人民路与光明大街交叉口浩瀚小区31号楼1单元201房间下铺")


def Wuda():
    '''
    #武大公有信息和自己的信息
    '''
    p1 = Class1("男",3,"武大郎","炊饼",36,100,"小商贩","胆小怕事")
    p1.def1("武大","清河县北七环环永定门外无门牌号地下室")


def Ximenqing():
    '''
    #西门庆公有信息和自己的信息
    '''
    p1 = Class1("男",9,"西门大官人","金钱+权利",32,100,"黑帮老大","奸诈小人",)
    p1.def1("西门庆","清河县CMD核心商贸区高档别墅8888号楼",18611100001)

def Panjinlian():
    '''
    #潘金莲公有信息和自己的信息
    '''
    p1 = Class2("女",18,"清河县北七环环永定门外无门牌号地下室","无业","嫌贫爱富",100,18611100002)
    p1.def2("潘金莲")


def Wangpo():
    '''
    #王婆公有信息和自己的信息
    '''
    p1 = Class2("女",53,"和潘金莲是隔墙邻居","媒婆","狼狈为奸",100,18611100003)
    p1.def2("王婆")


def story_background():
    '''
    本故事的背景介绍
    '''
    print("\033[31;1m西门庆原是阳谷县的一个破落财主，后来开了一家生药铺，他为人奸诈，贪淫好色，使得些好枪棒，是个受人另眼看待的暴发户兼地头蛇\033[1m")
    time.sleep(1.5)
    print("\033[32;0m他路过武大屋檐下，潘金莲将叉帘子的叉竿失手，正好打在他头上，正要发作，见是个妖娆的妇女，却反而笑了，恋恋不舍地走开\033[0m")
    time.sleep(1.5)
    print("\033[33;1m他缠着开茶坊的王婆，既送钱又许物，定要王婆给他拉线。王婆定下裁缝寿衣计，使他得与潘金莲通奸，王婆家成了他们白昼幽会的场所\033[1m")
    time.sleep(1.5)
    print("\033[34;1m武大郎来捉奸，被他一脚踢成重伤，接着可怜的无被又被毒死。西门庆收买县吏，掩盖事实,此事竟无人敢问。待武松回来后弄清事实\033[1m")
    time.sleep(1.5)
    print("\033[35;1m亲手杀死潘金莲又来到狮子桥酒楼，找到西门庆，一场恶斗之后，终于把西门庆杀掉\033[1m")
    time.sleep(2)

def story_start():
    print("一日傍晚,武大卖烧饼回家,感觉有点口渴,要喝点酒,潘金莲赶紧到了一碗就端过来,殊不知,这碗酒中竟然........")

def run():
    Wusong()
    Wuda()
    Ximenqing()
    Panjinlian()
    Wangpo()

if __name__ == "__main__":
    #story_background()
    choose =  input("\033[32;2m请选择故事菜单,1/查看故事背景,然后进入游戏 2/跳过背景直接进开始故事:\033[1m")
    while True:
        if  choose == "1":
            story_background()
            story_start()
            break
        elif choose == "2":
            story_start()
            break