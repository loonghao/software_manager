# -*- coding:utf8 -*-
import sys
from os.path import join as pathjoin
import time
from PySide import QtGui
import config


class SplashScreen(QtGui.QSplashScreen):
    def __init__(self):
        super(SplashScreen, self).__init__(QtGui.QPixmap(pathjoin(config.RESOURCES, "tray_icon.png")))  # 启动程序的图片

    # 效果 fade =1 淡入   fade= 2  淡出，  t sleep 时间 毫秒
    def effect(self):
        self.setWindowOpacity(0)
        t = 0
        while t <= 50:
            new_opacity = self.windowOpacity() + 0.02  # 设置淡入
            if new_opacity > 1:
                break

            self.setWindowOpacity(new_opacity)
            self.show()
            t -= 1
            time.sleep(0.04)

        time.sleep(1)
        t = 0
        while t <= 50:
            new_opacity = self.windowOpacity() - 0.02  # 设置淡出
            if new_opacity < 0:
                break

            self.setWindowOpacity(new_opacity)
            t += 1
            time.sleep(0.04)