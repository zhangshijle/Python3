#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie
import  time
import  sys

class Class1(object):  #初始化武松/西门庆/武大的共有属性
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
        time.sleep(0.5)
        print("\033[33;1m 初始化人物基本信息\033[1m".center(120,"#"))
        time.sleep(0.5)
        print("姓名:%s,性别:%s,年龄:%s,\n江湖绰号:%s,主要兵器:%s,生命值:%s,职业为:%s,性格为:%s" % (name,self.Gender,self.age,self.nickname,self.Weapon,self.Blood_values,self.Occupation,self.disposition))
        time.sleep(0.5)
        print("武功威力级别是:%s,家住地址:%s,电话号码是:%s" % (self.martial_level,address,phone))
        time.sleep(0.5)
        print("\033[31;1m人物%s的信息成功初始化完毕\033[1m" % name)
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)


    def def2(self,name,Blood_values,injure):  #获取剩余的生命值
        blood_values = self.Blood_values - injure
        return blood_values

    def def3(self,name,Blood_values):  #取当前的生命值
        print("%s的当前生命值为:%s" % (name,Blood_values))
        return Blood_values


    def talk(self,name,talk):
        print("%s说:%s" % (name,talk))


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
        time.sleep(0.5)
        print("\033[33;1m 初始化人物基本信息\033[1m".center(120,"#"))
        time.sleep(0.5)
        print("姓名:%s,性别:%s,住址:%s" % (name,self.Gender,self.address))
        time.sleep(0.5)
        print("职业:%s,性格:%s" % (self.Occupation,self.disposition))
        time.sleep(0.5)
        print("生命值为:%s,phone为:%s" % (self.Blood_values,self.phone))
        time.sleep(0.5)
        print("\033[31;1m人物%s的信息成功初始化完毕\033[1m" % name)
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)


    def def3(self,name,Blood_values,injure):  #获取剩余的生命值
        blood_values = self.Blood_values - injure
        return blood_values

    def def4(self,name,Blood_values):  #取当前的生命值
        print("%s的当前生命值为:%s" % (name,Blood_values))
        return Blood_values

class Class3(object):
    def __init__(self,name):
        self.name = name


    def talk(self,dialog):
        print("%s 说:%s" % (self.name,dialog))


def Wusong_wuda_ximenqing():
    '''
    #武松/武大/西门庆公有信息和自己的信息
    '''
    p1 = Class1("男",10,"行者","双刀",34,100,"都头","为人豪爽")
    p1.def1("武松","老家在清河县北七环环永定门外,杀死西门庆后后改住水泊梁山人民路与光明大街交叉口好汉小区31号楼1单元201房间下铺",18611100000)

    p1 = Class1("男",9,"西门大官人","金钱+权利",32,100,"黑帮老大","奸诈小人",)
    p1.def1("西门庆","清河县CMD核心商贸区高档别墅8888号楼",18611100001)

    p1 = Class1("男",3,"武大郎","炊饼",36,100,"小商贩","胆小怕事")
    p1.def1("武大","清河县北七环环永定门外无门牌号地下室",18611100004)


def Panjinlian_wangpo():
    '''
    #潘金莲公有信息和自己的信息
    '''
    p1 = Class2("女",18,"清河县北七环环永定门外无门牌号地下室","无业","嫌贫爱富",100,18611100002)
    p1.def2("潘金莲")

    p1 = Class2("女",53,"和潘金莲是隔墙邻居","媒婆","狼狈为奸",100,18611100003)
    p1.def2("王婆")


