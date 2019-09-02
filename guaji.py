# _*_ coding: utf-8 _*_
try:
    import pyautogui
except ImportError :
    try:
        from pip import main
        main('pyautogui')
    except Exception as errInfo:
        print(errInfo)
import random,time,datetime

class guaji:
    mouseX=0
    mouseY=0
    maxLasTime=20
    maxTimes = 5
    opDef=['pressForward','pressRun','pressBack','pressBackContinu','turnLeft','turnRight','pressRandowNumKey'\
           ,'jump']

    def __init__(self):
        self.screenWidth, self.screenHeight = pyautogui.size()  # 屏幕尺寸
        pyautogui.moveTo(self.screenWidth/2, self.screenHeight/2) #鼠标移动到屏幕中央
        self.runLasTime=3600*10   #默认挂机时间10小时

    def getMousePosition(self):  #获取当前鼠标位置
        self.mouseX, self.mouseY = pyautogui.position()

    def getRunTap(self): #每次动作间隔随机1-20秒
        return int(random.randrange(1,self.maxLasTime))

    def pressForward(self):  #向前一步
        pyautogui.press('w')

    def pressRun(self): #持续向前跑,随机持续时间
        lasTime = random.randrange(1,self.maxLasTime)
        pyautogui.keyDown('w')
        time.sleep(lasTime)
        pyautogui.keyUp('w')

    def pressBack(self):
        pyautogui.press('s')

    def pressBackContinu(self):
        lasTime = random.randrange(1,self.maxLasTime)
        pyautogui.keyDown('s')
        time.sleep(lasTime)
        pyautogui.keyUp('s')

    def turnLeft(self):
        pyautogui.press('a')

    def turnRight(self):
        pyautogui.press('d')

    def pressRandowNumKey(self,maxNum=7):
        numKey = random.randrange(1,maxNum)
        pyautogui.press(str(numKey))

    def jump(self):   #跳,随机次数
        times = random.randrange(1, self.maxTimes)
        for x in range(times):
            pyautogui.press('escape')


if __name__ == '__main__':
    guaji=guaji()
    nowDateTime=datetime.datetime.now()
    endDateTime=nowDateTime+datetime.timedelta(seconds=guaji.runLasTime)
    while True:
        now = datetime.datetime.now()
        if now >= endDateTime: #判断当前时间是否到了结束时间以跳出循环
            break
        randomOp=random.randrange(0,len(guaji.opDef))
        operate=getattr(guaji,guaji.opDef[randomOp])
        operate()
        time.sleep(int(guaji.getRunTap()))
    pass
wds