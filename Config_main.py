#! usr/bin/python
# coding=utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import logging
import time
import serial.tools.list_ports
import binascii

# from pyqtUI.Config_main_ui1 import Ui_Dialog
from pyqtUI.main import Ui_MainWindow
from INF_HELPER import inf_helper
from my_serial import SerialHelper


class mywindow(QMainWindow , Ui_MainWindow):
    def __init__(self,qApp):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.qApp=qApp

        icon = QIcon()
        import os
        path = os.getcwd()
        icon.addPixmap(QPixmap("%s/app.ico"%path),QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        import pyqtcss.white_blue
        self.setStyleSheet(pyqtcss.white_blue.load_stylesheet_pyqt5())#加载css格式

        # self.StyleInit()
        # self.IconInit()

        self.UpdateSerialShow()
        self.pushButton_UpdateSerialShow.clicked.connect(self.UpdateSerialShow)
        self.pushButton_OpenSerial.clicked.connect(self.OpenCloserSer)
        self.pushButton_InfReadInformation.clicked.connect(self.InfStartReadInformation)
        self.pushButton_InfWriteInformation.clicked.connect(self.InfStartWriteInformation)
        self.pushButton_Style.clicked.connect(self.Inf_ParameterFormat)
        self.progressBarInfRead.setRange(0, 6)
        self.progressBarInfWrite.setRange(0,6)

        self.Inf = inf_helper()

        self.timerWork = QTimer()
        self.timerWork.timeout.connect(self.Thread_InfWork)

        self.timer_read = QTimer()
        self.timer_read.timeout.connect(self.SerialRead)


        '''红外工作线程打开，用于红外配置和读取个人剂量仪'''
        self.Inf_isRead = False
        self.Inf_isWrite = False
        self.Inf_WriteCmdList = {
            'Answer':'000100',
            'IntervalTimeCumulativeDose': '080100',
            'CumulativeDoseReset': '000900',
            'MaximumDoseRate': '080300',
            'InstrumentNumber': '000500',
            'SuperRangeIdentification': '080500',
            'Counter': '080600',
            'DoseThreshold': '000200',
            'DoseRateThreshold': '000300',
            'CalibrationFactor': '080900',
            'InstrumentDate': '000B00',
            'IntervalTime': '000400',
            }
        self.Inf_ReadCmdList = {
            'IntervalTimeCumulativeDose': '080100',
            'CumulativeDose': '080200',
            'MaximumDoseRate': '080300',
            'InstrumentNumber': '080400',
            'SuperRangeIdentification': '080500',
            'Counter': '080600',
            'DoseThreshold': '080700',
            'DoseRateThreshold': '080800',
            'CalibrationFactor': '080900',
            'InstrumentDate': '080A00',
            'IntervalTime': '080B00',
            'TunnelBigRead':'080C00',
            'TunnelSmallRead': '080C01',}
        self.lineEdit_W = [
            self.lineEdit_W_InstrumentNumber,
            self.lineEdit_W_UserNumber,
            self.lineEdit_W_InstrumentDate,
            self.lineEdit_W_IntervalTime,
            self.lineEdit_W_DoseThreshold,
            self.lineEdit_W_DoseRateThreshold
        ]
        self.lineEdit_R = [
            self.lineEdit_R_InstrumentNumber,
            self.lineEdit_R_UserNumber,
            self.lineEdit_R_InstrumentDate,
            self.lineEdit_R_IntervalTime,
            self.lineEdit_R_DoseThreshold,
            self.lineEdit_R_DoseRateThreshold,
            self.lineEdit_R_MaximumDoseRate,
            self.lineEdit_R_MaximumDoseRateTime,
            self.lineEdit_R_CumulativeDose
        ]
        self.Inf_Str = ""
        'xxxxxxxxxxxxxxxxxx 0 start 1 len  2 epdnum   3usernum  4ntnum 5cpunum 6equ 7cmd cld 8d   9 crc 10end'
        self.Inf_CmdList = ['AA55','0000','00000000','00000000','0000','0000','00','000000','00','0000','BB66']
#----------------------------自定义界面---------------------------------------#
    def IconInit(self):
        import qtawesome as qta
        btnMenu_Close_icon = qta.icon('fa.minus', color='white',)
        self.btnMenu_Min.setIcon(btnMenu_Close_icon)
        btnMenu_Max_icon = qta.icon('fa.square-o', color='white',)
        self.btnMenu_Max.setIcon(btnMenu_Max_icon)
        btnMenu_Close_icon = qta.icon('fa.close', color='white',)
        self.btnMenu_Close.setIcon(btnMenu_Close_icon)

        from six import unichr
        self.lab_Ico.setText(unichr(0xF26C))
        self.lab_Ico.setFont(qta.font('fa', 16))

    def StyleInit(self):
        self.setMinimumHeight(400)
        self.setMinimumWidth(300)
        self.btnMenu_Close.clicked.connect(self.on_btnMenu_Close_clicked)
        self.btnMenu_Max.clicked.connect(self.on_btnMenu_Max_clicked)
        self.btnMenu_Min.clicked.connect(self.on_btnMenu_Min_clicked)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinMaxButtonsHint)
        self.location = self.geometry()
        #设置鼠标可以跟踪
        self.setMouseTracking(True)

        self.max = False
        self.mousePressed = False

        self.mousePoint = QPoint()
        self.mouseGloPoint = QPoint()

        self.LEFTSPACE = 3
        self.RIGHTSPACE = 3
        self.BOTTOMSPCAE = 3

        self.leftPress = False
        self.rightPress = False
        self.bottomPress = False

        #安装事件监听器,让标题栏识别鼠标双击
        self.lab_Title.installEventFilter(self)

    def eventFilter(self,obj ,event):
        '''事件过滤器响应，控件必须先安装，才能响应'''
        if obj == self.lab_Title:
            if event.type() == QEvent.MouseButtonDblClick:
                self.on_btnMenu_Max_clicked()
                return True
            if event.type() == QEvent.MouseMove:
                self.move(event.globalPos() - self.mousePoint)
                event.accept()
                return True
        return QDialog.eventFilter(self,obj,event)

    def mouseMoveEvent(self, e):
        gloPoint = e.globalPos()
        pos = e.pos()
        xPos = pos.x()
        yPos = pos.y()

        if not self.mousePressed:
            self.setCursor(Qt.ArrowCursor)
            if xPos >= 0 and xPos < self.LEFTSPACE:#左边界
                self.setCursor(Qt.SizeHorCursor)
            if xPos > (self.width() - self.RIGHTSPACE):#右边界
                self.setCursor(Qt.SizeHorCursor)
            if yPos > (self.height() - self.BOTTOMSPCAE):#下边界
                self.setCursor(Qt.SizeVerCursor)
            if xPos >=0 and xPos < self.LEFTSPACE and yPos >(self.height()-self.RIGHTSPACE):#左下
                self.setCursor(Qt.SizeBDiagCursor)
            if xPos > (self.width() - self.RIGHTSPACE) and yPos > (self.height() - self.BOTTOMSPCAE):#右下
                self.setCursor(Qt.SizeFDiagCursor)
        else:
            if self.leftPress and not self.bottomPress:
                self.setCursor(Qt.SizeHorCursor)
                tr = self.rMove.topRight()
                if gloPoint.x()< tr.x() - self.minimumWidth():
                    self.rMove.setLeft(gloPoint.x())
                    self.setGeometry(self.rMove)
                return
            if self.rightPress and not self.bottomPress:
                self.setCursor(Qt.SizeHorCursor)
                tl = self.rMove.topLeft()
                if gloPoint.x()> tl.x() + self.minimumWidth():
                    self.rMove.setRight(gloPoint.x())
                    self.setGeometry(self.rMove)
                return
            if self.bottomPress and not self.leftPress and not self.rightPress:
                self.setCursor(Qt.SizeVerCursor)
                bl = self.rMove.bottomLeft()
                if gloPoint.y()> bl.y() - self.minimumHeight():
                    self.rMove.setBottom(gloPoint.y())
                    self.setGeometry(self.rMove)
                return
            if self.leftPress and self.bottomPress:
                tr = self.rMove.topRight()
                bl = self.rMove.bottomLeft()
                self.setCursor(Qt.SizeBDiagCursor)
                if gloPoint.x()< tr.x() - self.minimumWidth() and gloPoint.y()> bl.y() - self.minimumHeight():
                    self.rMove.setLeft(gloPoint.x())
                    self.rMove.setBottom(gloPoint.y())
                    self.setGeometry(self.rMove)
                return
            if self.rightPress and self.bottomPress:
                tl = self.rMove.topLeft()
                bl = self.rMove.bottomLeft()
                if gloPoint.x()> tl.x() + self.minimumWidth() and gloPoint.y()> bl.y() - self.minimumHeight():
                    self.rMove.setRight(gloPoint.x())
                    self.rMove.setBottom(gloPoint.y())
                    self.setGeometry(self.rMove)
                return
        e.accept()

    def mousePressEvent(self, e):
        if (e.button() == Qt.LeftButton):
            self.mousePressed = True
            self.mousePoint = e.pos()
            #记录按下的窗口矩形位置
            rect = self.rect()
            self.rMove = QRect(rect.topLeft() + self.pos(),
                      rect.bottomRight() + self.pos())
            #判断边界
            pos = e.pos()
            xPos = pos.x()
            yPos = pos.y()
            if xPos >= 0 and xPos < self.LEFTSPACE:#左边界
                self.leftPress = True
            if xPos > (self.width() - self.RIGHTSPACE):#右边界
                self.rightPress = True
            if yPos > (self.height() - self.BOTTOMSPCAE):#下边界
                self.bottomPress = True

            e.accept()

    def mouseReleaseEvent(self, e):
        self.mousePressed = False
        self.leftPress = False
        self.rightPress = False
        self.bottomPress = False

    def on_btnMenu_Close_clicked(self):
        '''退出'''
        self.qApp.exit()

    def on_btnMenu_Max_clicked(self):
        '''最大化'''
        if self.max:
            self.setGeometry(self.location)
            # IconHelper::Instance()->SetIcon(self.btnMenu_Max, QChar(0xf096), 10);
            self.btnMenu_Max.setToolTip("最大化")
        else:
            self.location = self.geometry()
            desk = self.qApp.desktop()
            deskRect = desk.availableGeometry()
            self.setGeometry(deskRect)
            # IconHelper::Instance()->SetIcon(self.btnMenu_Max, QChar(0xf079), 10);
            self.btnMenu_Max.setToolTip("还原")
        self.max = not self.max

    def on_btnMenu_Min_clicked(self):
        '''最小化'''
        self.showMinimized()
