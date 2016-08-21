#coding=utf-8

import os
import tarfile
from PyQt4.QtCore import QThread, SIGNAL

'''
    python中的tarfile模块实现文档的归档压缩和解压缩

    功能：
        把工作空间下面的所有文件，打包生成一个tar文件
        同时提供一个方法把该tar文件中的一些文件解压缩到
        指定的目录中
'''


# 压缩
class CompressionThread(QThread):
    def __init__(self, Dir="./" ):
        super(CompressionThread, self).__init__()
        self.__SHOW_LOG = True
        self.__STOP_DEC_FLAG = False
        self.__Dir = Dir
        self.__logOutPutFunc = None


    def write_tar_file(self, path, content):
        '''打开指定path的tar格式的文件，如果该文件不存在
        系统会自动创建该文件，如果该文件以及存在，则打开文件
        打开文件后，向文件中添加文件(这个功能类似于把几个文件
        打包成tar包文件)
        path ='c:\\testTar\\hongten.tar'   目标
        content = [fileName01,fileName02,dir01,dir02]  要压缩的文件, 当前目录
        '''
        with tarfile.open(path, 'w') as tar:
            if self.__SHOW_LOG:
                print('打开文件:[{}]'.format(path))
            for n in content:
                if self.__SHOW_LOG:
                    print('压缩文件:[{}]'.format(n))
                tar.add(n)
            if self.__SHOW_LOG:
                print('关闭文件[{}]'.format(path))
            tar.close()

    def get_workspace_files(self, path="./"):
        '''获取工作空间下面的所有文件，然后以列表的形式返回'''
        if self.__SHOW_LOG:
            print('获取工作空间下的所有文件...')
        return os.listdir(path)

    def run(self):
        content =  self.get_workspace_files()
        self.write_tar_file(self.__Dir,content)

    def showLog(self, log):
        print log
        if self.__logOutPutFunc != None:
            self.__logOutPutFunc(log)


# 解压
class DecompressionThread(QThread):
    def __init__(self, tar_path, ext_path):
        super(DecompressionThread, self).__init__()

        self.__SHOW_LOG = True
        self.__STOP_DEC_FLAG = False
        self.__tar_path = tar_path
        self.__ext_path = ext_path

    def extract_files(self, ext_name):
        '''解压tar文件中的部分文件到指定目录中
        ext_name  要解压的文件名
        '''
        with tarfile.open(self.__tar_path) as tar:
            if self.__SHOW_LOG:
                print('打开文件:[{}]'.format(self.__tar_path))
            names = tar.getnames()
            if self.__SHOW_LOG:
                print('获取到所有文件名称:{}'.format(names))
            for name in names:
                print " name: ", name.split('.')[-1], ":", ext_name
                if name.split('.')[-1] == ext_name:
                    if self.__SHOW_LOG:
                        print('提取文件：[{}]'.format(name))
                    tar.extract(name, path=self.__ext_path)

    def extract_all_files(self):
        '''解压tar文件中的部分文件到指定目录中
        例如：
            把f:\testTar\abc.tar 解压到 f:\test\tmp\目录下
            self.__tar_path = f:\testTar\abc.tar
            self.__ext_path = f:\test\tmp\
        '''
        if not os.path.exists(self.__tar_path):  #  找不到文件或者目录
            message = "Sorry, Can't find the %s" % self.__tar_path
            raise Exception(message)
        if not os.path.isfile(self.__tar_path):  # 文件类型错误
            message = "Sorry,  %s: file type error" % self.__tar_path
            raise Exception(message)

        with tarfile.open(self.__tar_path) as tar:
            if self.__SHOW_LOG:
                self.showLog('open file:{}'.format(self.__tar_path))
            names = tar.getnames()
            # if self.__SHOW_LOG:
            #     self.showLog('获取到所有文件名称:{}'.format(names))
            i = 0
            total = len(names)

            from time import sleep

            for name in names:
                if self.__STOP_DEC_FLAG == True:
                    self.showLog("decompressing files abort!")
                    self.__STOP_DEC_FLAG = False
                    return
                i = i + 1
                if self.__SHOW_LOG:
                    sleep(1)
                    # self.showLog('提取文件：[{}]'.format(name),total,i)
                    self.showLog('decompressing file : {}'.format(name),total,i)
                tar.extract(name, path=self.__ext_path)
            sleep(2)
            self.showLog('decompress over ! ...')
            sleep(2)
            self.showLog('decompress over ! ...',-1)

    def run(self):
        self.extract_all_files()

    def showLog(self,log,total=0,count=0):
        print log
        if total <= 0:
            info = log
        else:
            info = log + "   [%s/%s]"%(count,total)

        if total == -1:
            flag = True
        else:
            flag = False
        process = {
            "status" :  flag,
            "total"  :  total,
            "count"  :  count,
        }
        self.emit(SIGNAL("Decompression_Log"), info,process)


def logOutPutFunc(log):
    print "logOutPutFunc:", log


if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)

    if os.name == 'posix' and sys.version_info[0] < 3:
        TAR_PATH = '/tmp/testTar/abc.tar'   #tar文件存放位置
        EXT_PATH = '/tmp/test/tmp'  #取出文件存放目录
    else:
        TAR_PATH = 'f:\\testTar\\hongten.tar'   #tar文件存放位置
        EXT_PATH = 'f:\\test\\tmp'  #取出文件存放目录

    try:
        _path = os.path.dirname(TAR_PATH)
        print _path
        os.makedirs(_path)
        os.makedirs(EXT_PATH)
    except Exception:
        pass

    compression = CompressionThread(TAR_PATH)
    compression.start()
    compression.wait()

    decompression = DecompressionThread(TAR_PATH, EXT_PATH)

    print('#' * 50)
    # 2. 提取指定文件
    # extract_files(TAR_PATH, EXT_PATH, 'html')
    # 3. 提取所有文件
    decompression.start()

    app.exec_()


