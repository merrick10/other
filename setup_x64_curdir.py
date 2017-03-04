# -*- coding:utf-8 -*-
import os,sys,logging,re,string
#mysql_x64安装
#替换my.ini其中的绝对路径

#日志设定
logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s]%(filename)s[line:%(lineno)d][%(levelname)s] %(message)s ',                        
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='sys_install_x64.log',
                        filemode='a')

def getCurrentDirPath():
    #获取当前脚本路径
    curfilepath = os.path.realpath(sys.argv[0])
    b = os.path.split(curfilepath)
    curdir = b[0]  #当前脚本路径
    #curfilename = b[1]
    #logging.info('current realpath:'+curfilepath)
    #logging.info('current dir:'+curdir)
    #logging.info('filename:'+curfilename)
    #updir = os.path.abspath(os.path.join(curdir,'..'))  
    #logging.info('parentpath: ' + updir)#上级目录
    return curdir

def createNewScript(bakpath,scriptpath,oldcontent,newcontent):
    bakfile = open(bakpath,'r')
    bakstr = bakfile.read()
    bakstr = bakstr.replace(oldcontent, newcontent)
    bakstr = bakstr.replace("\\",'/')
    if(os.path.exists(scriptpath)):
        os.unlink(scriptpath)
        print('delete ok: '+scriptpath )
        logging.info('delete ok: '+scriptpath)
    scriptfile = open(scriptpath,'w')
    scriptfile.write(bakstr)
    scriptfile.close()
    print('create script ok: '+scriptpath )
    logging.info('create script ok: '+scriptpath )
    
    
currentdir = getCurrentDirPath()
logging.info('current dir:'+currentdir)
print('current dir:'+currentdir)



path_mysqlini_x64_bak = currentdir + '/mysql_x64/my.ini_bak'
#path_mysqlini_win32_bak = currentdir + '/mysql_win32/my.ini_bak'
path_myini = currentdir + '/mysql_x64/my.ini'

createNewScript(path_mysqlini_x64_bak,path_myini,'<setupdir>',currentdir)


##inifile = open(path_mysqlini_x64_bak,'r')
##inistr = inifile.read()
###print(inistr)
##newinistr = inistr.replace("<setupdir>", currentdir)
##newinistr = newinistr.replace("\\",'/')
###print(newinistr)
###print('\100')
##if(os.path.exists(currentdir+'/mysql_x64/my.ini')):
##    os.unlink(currentdir+'/mysql_x64/my.ini')
##    print('delete ok: '+currentdir+'/mysql_x64/my.ini' )
##myini = open(currentdir+'/mysql_x64/my.ini','w')
##myini.write(newinistr)
##myini.close()
##print('create my.ini ok: '+currentdir+'/mysql_x64/my.ini' )


#安装mysql服务
logging.info('start install mysql5.6_x64:')
print('start install mysql5.6_x64:')

#db_install_x64.bat_bak
path_dbinstallbat_bak = currentdir + '/db_install_x64.bat_bak'
path_dbinstallbat = currentdir + '/db_install_x64.bat'
createNewScript(path_dbinstallbat_bak,path_dbinstallbat,'<setupdir>',currentdir)

##
##batfile = open(path_dbinstallbat_bak,'r')
##batstr = batfile.read()
##newbatstr = batstr.replace("<setupdir>", currentdir)
##newbatstr = newbatstr.replace("\\",'/')
##
##if(os.path.exists(currentdir+'/db_install_x64.bat')):
##    os.unlink(currentdir+'/db_install_x64.bat')
##    print('delete ok: '+currentdir+'/db_install_x64.bat' )  #删除旧文件
##dbbat = open(currentdir+'/db_install_x64.bat','w')
##dbbat.write(newbatstr)
##dbbat.close()
##print('create dbinstallbat ok: '+currentdir+'/db_install_x64.bat' )


def executeScript(scriptpath):
    r1 = r1 = os.popen(scriptpath)
    info = r1.readlines()  
    for line in info:  
        line = line.strip('\r\n')
        print(line)
        logging.info(line)
        if(line=='failed'):
            logging.warn('install service failed  ... exit')
            print('install failed  ... exit')
            exit()
    logging.info('finished install service')
    print('finished install service')
    

executeScript(currentdir+'/db_install_x64.bat')

##r1 = os.popen(currentdir+'/db_install_x64.bat')
##info = r1.readlines()  
##for line in info:  
##    line = line.strip('\r\n')    
##    logging.info(line)
##    if(line=='failed'):
##        logging.warn('install db & start db service failed  ... exit')
##        print('install db & start db service failed  ... exit')
##        exit()
##logging.info('finished install mysql5.6_x64:')
##print('finished install mysql5.6_x64:')



