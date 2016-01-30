#!/usr/bin/env python
#coding:utf-8
#author Zhang Shijie

d1 = {"手机":4598,"彩电":1580,"沙发":2250,"汽车":125000,"水杯":65,"衬衣":128,"Mac":12898}  #定义商品

shangpin = list(d1.keys())  #根据key取出商品的名称
jiage = list(d1.values())   #根据value 取出商品的价格
shangpin_num = range(len(shangpin)) #商品队列长度,即有多少商品
list1 = []  #已经购买的商品价格列表
list2 = []  #已经购买的商品名称列表
y_user_baitiao = 8000 #总白条额度
user_baitiao_y = 0 #设置一个可用白条额度,当用户有剩余额度时吧剩余额度赋值给user_baitiao_y
import  datetime #倒入时间模块,在保存购物车的时候增加瞬间戳

def user_shop_history():
    with open("history.txt","r") as f:
        history_data = f.readlines()
        for i in history_data:
            print(i)

def shangpin_select_func(): #让用户选择商品的函数
    num = 0
    print("".center(100,"#"))
    print("\033[31;1m商品编号 商品名称 商品价格\033[0m")
    for shangpin_list in shangpin:
        SHANGPIN_NUM = num
        print("%s       %s       %s" % (SHANGPIN_NUM,shangpin_list,d1[shangpin_list])) #自动匹配商品列表长度,并给商品加上商品编号
        num += 1
    print("\033[31;1m用户登录\033[1m".center(100,"-"))

def user_login_func():  #登录函数
    for login_num in range(3): #3此循环,用户有三次机会输入密码
        user = "zhangshijie" #登录用户
        password = 123456 #登录密码
        login_user = input("请输入登录用户名:") #要求用户输入登录用户
        login_password = int(input("请输入登录密码:")) #要求用户输入登录密码
        if login_user == user and login_password == password:  #假如用户输入的用户和密码与设定好的是一样的
            print("\033[31;1m欢迎登录\033[1m".center(100,"-"))
            print("欢迎登录购物商城") #输出欢迎登录界面
            break #跳出本循环
        else:
            print("用户名密码或密码错误,请重新登录") #如果密码不对,返回错误
    else:
        print("用户名密码输入次数达到3次或以上,请稍后重新登录")

def shop_input_func(): #获取用户选择商品的函数
    global gongzi
    print("\033[31;1m支出预算\033[1m".center(100,"-"))
    gongzi = int(input("输入你准备花多少钱购物:")) #自定义欲消费的金额,也可提前设置好
    flag = True #标记位
    while flag:
        print("\033[31;1m商品选购\033[1m".center(100,"-"))
        select  = input("请输入你要选购的商品:")  #默认获取到的是字串,要用int转换成数值,否则根据输入的数字取下标元素报错,"TypeError: list indices must be integers or slices, not str"
        #name = "%s" % (shangpin[select]) #以用户输入的数字为下标,取出该下标的物品名称
        danjia = ("%s"  % jiage[int(int(select))]) #获取商品单价
        danname= ("%s" % shangpin[int(select)])  #获取商品名称
        if danname in list2:
            print("您已经购买商品%s,请选择其他商品" % danname)
        elif int(select) > shangpin_num[-1] or danname in list2:  #如果输入的商品编号大于商品列表的最后一个值,则可以肯定商品不存在
            print("您选择的商品不存在或您已经购买商品%s,请重新选择" % danname)
        elif int(gongzi) < int(jiage[int(int(select))]): #假如用户剩余的钱比选择的商品价格少
            print("钱不够了,请选择其他商品,你还有的工资是%d元,购买此物品您还差%d元" % (gongzi,int(jiage[int(select)])-int(gongzi))) #输出钱不足了
            #flag = False
            user_baitiao() #调用user_baitiao函数
        elif int(gongzi) > int(jiage[int(select)]) and int(select) in shangpin_num: #如果用户的工资大于选择的商品切该商品存在
            danjia = ("%s"  % jiage[int(int(select))]) #获取商品单价
            danname= ("%s" % shangpin[int(select)])  #获取商品名称
            list1.append(danjia) #将单价保存在list1中
            list2.append(danname) #将商品名称保存在list2中
            #print(list1,"list1",list2,"list2")
            gongzi = gongzi - jiage[int(select)] #将用户现有的先减去购买商品的钱并赋值给用户自己
            print("您选择加到购物车的商品是%s,花了%d元,您还有%d元" % (danname,int(danjia),int(gongzi))) #输出用户购买的商品,花了多少钱,还有多少钱
        else:
            print("你选择的商品不存在,请重新选择") #其他输出显示商品不存在
        QUIT_NUM = input("请问您继续购物还是要退出结算? 输入Q/q退出,输入Y/y继续,输入C/c查询已加入到购物车到商品,输入E/e编辑购物车,输入V/v查看历史购物记录:") #让用户选择是继续,退出还说查询购买的商品或退出
        quit_num =  QUIT_NUM.lower() #将用户输入的转化为小写
        #print(quit_num)
        if quit_num == "q": #如果输入q
            #print("\033[31;退出登录\033[1m".center(100,"-"))
            user_logout_func() #调用user_logout_func函数
            break #跳出循环
        elif quit_num == "y": #如果是y就继续循环
            pass
        elif quit_num == "v":
            print("\033[31;1m历史纪录\033[1m".center(100,"-"))
            with open("history.txt","r") as f:
                user_shop_history()

        elif quit_num == "e": #如果用户输入e想编辑购物车
            print("\033[31;1m编辑购物\033[1m".center(100,"-"))
            user_edit_gouwuche() #调用user_edit_gouwuche函数
            break
        elif quit_num == "c": #如果用户输入c想查看当前购物车商品列表
            print("\033[31;1m查看购物\033[1m".center(100,"-"))
            #print("您现在选择的商品有",list2)
            c_logout_num = 0 #统计当前花了多少钱,先设置一个数为0
            #while True: #会导致按1推出后还在循环
            for c in list1: #循环list商品价格列表
                c_logout_num += int(c) #将每个元素和c_logout_num相加再赋值给c_logout_num
                #print(logout_num+int(i))
            print("您选购的商品有%s,当前共需要付款%s元,您的账户还有%s元!" % (list2,c_logout_num,gongzi)) #显示当前购买的商品,价格和账户于额
            while True:
                C_QUIT_NUM = input("请问您继续购物还是要退出结算? 输入Q/q退出,输入Y/y继续,输入C/c查询已加入到购物车到商品,输入E/e编辑购物车,输入V/v查看历史购物记录:")
                c_quit_num =  C_QUIT_NUM.lower() #抓换小写
                #print(c_quit_num)
                if c_quit_num == "q": #如果用户输入q要退出
                    user_logout_func()  #调用user_logout_func退出函数
                    break
                if c_quit_num == "v":
                    print("\033[31;0m历史纪录\033[0m".center(100,"-"))
                    user_shop_history() #调用查看历史购物记录函数
                    #continue
                if c_quit_num == "e":  #如果是e
                    print("\033[31;1m编辑购物\033[1m".center(100,"-"))
                    user_edit_gouwuche() #调用user_edit_gouwuche函数
                    break
        else:
            print("输入错误,请重新输入!")

