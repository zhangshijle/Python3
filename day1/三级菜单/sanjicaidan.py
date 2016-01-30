#!/usr/bin/env python
#-*- coding:utf-8 -*-

list1 = {"河北省":{"邯郸":['大名县','魏县','平安县','鸡泽县',' 峰峰矿区'],
                    "承德市":['承德县','双桥区','兴隆县','平泉县'],
                    },

            "山东省":{"济南市":['历下区','市中区','天桥区','历城区'],
                    "青岛市":['四方区','即墨市','胶州市','市东区'],
                   },

            "陕西省":{"西安市":['新城区','长安区','未央区','莲湖区'],
                    "咸阳市":['秦都区','永寿县','渭城区','三原县'],
                   },

            "辽宁省":{"沈阳市":['和平区','沈河区','铁西区','皇姑区','于洪区'],
                    "大连市":["中山区","西岗区","金州区","长梅县","旅顺口区"],
                    "鞍山市":["铁东区","铁西区","立山区","千山区","海城市"],
                    "抚顺市":["新抚区","顺城区","望花区","东洲区","东洲区"],},
            "内蒙古自治区":{"赤峰市":['红山区','元宝山区','松山区','宁城县','林西县'],
                            "通辽市":['科尔沁区','霍林郭勒市','开鲁县','科尔沁左翼中旗','科尔沁左翼后旗'],},
}

#k = list1.items()
#print k[2][0]

for i in range(3):  #三次循环，
    print "\033[31;1m---------------------开++始++查++询---------------------------\033[0m"
    shenglist = list1.keys()  #取出list1的键,就是三个省的名称,并赋值给shenglist
    SHENGNUM = range(len(shenglist))

    for shengname in shenglist: #循环省的列表,每次一个省名称
        shengnum= SHENGNUM[0]
        print "\033[31;1m%s. %s\033[0m" % (shengnum,shengname) #打印每次循环到的省的名称
        del SHENGNUM[0]
    print "\033[34;1m----------------------------------------------------\033[1m" #分割线,在省循环完成之后分割和下面的线条
    provincename = input("\033[31;31m请输如您要查看的省名数字:\033[0m")  #让用户输入要查看的省的名称,并赋值给provincename
    flag = False  #定义标志位用于之后跳出整个循环

    aaa = range(len(shenglist))  #统计有多少个省，会生成一个列表，[0,1,2,3,4].....
    if provincename in aaa:  #检查判断输入是否为正确的省名,如果在就执行下面的操作
        k = list1.keys()[provincename]  #获取到实际的省名称
        d = list1[k].values() #省的值

        while True:
            print"\033[34;1m-----------------你选择的%s包含的市为--------------------\033[0m" % (k)
            SHINUM = range(len(k))  #生成一个自动识别多少个省的列表，用于在省前面加0-x的数字显示
            #print SHINUM

            for shi in list1[k].keys(): #使用for循环遍历shilist,取出每一个市的名字
                shinum = SHINUM[0]  #对省进行显示编号，第一次为range省总长度的第一个值，range会生成和省数量一样的多一个数字列表
                #print shinum
                print "\033[34;1m-->>%s.%s\033[0m" % (shinum,shi)    #打印循环到的市列表
                del SHINUM[0] #循环完成第一次即删除列表的第一个元素，第二次的时候会把1赋值给第二个省元素，一次类推知道循环完成
            print "----------------------------------------------------"

            quitcmd = raw_input("\033[32;1m请问是否退出：A/a 坚决退出,B/b 返回上一层,Yes或其他键继续 ：\033[0m")
            QUITCMD = quitcmd.upper() #将用户的输入全部转换为大写
            if QUITCMD == "A":   #获取用户输入，并修改标志位为True
                flag = True #将标记标为True,用于后续if flag判断用户输入的是否为A
                print '您已经成功退出'
                break  #如果是A退出
            elif QUITCMD == "B": #假如用户输入的是B,则结束本次循环
                print "\033[31;1m您已经返回上一级\033[0m"
                break  #如果是B也退出
            else:
                shione = input("\033[33;1m请输入你要查看哪个市里面的县或市区的数字编号?：\033[0m")  #获取用户的输入的市区,稍后返回县
                xianshi = list1.values()[provincename].values()[shione] #求出谋省包含的区，到达三级菜单的最底层
                if shione in range(len(xianshi)): #如果输入的序号是在符合范围内
                    print "\033[33;1m-----------------您选择的编号%s包含的县为--------------------\033[0m" % (shione)   #打印一个横条,显示市的名称
                    XIANNUM  = range(len(xianshi))  #自动取出该市下的区或县的序号列表
                    for xian in xianshi: #循环打印县列表,获取每一个县
                        xiannum = XIANNUM[0] #为县生成序号编号
                        print "\033[33;1m-->> 本市的县/区有:\033[0m\033[31;1m%s.%s\033[0m" % (xiannum,xian) #传入县编号和县名称作为参数
                        del XIANNUM[0] #删除第一个序列变编号的值，
                    print "\033[32;1m<<<<##################您已经到达三级菜单的最低端###################>>>\033[3m"
                    print "\033[31;1m-----------------------------------------------------\033[0m"  #打印一条县的结束横线
                else: #如果用户输入的县不存在
                    print "\033[33;1m你输入的市名 %s 不存在请重新输入\033[0m" % (shione) #如果输入的编号不存在，返回不存在
                    continue

                quitcmd = raw_input("\033[32;1m请问是否退出：A/a 坚决退出、B/b 或任意键返回上一层：\033[0m")
                QUITCMD = quitcmd.upper() #将用户的输入全部转换为大写
                if QUITCMD == "A":   #获取用户输入，并修改标志位为True
                    flag = True #将标记标为True,用于后续if flag判断用户输入的是否为A
                    print '您已经成功退出'
                    break
                elif QUITCMD == "B": #假如用户输入的是B,则结束本次循环
                    print "\033[31;1m您已经返回上一级\033[0m"
                    continue
                else: #如果用户输入的既不是A也不是B,则退出本次循环返回上一级,和B的效果是一直的
                    print "\033[31;1m您已经返回上一级\033[0m"
                    continue
    if flag: #判断如果标志位为True，这里将执行下面的break操作退出整个循环
        break #退出本次整个for shengname in shenglist循环
    else: #假如if provincename in list1条件不成立,即用户输入的省份不对
        print "\033[31;1m 您输入的省名称 %s 是不存在的,请检查后重新输入名称\033[1m" % (provincename)  #提示输入的名称不正确

else:  #当输入的省名称不存在的时候
    print "\033[31;1m您输入的名称%s不在列表当中,请检查后重新输入\033[0m" % (provincename)