def story_background():
    '''
    本故事的背景介绍
    '''
    print("\n")
    print("\033[33;2m<<武松斗杀西门庆>>\033[2m".center(120,"#"))
    print("故事背景".center(100,"-"))
    print("\033[31;1m西门庆原是阳谷县的一个破落财主，后来开了一家生药铺，他为人奸诈，贪淫好色，使得些好枪棒，是个受人另眼看待的暴发户兼地头蛇\033[1m")
    time.sleep(1)
    print("\033[32;0m他路过武大屋檐下，潘金莲将叉帘子的叉竿失手，正好打在他头上，正要发作，见是个妖娆的妇女，却反而笑了，恋恋不舍地走开\033[0m")
    time.sleep(1)
    print("\033[33;1m他缠着开茶坊的王婆，既送钱又许物，定要王婆给他拉线。王婆定下裁缝寿衣计，使他得与潘金莲通奸，王婆家成了他们白昼幽会的场所\033[1m")
    time.sleep(1)
    print("\033[34;1m武大郎来捉奸，被他一脚踢成重伤，接着可怜的无被又被毒死。西门庆收买县吏，掩盖事实,此事竟无人敢问。待武松回来后弄清事实\033[1m")
    time.sleep(1)
    print("\033[35;1m亲手杀死潘金莲又来到狮子桥酒楼，找到西门庆，一场恶斗之后，终于把西门庆杀掉\033[1m\n")
    time.sleep(1.5)

def story_start():
    print("一日傍晚,武大卖烧饼回家,感觉有点口渴,要喝点酒,潘金莲赶紧到了一碗就端过来,殊不知,这碗酒中竟然........")
    time.sleep(1)
    print("酒中竟然被潘金莲放了致命毒药含笑半步癫,武大想起对潘金莲的一片苦心,竟然落到被下药,于是苦笑了一声,说道")
    wuda_panjinlian()

def wuda_panjinlian():
    '''
    武大的对白
    '''
    value = Class1("男",3,"武大郎","炊饼",36,100,"小商贩","胆小怕事") #武大的基础信息
    p1 = Class3("武大")
    p2 = Class3("潘金莲")
    p1.talk("这酒的味道不对,里面放了什么?")
    time.sleep(1)
    print("毒性开始发作,武大的生命值被减去10,剩于值为",value.def2("武大",0,10)) #武大的生命值减10
    time.sleep(1)
    p2.talk("是我放的含笑半步癫")
    time.sleep(1)
    p1.talk("啊? 是我把你从妓院里面把你赎身出来,把你接到我家里来,给你吃穿和住宿")
    time.sleep(1)
    p1.talk("你不感谢我也就罢了,竟然还要给我下毒?,太不够意思了")
    time.sleep(1)
    p2.talk("以前是我看错眼了,我根本不喜欢你,我现在喜欢上了西门大官人,是个高富帅,对我有好")
    time.sleep(1)
    p2.talk("而且对我百依百顺,还给我好多钱买衣服和化妆品,连淘宝账号和工资卡都给我了,你一年挣得钱也不如他几分钟的收入")
    time.sleep(1)
    p1.talk("真是气死我了.......")
    time.sleep(1)
    print("毒性第二次发作,武大的生命值被减去30,剩于值为",value.def2("武大",0,30)) #武大的生命值减30
    time.sleep(1)
    p1.talk("真是气死我了.......,你们不会有好结果的~")
    time.sleep(1)
    p1.talk("真是气死我了.......,你们不会有好结果的,你们会遭天打雷劈的~")
    time.sleep(1)
    p2.talk("后面的事情你就管不到了,安心去吧~")
    time.sleep(1)
    p1.talk("我还有8个烧饼没有卖出去.死不瞑目啊!")
    time.sleep(1)
    print("毒性第三次发作,武大的生命值被减去60,剩于值仅仅为",value.def2("武大",0,60)) #武大的生命值减60
    time.sleep(1)
    p2.talk("真是个屌丝,还不如在Alex那学pytho的人强")
    time.sleep(1)
    p2.talk("改天要有一个alex的电话号码,聊一聊!")
    time.sleep(1)
    p1.talk("你这个贱人,我还有最后一句话,我弟弟武松一定会给我报仇的...")
    time.sleep(1)
    print("武大就这样死了,于是潘金莲将这个消息告诉了王婆和潘金莲")
    time.sleep(1)
    print("最强的一次毒性发作,武大的生命值被减去100,剩于值为",value.def2("武大",0,100)) #武大的生命值减100


