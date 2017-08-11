#-*- coding=UTF-8 -*-
import sys
import os
import sqlite3
import time
import logging
import logging.config
import sqlite3
from pyh import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
dbpath = './test.db'
def createlog(name=__name__,log_file_name = 'test1.log',debug=[],info=[],warn= [],error= [],fetal=[]):
    try:
        if os.path.getsize(log_file_name) > 1000000:
            os.remove(log_file_name)
    except BaseException:
        print 'txt can not be deleted'
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # create a file handler
        handler = logging.FileHandler(log_file_name)
        handler.setLevel(logging.DEBUG)
        # create a logging format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(handler)
        ########################解决日志重复的问题logger.removeHandler(handler)
    if info:logger.info(info)
    if debug:logger.debug(debug)
    if warn:logger.warning(warn)
    if error:logger.error(error)
    if fetal:logger.fatal(fetal)

def createHtmlfromDB(dbTable='netDelay'):
    page = PyH('summaryReport page')
    page << h1(dbTable + ' Result Report', cl='center')
    cx = sqlite3.connect(dbpath)
    cu = cx.cursor()
    cu.execute('select * from ' + dbTable)
    tab = page << table(border="1", cellspacing='0', align='center', width='1200', bordercolor='Blue')
    trTemp = tab << tr(align='center', bordercolor='Blue', bgColor='#0099ff')
    trTemp << td(u'时延') + td('ReadyToNotReady(s)')+td('NotReadyToReady(s)') + td('CreatePodTime')
    for file in cu.fetchall():
        print file
        trTemp1 = tab << tr(align='center', bordercolor='Blue')
        trTemp1 << td(file[0]) + td(file[1])+td(file[2]) + td('  ')
    fp = 'DetailPage.html'
    page.printOut(file=fp)

if __name__ == "__main__":
    createHtmlfromDB(dbTable='netDelay')