# -*- coding: utf-8 -*-
import datetime
import codecs
import pandas as pd


def Change_name(name):
    with codecs.open("data/datainfo.csv", encoding='utf-8') as f:
        for line in f:
            l = line.split(',')
            if l[0].strip() == name:
                return l[1]
            elif l[1].strip() == name:
                return l[0]
    return name


def getData(dtStr):
    dt = datetime.datetime.strptime(dtStr, '%Y-%m-%d %H:%M:%S')
    datetimeStr = dt.strftime('%Y%m%d%H%M%S')

    prov = u'广东'.encode('gbk')
    http = 'http://172.22.1.175/di/http.action?userId=idc&pwd=U3cuYV' \
           '&interfaceId=getRACAutoRain4Prov' \
           '&dataFormat=json&prov=' + prov + \
           '&ymdhms=' + datetimeStr
    # http = 'http://172.22.1.175/di/http.action?userId=gmcrzs&pwd=hjjl' \
    #        '&interfaceId=statSurfAutoRain4Prov' \
    #        '&dataFormat=json' \
    #        '&s_ymdhms=20170822200000' \
    #        '&e_ymdhms=20170823020000' \
    #        '&prov=' + prov
    try:
        t1 = datetime.datetime.now()
        data = pd.read_json(http)
        t2 = datetime.datetime.now()
        t = t2 - t1
        print 'jason: ' + str(t)
    except Exception, e:
        print e
    else:
        datav = data.values
        adata = {}

        adata = datav[0][0]
        for key in adata.keys():
            print Change_name(key) + '   ' + adata[key]




def main():
    getData('2017-6-15 0:0:0')
if __name__ == '__main__':
    main()