def wangpo_panjinlian_ximenqing():
    '''
    王婆和潘金莲与西门庆
    '''
    p1 = Class3("潘金莲")
    p2 = Class3("王婆")
    p3 = Class3("西门庆")
    print("\n\n")
    print("潘金莲,王婆,西门庆".center(100,"#"))
    time.sleep(1)
    p1.talk("王婆,西门公子,我已经把武大用药毒死了")
    time.sleep(1)
    p2.talk("恭喜西门大官人!")
    time.sleep(1)
    p3.talk("官府的事情我会给你们摆平!")
    time.sleep(1)
    p1.talk("武大说他弟弟叫武松,以后会给他报仇")
    time.sleep(1)
    p3.talk("不要害怕,这地方我说了算!")
    time.sleep(1)
    p3.talk("定要他有来无回!")
    time.sleep(1)
    p2.talk("大官人和金莲今晚就住我这把")
    time.sleep(1)
    p3.talk("好,你先出去吧")
    time.sleep(1)
    p1.talk("据说武松很厉害的,我们应该小心点才好~!")
    time.sleep(1)
    p3.talk("不用害怕,我的武功也很厉害的")
    time.sleep(1)
    p1.talk("大官人....")
    time.sleep(1)
    p3.talk("金莲....")
    time.sleep(1)
    print("\033[31;1m接下来的这段男女情节请自己想象!\033[1m")
    time.sleep(1)
    print("武松在景阳冈收到哥哥去世的Email,悲痛欲绝,随立即赶回老家,要查明哥哥去世的真相,潘金莲,西门庆和王婆听说武松还有10里路就到了,于是.....")
    p2.talk("大官人,武松就要到了,我们该如何使好啊?,老身今年五十多了,可怎么办啊?")
    time.sleep(1)
    p3.talk("胆小怕事的奴才,我要将他引到狮子楼.然后将他除掉")
    time.sleep(1)
    p2.talk("大官人威武!")
    time.sleep(1)
    p1.talk("大官人小心")
    time.sleep(1)
    p3.talk("王婆,你去告诉武松,就说武大是我杀的,我在狮子楼等他")
    time.sleep(1)
    p2.talk("我的天啊,老身不敢啊!")
    time.sleep(1)
    p3.talk("快去,不然让官府把你抓起来!")
    time.sleep(1)
    p2.talk("好吧")
    time.sleep(1)
    p1.talk("大官人此去小心,武松不是一般人等能对付得了的,据说刚打死了老虎")
    time.sleep(1)
    p3.talk("金莲放心,我去去就来!")
    time.sleep(1)


