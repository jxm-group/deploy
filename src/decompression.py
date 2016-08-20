#coding=utf-8

import os
import tarfile
from PyQt4.QtCore import QObject

'''
    python中的tarfile模块实现文档的归档压缩和解压缩

    功能：
        把工作空间下面的所有文件，打包生成一个tar文件
        同时提供一个方法把该tar文件中的一些文件解压缩到
        指定的目录中
'''


class Decompression(object):
    def __init__(self):
        self.__SHOW_LOG = True
        self.__STOP_DEC_FLAG = False
        self.__logOutPutFunc = None

    def setLogOutPutFunc(self,logOutPutFunc):
       self.__logOutPutFunc = logOutPutFunc

    def write_tar_file(self,path, content):
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

    def get_workspace_files(self,path = "./"):
        '''获取工作空间下面的所有文件，然后以列表的形式返回'''
        if  self.__SHOW_LOG:
            print('获取工作空间下的所有文件...')
        return os.listdir(path)

    def extract_files(self,tar_path, ext_path, ext_name):
        '''解压tar文件中的部分文件到指定目录中
        ext_name  要解压的文件名
        '''
        with tarfile.open(tar_path) as tar:
            if self.__SHOW_LOG:
                print('打开文件:[{}]'.format(tar_path))
            names = tar.getnames()
            if self.__SHOW_LOG:
                print('获取到所有文件名称:{}'.format(names))
            for name in names:
                print " name: ", name.split('.')[-1] ,":",ext_name
                if name.split('.')[-1] == ext_name:
                    if self.__SHOW_LOG:
                        print('提取文件：[{}]'.format(name))
                    tar.extract(name, path = ext_path)

    def extract_all_files(self,tar_path, ext_path):
        '''解压tar文件中的部分文件到指定目录中
        例如：
            把f:\testTar\abc.tar 解压到 f:\test\tmp\目录下
            tar_path = f:\testTar\abc.tar
            ext_path = f:\test\tmp\
        '''
        if not os.path.exists(tar_path):  #  找不到文件或者目录
            message = "Sorry, Can't find the %s" % tar_path
            raise   Exception(message)
        if not os.path.isfile(tar_path):  # 文件类型错误
            message = "Sorry,  %s: file type error" % tar_path
            raise   Exception(message)

        with tarfile.open(tar_path) as tar:
            if self.__SHOW_LOG:
                self.showLog('打开文件:[{}]'.format(tar_path))
            names = tar.getnames()
            if self.__SHOW_LOG:
                self.showLog('获取到所有文件名称:{}'.format(names))
            for name in names:
                if  self.__STOP_DEC_FLAG == True :
                    self.showLog("解压缩被终止!")
                    break
                if self.__SHOW_LOG:
                    self.showLog('提取文件：[{}]'.format(name))
                tar.extract(name, path = ext_path)

    def  showLog(self,log):
        print log
        if self.__logOutPutFunc != None:
            self.__logOutPutFunc(log)

def logOutPutFunc(log):
    print "logOutPutFunc:",log


def main():

    import sys
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

    decompression = Decompression()
    decompression.setLogOutPutFunc(logOutPutFunc)

    content = decompression.get_workspace_files()
    # 1. 打包文件
    decompression.write_tar_file(TAR_PATH, content)
    print('#' * 50)
    # 2. 提取指定文件
    # extract_files(TAR_PATH, EXT_PATH, 'html')
    # 3. 提取所有文件
    decompression.extract_all_files(TAR_PATH, EXT_PATH)

if __name__ == '__main__':
    main()
