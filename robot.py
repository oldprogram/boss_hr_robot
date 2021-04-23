#coding=utf-8
"""
This is part of the MSS Python's module.
Source: https://github.com/BoboTiG/python-mss
Simple naive benchmark to compare with:
    https://pythonprogramming.net/game-frames-open-cv-python-plays-gta-v/
"""
import time
import pyperclip

from math import sqrt
from pymouse import PyMouse
from pykeyboard import PyKeyboard

########################################
class Point:
    def __init__(self,x_init,y_init):
        self.x = x_init
        self.y = y_init

    def shift(self, x, y):
        self.x += x
        self.y += y

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])

def distance(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)



def drag(p1, p2, t = 0.05, r = 1):
    m.press(p1.x, p1.y, 1)

    x = p1.x
    y = p1.y
    step = 80


    while distance(Point(x, y), p2) >= 1 :
        x += (p2.x - x)/step
        y += (p2.y - y)/step
        step -= 1
        m.move(int(x), int(y))
        #print(Point(x,y))
        time.sleep(0.01)
    time.sleep(t)
    if r == 1:
        m.release(p2.x, p2.y, 1)

########################################
pos1 = Point(171,165)
pos2 = Point(943,235)
pos3 = Point(803,931)
pos4 = Point(1079,574)
pos5 = Point(1089,574)
#Point(468,169) Point(1453,261) Point(1504,997) Point(1850,561) Point(1620,621)
def get_key_pos():
    last_time = time.time()
    step = -1
    
    print("标定开始...")
    while 1<2:
        t = time.time() - last_time
        if  t > 5:
            last_time = time.time()
            if step == -1:
                print("请点击一次简历左上角的空白处,并保持不动")
                step = 0
            elif step == 0:
                pos1.x,pos1.y = m.position()
                print("请点击一次打招呼,并保持不动")
                step = 1
            elif step == 1:
                pos2.x,pos2.y = m.position()
                print("请点击一次文字输入框,并保持不动")
                step = 2
            elif step == 2:
                pos3.x,pos3.y = m.position()
                print("请点击一次关闭对话框,并保持不动")
                step = 3
            elif step == 3:
                pos4.x,pos4.y = m.position()
                print("请点击一次下一个(如果下一个右边有下拉滚动条，则放在下一个的右侧边缘，否则放在左侧边缘),并保持不动")
                step = 4
            elif step == 4:
                pos5.x,pos5.y = m.position()
                print(pos1,pos2,pos3,pos4,pos5)
                return