def wusong(): #武松的故事情节
    value = Class1("男",10,"行者","双刀",34,100,"都头","为人豪爽") #武松的装备和参数
    value2 = Class1("男",9,"西门大官人","金钱+权利",32,100,"黑帮老大","奸诈小人",) #西门庆的装备和参数
    value3 = Class2("女",53,"和潘金莲是隔墙邻居","媒婆","狼狈为奸",100,18611100003)
    value4 = Class2("女",18,"清河县北七环环永定门外无门牌号地下室","无业","嫌贫爱富",100,18611100002)
    print("\033[31;1m生命值默认为100,随着受到不同的伤害会不断减少,如果为0则表示人物死亡\033[1m")
    wusong_value = value.def3("武松",100) #武松集成到的生命值
    time.sleep(1)
    ximenqing_value = value2.def3("西门庆",100) #西门庆获取到的生命值
    time.sleep(1)
    wangpo_value = value3.def4("王婆",100)
    time.sleep(1)
    panjinlian_value = value3.def4("潘金莲",100)
    time.sleep(1)

    p1 = Class3("武松")
    p2 = Class3("潘金莲")
    p3 = Class3("王婆")
    p4 = Class3("西门庆")
    p1.talk("乡亲们都说潘金莲/王婆和西门庆还死我大哥,此愁不报誓不为人,刚王婆托人告诉我西门庆在狮子楼等我过去,分明是设下圈套等我过去,哼~!")
    time.sleep(1)
    p1.talk("我临时改变计划,先回家解决了贱人和王婆,在找西门庆算账,对! 就这么干")
    time.sleep(1)
    print("于是武松大步向家里走去!")
    time.sleep(1)
    print("武松走到家里看到潘金莲在屋子里和王婆说话,心想来的正好,待我解决了你们,在杀死西门庆,哼!,于是问潘金莲?")
    time.sleep(1)
    p1.talk("你们为什么要害死我哥哥?")
    time.sleep(1)
    p2.talk("数数,不是我做的,是王婆和西门官人害死的!")
    time.sleep(1)
    p3.talk("你不要乱栽赃啊,我给你们提供免费的偷换地点还这么说我!")
    time.sleep(1)
    p1.talk("贱人,害死我哥哥,杀人偿命,拿命来!")
    time.sleep(1)
    print("正在气头上的武松要取王婆和潘金莲的姓名,但是没有带自己的双刀和其他工具,他左右看了一下,发现一把菜刀,一把自带的短刀和一根木棒")
    time.sleep(1)
    choose_tools = input("\033[31;1m请选择武松要使用的工具,1/菜刀, 2/短刀 3/木棒:\033[1m")
    time.sleep(1)

    while True:
        if  choose_tools == "1":
            print("\033[31;1m兵器介绍: 菜刀的杀伤力为50,需要两刀才能杀死一个人\033[1m")
            time.sleep(1)
            p1.talk("我非常生气,我要用菜刀先杀死你们,因为一切祸因你而起,于是武松用菜刀砍了王婆和潘金莲一刀")
            time.sleep(1)
            print("潘金莲被砍了一刀.生命值减50,王婆被刺了一刀,生命值减50")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",100-50)
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",100-50)
            time.sleep(1)
            p1.talk("你们俩居然还都没有死,再给你们来一刀")
            time.sleep(1)
            print("潘金莲被砍了一刀.生命值减50,王婆被刺了一刀,生命值减50")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",wangpo_value-50) #用剩余的生命值减去当前损失的生命值
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",panjinlian_value-50)
            time.sleep(1)
            print("王婆和潘金莲分别挨了两菜刀而死")
            time.sleep(1)
            ximenqing()
            break
        elif choose_tools == "2": #选择的兵器为木棍
            print("\033[31;1m兵器介绍: 短刀为致命武器,一刀即使人毙命\033[1m")
            time.sleep(1)
            p1.talk("我非常生气,我要用短刀杀死你们!")
            time.sleep(1)
            print("武松用短刀分别刺了潘金莲和王婆每人一刀,这是致命的一刀")
            time.sleep(1)
            print("潘金莲被刺了一刀.生命值减100,王婆被刺了一刀,生命值减100")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",100-100)
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",100-100)
            time.sleep(1)
            print("潘金莲和王婆每人挨了一刀而死")
            time.sleep(1)
            ximenqing()
            break
        elif choose_tools == "3":
            print("\033[31;1m兵器介绍: 木棍的杀伤力为25,需要4棍才能打死一个人\033[1m")
            time.sleep(1)
            p1.talk("我非常生气,我要用木棒你们,于是武松用木棒打了王婆和潘金莲一棒,但是只把他们打成轻伤")
            time.sleep(1)
            print("潘金莲被打了一棍.生命值减25,王婆被刺了一棍,生命值减25")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",100-25) #总是生命值减去受伤的值,得到当前的生命值
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",100-25) #总是生命值减去受伤的值,得到当前的生命值
            time.sleep(1)
            print("武松见他们是轻伤,随后又打了他们每人一棒")
            time.sleep(1)
            print("潘金莲被打了一棍.生命值减25,王婆被刺了一棍,生命值减25")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",wangpo_value-25)
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",panjinlian_value-25)
            time.sleep(1)
            print("武松见他们伤势不是很严重,于是又打了他们一棍")
            time.sleep(1)
            print("潘金莲被打了一棍.生命值减25,王婆被刺了一棍,生命值减25")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",wangpo_value-25)
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",panjinlian_value-25)
            time.sleep(1)
            print("武松见他们已经成了重伤,于是打出了致命的一棍")
            time.sleep(1)
            print("潘金莲被打了一棍.生命值减25,王婆被刺了一棍,生命值减25")
            time.sleep(1)
            wangpo_value = value3.def4("王婆",wangpo_value-25)
            time.sleep(1)
            panjinlian_value = value3.def4("潘金莲",panjinlian_value-25)
            time.sleep(1)
            print("王婆和潘金莲分别挨了4棍而死")
            time.sleep(1)
            ximenqing()
            break