def user_edit_gouwuche():  #编辑购物车函数
        #print("您当前购物车的商品有%s,价格为%s" % (list2,list1))
        user_edit_dict = dict(zip(list2,list1)) #当前已购买的商品字典列表
        print("您当前购物车的商品为",user_edit_dict) #打印当前购买的商品
        user_edit_Fangfa = input("请选择是要添加商品还是删除商品,A/a添加,D/d为删除,C/c退出结算:") #选择添加商品还是删除商品
        user_edit_fangfa = user_edit_Fangfa.lower()
        while True:
            if user_edit_fangfa == "d":
                print("\033[31;1m删除购物\033[1m".center(100,"-"))
                user_edit_del_select  = input("请输入你要删除的商品名称:")  #默认是字串,要用int转换成数值,否则根据输入的数字取下标元素报错,"TypeError: list indices must be integers or slices, not str"
                #name = "%s" % (shangpin[select]) #以用户输入的数字为下标,取出该下标的物品名称
                #print(user_edit_index)
                #global  list2
                #global  list1
                if user_edit_del_select in list2:
                    user_edit_index = list2.index(user_edit_del_select) #获取商品的index位置
                    del list2[user_edit_index] #根据索引位置删除商品的名称
                    del list1[user_edit_index] #根据索引位置删除索引的价格
                    del  user_edit_dict[user_edit_del_select] #删除已购买的字典列表中的商品和价格
                    import  time  #倒入时间模块
                    print("正在删除商品%s" % user_edit_del_select)  #输出正在删除商品
                    time.sleep(1)
                    print("正在删除商品%s" % user_edit_del_select)
                    time.sleep(1)
                    print("您已经成功删除了商品%s" % user_edit_del_select) #打印删除成功信息
                    print("您的当前购物车为%s" % user_edit_dict)
                    user_edit_Quit = input("请问是继续删除还是退出结算? 1/结算, 2/继续删除,3/返回上一级") #删除一个商品以后询问是结算还是继续删除商品
                    user_edit_quit = user_edit_Quit.lower() #将用户输入转换为小写
                    if user_edit_quit == "1": #假如用户输入1结算
                        user_logout_func() #调用阶段函数结算
                        break
                    elif user_edit_quit == "2": #假如用户输入的是2
                        continue
                    elif user_edit_quit == "3": #假如是3,调用退出函数
                        user_edit_gouwuche()
                        break
                else:
                    print("输入错误,请重新输入要删除的商品名称")
                    print("您当前的购物车有%s" % list2)
                    continue

            if  user_edit_fangfa == "a": #假如用户输入的是a
                print("\033[31;1m添加购物\033[1m".center(100,"-"))
                user_edit_add_select  = input("请输入你要添加的商品名称,此名称必须是存在商品列表当中并切您未曾购买过的商品:") #获取用户输入
                if  user_edit_add_select in shangpin: #假如用户输入的存在于商品名称列表
                    if  user_edit_add_select in list2: #假如商品存在列表后有存在于已购买商品列表
                        print("您购物车已经有此商品,请选择您未从购物商城添加到购物车的商品") #表示商品已经存在,让用户选购其他商品
                        print("您的购物车商品为%s " % list2)
                        print("当前商城商品有%s" % shangpin)
                    else:
                        list2.append(user_edit_add_select) #更新物品列表
                        list1.append(d1[user_edit_add_select]) #更新价格列表
                        user_edit_dict = dict(zip(list2,list1)) #更新已购买字典列表
                        #print(list2)
                        #print(list1,"list1")
                        #print(d1[user_edit_add_select])
                        import  time
                        print("正在添加商品%s" % user_edit_add_select) #输出这正在添加商品
                        time.sleep(1)
                        print("正在添加商品%s" % user_edit_add_select)
                        time.sleep(1)
                        print("您已经成功添加了商品%s" % user_edit_add_select) #打印删除成功信息
                        print("您的当前购物车为%s" % user_edit_dict) #购物车商品
                        user_edit_Quit = input("请问是继续添加还是退出结算? 1/结算, 2/继续添加,3/返回上一级") #添加一个商品后询问是继续添加还是结算
                        user_edit_quit = user_edit_Quit.lower() #将用户转换为小写
                        if user_edit_quit == "1": #假如用户输入1结算
                            user_logout_func() #调用阶段函数结算
                            break
                        elif user_edit_quit == "2": #假如用户输入的是2
                            continue
                        elif user_edit_quit == "3": #假如是3,调用退出函数
                            user_edit_gouwuche()
                            break
                        else:
                            print("您的输入的商品有误会已经存在购物车,请重新输入:")
                            continue
                else:
                    print("您输入的商品不存在,请重新输入~")

            if  user_edit_fangfa == "c": #假如用户输入的是c要退出结算
                user_logout_func()
                break

            else:
                print("输入错误,请输入A/a添加商品或D/d删除商品")
                print("您的购物车商品为%s " % list2)
                print("当前商城商品有%s" % shangpin)
                user_edit_gouwuche()
                break