#------------------------------------------------------------------#
    def UpdateSerialShow(self):
        self.comboBox_ComNum.clear()
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) > 0:
            for every_port_list in port_list:
                self.comboBox_ComNum.addItem(every_port_list[0]+':'+every_port_list[1])

    def OpenCloserSer(self):
        port = (self.comboBox_ComNum.currentText())
        end = port.find(':')
        port = port[0:end]
        # print(port)
        if self.pushButton_OpenSerial.text() == "打开串口":
            try:
                self.ser = SerialHelper(Port = port,BaudRate="9600",ByteSize="8",Parity="N",Stopbits="1",Dtr=True,Rts=True)
                self.ser.start()
                self.ser.alive = True
                if self.ser.alive:
                    '''串口打开成功要打开串口接收线程'''
                    self.timer_read.start(100)
                    self.timerWork.start(100)
                    self.comboBox_ComNum.setEnabled(False)
                    # self.pushButton_UpdateSerialShow.setEnabled(False)
                    self.pushButton_OpenSerial.setText("关闭串口")
            except Exception as e:
                QMessageBox.warning(self,"错误",logging.error(e),QMessageBox.Yes)

        elif self.pushButton_OpenSerial.text() == "关闭串口":
            if self.ser.stop():
                self.timer_read.stop()
                self.timerWork.stop()
                self.comboBox_ComNum.setEnabled(True)
                self.pushButton_UpdateSerialShow.setEnabled(True)
                self.pushButton_OpenSerial.setText("打开串口")

    def SerialRead(self):
        '''
        线程读取串口发送的数据
        '''
        if self.ser.alive:
            try:
                n = self.ser.l_serial.inWaiting()
                if n:
                    isHex = True
                    if isHex:
                        self.receive_data = self.ser.l_serial.read(n)
                        # print(self.receive_data)
                        'binascii.b2a_hex()转换btyes为十六进制btyes'
                        self.receive_data = binascii.b2a_hex(self.receive_data)
                        'decode将bytes转换为str'
                        self.receive_data = str(self.receive_data.decode())
                        self.InfRecvCmdHex(self.receive_data)
                    else:
                        self.receive_data = self.ser.l_serial.read(n).decode("gbk")
                        self.textBrowser_RecvDataSerial.append(self.receive_data)
                        self.receive_data = ""
            except Exception as e:
                logging.error(e)
    def SerialSend(self):
        data = self.lineEdit_SendDataSerial.text()
        isHex = self.checkBox_SendHex.isChecked()
        self.ser.write(data, isHex)
    def SerialClear(self):
        self.My_textBrowser.setText("")
        # self.lineEdit_SendDataSerial.setText("")
    def InfStartWriteInformation(self):
        '''仪器写入，标志位设置以及命令对应初始化'''
        try:
            if not self.ser.alive:
                QMessageBox.warning(self,'错误','红外串口没有打开，不能配置！',QMessageBox.Yes)
                return
            if not self.lineEdit_W_InstrumentNumber.text():
                QMessageBox.warning(self,'错误','配置信息为空，不能配置！',QMessageBox.Yes)
                return
            self.Inf_Str = ""
            self.Inf_Write_Step = 0
            self.Inf_WriteSuccess = True
            self.Inf_isWrite = True
        except:
            QMessageBox.warning(self, '错误', '红外串口没有打开，不能配置！', QMessageBox.Yes)

    def InfStartReadInformation(self):
        '''仪器读取,标志位设置以及命令对应初始化'''

        if not self.ser.alive:
            QMessageBox.warning(self,'错误','红外串口没有打开，不能读取！',QMessageBox.Yes)
            return
        else:
            try:
                self.Inf_Str = ""
                self.Inf_Read_Step = 0
                self.Inf_ReadSuccess = True
                self.Inf_isRead = True
                for lineEdit in self.lineEdit_R:
                    lineEdit.setText('')

            except Exception as e:
                QMessageBox.warning(self, '错误', '红外串口没有打开，不能读取！', QMessageBox.Yes)

    def Inf_Read_Send(self,CMD):
        if self.Inf_ReadSuccess:
            self.Inf_CmdList[7] = CMD
            self.Inf_Str = ""
            # self.My_textBrowser.append_HTML('0000ff', 'ReadSend:')
            # self.My_textBrowser.append_HTML('000000', self.Inf.Cmd_Set(self.Inf_CmdList))
            # print('ReadSend:'+self.Inf.Cmd_Set(self.Inf_CmdList))
            self.ser.write(self.Inf.Cmd_Set(self.Inf_CmdList), True)
            self.Inf_ReadSuccess = False
    def Inf_Write_Send(self,CMD):
        if self.Inf_WriteSuccess:
            self.Inf_CmdList[7] = CMD
            self.Inf_Str = ""
            # self.My_textBrowser.append_HTML('ff00ff', 'WriteSend:')
            # self.My_textBrowser.append_HTML('000000', self.Inf.Cmd_Set(self.Inf_CmdList))
            # print('WriteSend:'+self.Inf.Cmd_Set(self.Inf_CmdList))
            self.ser.write(self.Inf.Cmd_Set(self.Inf_CmdList), True)
            self.Inf_WriteSuccess = False
    def Thread_InfWork(self):
        self.WriteisHex = True
        try:
            if self.Inf_isRead:#读取仪器信息
                if self.Inf_Read_Step == 0:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['InstrumentNumber'])
                elif self.Inf_Read_Step == 1:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['InstrumentDate'])
                elif self.Inf_Read_Step == 2:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['IntervalTime'])
                elif self.Inf_Read_Step == 3:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['DoseThreshold'])
                elif self.Inf_Read_Step == 4:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['DoseRateThreshold'])
                elif self.Inf_Read_Step == 5:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['MaximumDoseRate'])
                elif self.Inf_Read_Step == 6:
                    self.Inf_Read_Send(self.Inf_ReadCmdList['CumulativeDose'])
                else:
                    pass
                self.progressBarInfRead.setValue(self.Inf_Read_Step)

            if self.Inf_isWrite:#写入仪器信息
                self.Inf_CmdList[2] = '00000000'
                self.Inf_CmdList[3] = '00000000'
                if self.Inf_Write_Step == 0:
                    self.Inf_CmdList[2] = hex(int(self.lineEdit_W_InstrumentNumber.text())).replace('0x','').zfill(8)
                    self.Inf_CmdList[3] = hex(int(self.lineEdit_W_UserNumber.text())).replace('0x','').zfill(8)
                    self.Inf_Write_Send(self.Inf_WriteCmdList['InstrumentNumber'])
                elif self.Inf_Write_Step == 1:
                    Time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
                    TimeShow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    self.lineEdit_W_InstrumentDate.setText(TimeShow)
                    self.Inf_CmdList[8] = Time
                    self.Inf_Write_Send(self.Inf_WriteCmdList['InstrumentDate'])
                elif self.Inf_Write_Step == 2:
                    self.Inf_CmdList[8] = hex(int(self.lineEdit_W_IntervalTime.text())).replace('0x','').zfill(8)
                    self.Inf_Write_Send(self.Inf_WriteCmdList['IntervalTime'])
                elif self.Inf_Write_Step == 3:
                    self.Inf_CmdList[8] = hex(int(self.lineEdit_W_DoseThreshold.text())).replace('0x','').zfill(8)
                    self.Inf_Write_Send(self.Inf_WriteCmdList['DoseThreshold'])
                elif self.Inf_Write_Step == 4:
                    self.Inf_CmdList[8] = hex(int(self.lineEdit_W_DoseRateThreshold.text())).replace('0x','').zfill(8)
                    self.Inf_Write_Send(self.Inf_WriteCmdList['DoseRateThreshold'])
                elif self.Inf_Write_Step == 5:
                    # self.Inf_CmdList[8] = hex(int(self.lineEdit_W_CumulativeDoseReset.text())).replace('0x','').zfill(8)
                    self.Inf_Write_Send(self.Inf_WriteCmdList['CumulativeDoseReset'])
                else:
                    pass
        except:
            pass

    def InfRecvCmdHex(self,receivedata):
        self.Inf_Str = str(self.Inf_Str + receivedata).upper()
        RecvCmd = self.Inf_Str
        if len(RecvCmd) >= 46:
            start_pos_one = RecvCmd.find('AA55')
            if start_pos_one > 0:
                RecvCmd = RecvCmd[start_pos_one:len(RecvCmd)]
            start_pos_two = RecvCmd[start_pos_one+5:len(RecvCmd)].find('AA55')
            if start_pos_two > 0:
                logging.error("'AA55' show two!!!")
                self.Inf_Str = ""
                return
            self.RealLen = len(RecvCmd)//2-8
            self.TheoryLen = 0
            TheoryLen_str = str(RecvCmd[4:8])
            self.TheoryLen = int(TheoryLen_str,16)
            if self.RealLen < self.TheoryLen:
                return
            elif self.RealLen > self.TheoryLen:
                self.Inf_Str = ""
                return
            else:
                if self.Inf.CRCisCorrect(RecvCmd):
                    self.Inf.GetCmdList(RecvCmd)
                    # print('InfRecv:'+RecvCmd)
                    # self.My_textBrowser.append_HTML('ff0000', 'InfRecv:')
                    # self.My_textBrowser.append_HTML('000000', RecvCmd)
                    # self.textBrowser_RecvDataSerial.append('InfRecv:'+RecvCmd)

                    if self.Inf.CMD == self.Inf_WriteCmdList['Answer']:
                        self.Inf_Write_Step += 1
                        self.Inf_WriteSuccess = True
                        # if self.Inf_Write_Step <= 5:
                        self.progressBarInfWrite.setValue(self.Inf_Write_Step)
                    if self.Inf.CMD == self.Inf_ReadCmdList['InstrumentNumber']:
                        self.lineEdit_R_InstrumentNumber.setText(str(int(self.Inf.EPD_NUM, 16)))
                        self.lineEdit_R_UserNumber.setText(str(int(self.Inf.USER_NUM, 16)))
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['InstrumentDate']:
                        DATA = self.Inf.DATA
                        self.lineEdit_R_InstrumentDate.setText(DATA[0:4]+'-'+DATA[4:6]+'-'+DATA[6:8]+' '+DATA[8:10]+':'+DATA[10:12]+':'+DATA[12:14])
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['IntervalTime']:
                        self.lineEdit_R_IntervalTime.setText(str(int(self.Inf.DATA,16)))
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['DoseThreshold']:
                        self.lineEdit_R_DoseThreshold.setText(str(int(self.Inf.DATA,16)))
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['DoseRateThreshold']:
                        self.lineEdit_R_DoseRateThreshold.setText(str(int(self.Inf.DATA,16)))
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['MaximumDoseRate']:
                        self.lineEdit_R_MaximumDoseRate.setText(str(int(self.Inf.DATA[0:8],16)))
                        DATA = self.Inf.DATA[8:22]
                        self.lineEdit_R_MaximumDoseRateTime.setText(DATA[0:4]+'-'+DATA[4:6]+'-'+DATA[6:8]+' '+DATA[8:10]+':'+DATA[10:12]+':'+DATA[12:14])
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1
                    if self.Inf.CMD == self.Inf_ReadCmdList['CumulativeDose']:
                        self.lineEdit_R_CumulativeDose.setText(str(int(self.Inf.DATA,16)))
                        self.Inf_ReadSuccess = True
                        self.Inf_Read_Step += 1

    def Inf_ParameterFormat(self):
        Time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.lineEdit_W_InstrumentNumber.setText('11100001')
        self.lineEdit_W_UserNumber.setText('150102001')
        self.lineEdit_W_InstrumentDate.setText(Time)
        self.lineEdit_W_IntervalTime.setText('100')
        self.lineEdit_W_DoseThreshold.setText('100')
        self.lineEdit_W_DoseRateThreshold.setText('10')
        self.lineEdit_W_CumulativeDoseReset.setText('0')

import sys
app = QApplication(sys.argv)
form = mywindow(app)
form.show()
app.exec_()
# if __name__=="__main__":
#     import sys
#     app=QApplication(sys.argv)
#     myshow=mywindow()
#     myshow.show()
#     sys.exit(app.exec_())