def ximenqing(): #西门庆的场景
    value = Class1("男",10,"行者","双刀",34,100,"都头","为人豪爽") #武松的装备和参数
    value2 = Class1("男",9,"西门大官人","金钱+权利",32,100,"黑帮老大","奸诈小人",) #西门庆的装备和参数
    print("\033[31;1m生命值默认为100,随着受到不同的伤害会不断减少,如果为0则表示人物死亡\033[1m")
    wusong_value = value.def3("武松",100) #武松集成到的生命值
    time.sleep(1)
    ximenqing_value = value2.def3("西门庆",100) #西门庆获取到的生命值
    time.sleep(1)
    p1 = Class3("武松")
    p2 = Class3("西门庆")

    p1 = Class3("武松")
    time.sleep(1)
    p2 = Class3("西门庆")
    time.sleep(1)
    print("\033[31;1m武松杀死了潘金莲和王婆后,继续想狮子楼走去,要去杀死西门庆为哥报仇")
    time.sleep(1)
    print("武松报仇心切,一会就走到了狮子楼,只见.......\033[1m")
    time.sleep(1)
    print("只见西门庆站在门口等着武松来..")
    time.sleep(1)
    p1.talk("为什么害死我哥哥?")
    time.sleep(1)
    p1.talk("我要为哥哥报仇!")
    time.sleep(1)
    p2.talk("废话少说,我今天要杀了你,然后我金莲在一起")
    time.sleep(1)
    p1.talk("那个贱人已经被我插死了,人头在此")
    time.sleep(1)
    p1.talk("王婆也被我杀死了")
    time.sleep(1)
    p1.talk("现在我就杀死你,你们去阴曹地府团聚吧")
    time.sleep(1)
    p2.talk("啊? 我的金莲,武松,你拿命来~~")
    time.sleep(1)
    p1.talk("西门庆,拿命来~~~")
    time.sleep(1)
    print("\033[31;1m人选选择兵器\033[1m".center(120,"#"))
    time.sleep(1)
    wusong_tools = 0  #武松选择的兵器标记
    choose_tools_wusong = input("\033[31;1m请选择武松要使用的工具,1/双刀, 2/单刀 :\033[1m")
    while True:
        if choose_tools_wusong == "1":
            print("武松选择了双刀")
            wusong_tools = 1
            print("\033[31;1m兵器介绍: 双刀刀的杀伤力为50,两刀即使人毙命\033[1m")
            break
        elif choose_tools_wusong == "2":
            print("武松选择了单刀")
            wusong_tools = 2
            print("\033[31;1m兵器介绍: 单刀的杀伤力为40,三刀即使人毙命\033[1m")
            break
        else:
            print("输入错误,没有此兵器,重新初始化游戏和兵器,请重新选择")
            ximenqing()
            break
    print("成功保存武松的兵器")
    time.sleep(1)
    choose_tools_ximenqing = input("\033[31;1m请选择西门庆要使用的工具,1/双刀, 2/单刀 :\033[1m")
    time.sleep(1)
    ximenqing_tools = 0
    while True:
        if choose_tools_ximenqing == "1":
            print("西门庆选择了双刀")
            ximenqing_tools = 1
            print("\033[31;1m兵器介绍: 双刀刀的杀伤力为50,两刀即使人毙命\033[1m")
            time.sleep(1)
            break
        elif choose_tools_ximenqing == "2":
            print("西门庆选择了单刀")
            ximenqing_tools = 2
            print("\033[31;1m兵器介绍: 单刀的杀伤力为40,三刀即使人毙命\033[1m")
            time.sleep(1)
            break

        else:
            print("输入错误,没有此兵器,重新初始化游戏和兵器,请重新选择")
            time.sleep(1)
            ximenqing()
            break
    print("成功保存保存西门庆的兵器")
    if wusong_tools == 1:  #加入武松的兵器是单刀
        if ximenqing_tools == 1:
            print("武松用双刀和西门庆的双刀从早上打到晚上")
            time.sleep(1)
            print("后来西门庆被武松用双刀砍了一刀,西门庆的生命值被减去50")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",100-50)
            time.sleep(1)
            print("武松用双刀砍了西门庆一刀,西门庆的生命值又被减去50")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-50)
            time.sleep(1)
            print("武松用双刀砍死了西门庆")
            time.sleep(1)
            end()
        else:
            print("武松用双刀和西门庆的单刀从早上打到晚上")
            time.sleep(1)
            print("后来西门庆被武松用双刀砍了一刀,西门庆的生命值被减去50")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",100-50)
            time.sleep(1)
            print("武松用双刀砍了西门庆一刀,西门庆的生命值又被减去50")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-50)
            time.sleep(1)
            print("武松用双刀砍死了西门庆")
            time.sleep(1)
            end()
    if wusong_tools == 2:
        if ximenqing_tools == 1:
            print("武松用单刀和西门庆的双刀从早上打到晚上")
            time.sleep(1)
            print("后来西门庆被武松用单刀砍了一刀,西门庆的生命值被减去40")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",100-40)
            time.sleep(1)
            print("武松用单刀砍了西门庆一刀,西门庆的生命值又被减去40")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-40)
            time.sleep(1)
            print("最后关头,武松给了西门庆致命一刀,西门庆的生命值")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-40)
            time.sleep(1)
            print("西门庆被武松用单刀砍了三刀,其生命值已经欠费,西门庆就此而亡")
            end()
        else:
            print("武松用单刀和西门庆的单刀从早上打到晚上")
            time.sleep(1)
            print("后来西门庆被武松用单刀砍了一刀,西门庆的生命值被减去40")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",100-40)
            time.sleep(1)
            print("武松用单刀砍了西门庆一刀,西门庆的生命值又被减去40")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-40)
            time.sleep(1)
            print("最后关头,武松给了西门庆致命一刀,西门庆的生命值")
            time.sleep(1)
            ximenqing_value = value2.def3("西门庆",ximenqing_value-40)
            print("西门庆被武松用单刀砍了三刀,其生命值已经欠费,西门庆就此而亡")
            time.sleep(1)
            end()