def user_logout_func():  #用户退出函数
    print("\033[31;1m结算退出\033[0m".center(100,"-"))
    #print(list1)
    user_logout_now = datetime.datetime.now()
    logout_num = 0 #对用户采购的商品进行结算
    for i in list1: #循环用户保存的商品价格列表
        logout_num += int(i) #将列表相加并赋值给logout_num
        #print(logout_num+int(i))
    with open("history.txt","a+") as f: #以追加读写的方式打开用户购物记录文件,可用保存a+方式可以保留之前的购物记录,w会晴空之前的记录
        for i in list2: #循环用户购买到的商品
            f.write("您在%s购买的商品有%s\n" % (user_logout_now.strftime("%Y年%m月%日%H点%M分%S"),i))
            f.flush() #立即将内存的数据保存在硬盘
    print("\033[31;0m您本次购物一共花费%d元,够买到了%s,欢迎下次再来购物!\033[0m" % (logout_num,list2)) #输出用户本次的购物清单

def user_baitiao(): #用户白条函数
    Command = input("您的金额不足,是否需要使用白条额度?,Y立即使用,N继续购物或结账?") #让用户选择是否要使用白条
    command = Command.lower()
    global y_user_baitiao
    if command == "y":
        print("白条界面".center(100,"-"))
        user_baitiao_num = input("您总共有8000白条额度,当前额度为%s,您想使用多少?" % int(y_user_baitiao)) #或取当前的白条可用额度,可用额度等于总额度减去已经使用的额度
        if int(user_baitiao_num) <= int(y_user_baitiao): #假如用户输入的额度小雨等于可用额度
            global gongzi
            global user_baitiao_y #全局变量
            gongzi += int(user_baitiao_num)  #使用白条后的工资
            y_user_baitiao = y_user_baitiao - int(user_baitiao_num) #计算白条的剩余额度
            user_baitiao_y += int(user_baitiao_num)  #使用了多少白条额度
            #print(y_user_baitiao,"白条剩余额度")
            #print(user_baitiao_num,"累计用了多少额度")
            print("您现在的的工资为%s,您本次使用了%s元的白条额度,当前白条可用额度为%s,累计使用了白条额度为%s" % (gongzi,user_baitiao_num,y_user_baitiao,user_baitiao_y))
        else:
            print("超出白条范围了,请输入%s以内的数字" % (y_user_baitiao))
    else:
        pass

def run():
    shangpin_select_func()
    user_login_func()
    shop_input_func()


if __name__ == "__main__":
    run()