########################################
def people_filter():
    drag(Point(pos1.x,pos1.y),Point(pos1.x,1200),2,0)
    drag(Point(pos1.x,1200),Point(800,900),1)

    k.press_key(k.control_key)
    k.tap_key('c')
    time.sleep(1)
    k.release_key(k.control_key)

    m.move(1334, 461)      
    m.scroll(10)

    text = pyperclip.paste()
    ret = text.find("看过Ta的人还联系了")   #推荐信息给过滤掉
    if ret != -1:
        text = text[:ret]
        #print(text)

    #print("分析:",text)

    value = int(0)
    richness = text.count("\n") #根据多少行判断是否丰富
    print(">>> 候选人，人物画像: ")
    print("> 简历丰富度（多少行）：",richness)
    if richness > 35:
        print("> 简历:丰富")
        value = value + 5
    else:
        print("> 简历:不丰富")     

    if text.find("本科") != -1:
        print("> 本科:YES")
    else: 
        print("> 本科:NO")

    if text.find("单片机") != -1:
        value = value + 5 
        print("> 单片机:YES")
    else: 
        print("> 单片机:NO")

    if text.find("BLE") != -1 or text.find("ble") != -1 :
        value = value + 10 
        print("> BLE:YES")
    else: 
        print("> BLE:NO")

    if text.find("ESP") != -1 or text.find("esp") != -1 :
        value = value + 10 
        print("> ESP:YES")
    else: 
        print("> ESP:NO")

    if text.find("ZIGBEE") != -1 or text.find("zigbee") != -1 :
        value = value + 10 
        print("> ZIGBEE:YES")
    else: 
        print("> ZIGBEE:NO")

    if text.find("STM32") != -1 or text.find("stm32") != -1:
        value = value + 5 
        print("> STM32:YES")
    else: 
        print("> STM32:NO")

    if text.find("ARM") != -1 or text.find("arm") != -1:
        value = value + 3 
        print("> ARM:YES")
    else: 
        print("> ARM:NO")

    if text.find("keil") != -1:
        value = value + 2 
        print("> KEIL:YES")
    else: 
        print("> KEIL:NO")

    if text.find("蓝牙") != -1:
        value = value + 3 
        print("> 蓝牙:YES")
    else: 
        print("> 蓝牙:NO")

    if text.find("智能硬件") != -1:
        value = value + 2
        print("> 智能硬件:YES")
    else: 
        print("> 智能硬件:NO")

    if text.find("WIFI") != -1 or text.find("WiFi") != -1 or text.find("wifi") != -1 :
        value = value + 2 
        print("> WIFI:YES")
    else: 
        print("> WIFI:NO")

    if text.find("UART") != -1 or text.find("SPI") != -1 or text.find("II2") != -1 or text.find("PWM") != -1 :
        value = value + 2 
        print("> 外设:YES")
    else: 
        print("> 外设:NO")

    if text.find("RTOS") != -1 or text.find("rtos") != -1:
        value = value + 5 
        print("> RTOS:YES")
    else: 
        print("> RTOS:NO")

    if text.find("MCU") != -1 or text.find("mcu") != -1:
        value = value + 5 
        print("> MCU:YES")
    else: 
        print("> MCU:NO")

    if text.find("SOC") != -1 or text.find("soc") != -1:
        value = value + 3 
        print("> SOC:YES")
    else: 
        print("> SOC:NO")

    if text.find("linux") != -1:
        value = value + 2 
        print("> LINUX:YES")
    else: 
        print("> LINUX:NO")

    if text.find("硬件工程师") != -1 or text.find("硬件设计工程师") != -1 :
        value = 0
        print("> 硬件工程师:YES")
    else: 
        print("> 硬件工程师:NO <-- 不要")

    if text.find("21年应届生") != -1:
        value = 0
        print("> 21年应届生:YES <-- 不要")
    else: 
        print("> 21年应届生:NO")

    print("> 总分:", value)

    if value < 10:
        return 0
    else:
        return 1
########################################


m = PyMouse()
k = PyKeyboard()
def hr_start():
#   get_key_pos()

    last_time = time.time()
    step = -1
    while 1<2:
        t = time.time() - last_time
        if  t > 4:
            if step == -1:
                if people_filter() == 1:
                    step = 0
                else:
                    step = 4
            elif step == 0:
                m.click(pos2.x, pos2.y, 1)     
                step = 1
                print("沟通")
            elif step == 1:
                m.click(pos2.x, pos2.y, 1)      
                step = 2
                pyperclip.copy("您好, 方便发一下简历吗？")
                print("打开沟通对话框")
            elif step == 2:
                m.click(pos3.x, pos3.y , 1)     
                k.press_key(k.control_key)
                k.tap_key('v')
                time.sleep(1)
                k.release_key(k.control_key)
                k.tap_key(k.enter_key)
                step = 3
                print("输入一句话")
            elif step == 3:
                m.click(pos4.x, pos4.y, 1)      #取整除 - 向下取接近除数的整数
                step = 4
                print("关闭沟通")
            elif step == 4:
                #m.click(pos5.x, pos5.y, 1)
                #可以不用点击下一个，而用快捷按钮:CTRL+右
                #https://cloud.tencent.com/developer/article/1406355
                k.press_key(k.control_key)
                k.tap_key('Right')
                time.sleep(1)
                k.release_key(k.control_key)
                time.sleep(1)

                step = -1
                print("下一个")

            #print("time=",t)
            last_time = time.time()


hr_start()