def end():
    print("武松终于为哥哥报了仇")
    time.sleep(1)
    print("武松将家具送给了亲朋好友,决定去梁山")
    time.sleep(1)
    print("武松经过半个月的行走,终于到达了梁山,在门口,他见竟然到了 西XX....")
    time.sleep(1)
    print("\033[31;1m 故事未完待续!!.......\033[1m")

def user_login_func():  #登录函数
    login_num = 0
    for login_num in range(3): #3此循环,用户有三次机会输入密码
        user = "zhangshijie" #登录用户
        password = 123456 #登录密码
        login_user = input("请输入登录用户名:") #要求用户输入登录用户
        login_password = int(input("请输入登录密码:")) #要求用户输入登录密码
        if login_user == user and login_password == password:  #假如用户输入的用户和密码与设定好的是一样的
            print("\033[31;1m登录成功\033[1m".center(100,"-"))
            print("欢迎本游戏界面") #输出欢迎登录界面
            break #跳出本循环
        else:
            login_num += 1
            print("用户名密码或密码错误,请重新登录:") #如果密码不对,返回错误
            continue
    else:
        print("用户名密码输入次数达到3次或以上,请稍后重新登录:")
        sys.exit(1) #使用break退出本循环后依然会执行后面的循环,因此使用sys.exit()退出主程序,错误码为1

def run():
    Wusong_wuda_ximenqing()
    Panjinlian_wangpo()

def choose():
    choosenum =  input("\033[32;2m请选择故事菜单,1/再次查看精彩故事背景,然后进入游戏 2/跳过背景直接进开始故事:\033[1m")
    a = str(choosenum).isalnum()
    while True:
        if  a:
            if choosenum == "1":
                story_background()
                story_start()
                break
            elif choosenum == "2":
                story_start()
                break
            else:
                print("输入超出范围,请重新输入1/查看故事背景,然后进入游戏 2/跳过背景直接进开始故事")
                choose()
        else:
            print("第一次就输错了,真low,重新输吧!")
            choose()

if __name__ == "__main__":
    user_login_func()
    story_background()
    run()
    choose()
    wangpo_panjinlian_ximenqing()
    wusong()
    ximenqing()