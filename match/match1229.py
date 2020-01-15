# -*- coding: utf-8 -*-
import pymysql.cursors
 
#python 两个list 求交集，并集，差集 - CSDN博客  https://blog.csdn.net/bitcarmanlee/article/details/51622263
#获取两个list的交集 返回值是list
def intersection(listA,listB):
    #求交集的两种方式
    retA = [i for i in listA if i in listB]
    # retB = list(set(listA).intersection(set(listB)))
    return retA
#获取两个list的并集 返回值是list
# def union(listA,listB):
#     #求并集
#     retC = list(set(listA).union(set(listB)))
#     return retC
#获取两个list的补集 返回值是list
# def complement(listA,listB):
#     #求差集，在B中但不在A中
#     retD = list(set(listB).difference(set(listA)))
#     return retD


# 12月20日匹配逻辑
# 将模板id和标签id筛选出来组成数组
'''
例如：dict字典 dict['id']=[labelid,labelid] 
循环迭代字典value，计算与匹配标签数组的差集，按个数，将id插入新的字典 iddict[2]=[id,...id]
反序循环匹配标签的个数，将上步字典的value拼成一个list即可
'''
'''
在标签匹配数量的基础上，再进行风格排序。风格模板依次在同等匹配数量上排序。
从数据库里拿出dist={
    id:{
        labelid:[],
        style:1
    },
    id:{
        labelid:[],
        style:2
    }
}

'''
def connectMysql(hasArr=[0,0,0,0]):
    connection = pymysql.connect(host='39.108.171.116',
                                user='root',
                                password='sqladminroot0.123',
                                db='cyrd5.0',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    if isinstance(hasArr, list):
        try:
            with connection.cursor() as cursor:
                # 读取记录
                sql1="SELECT id,label_id,style FROM `in_template` where status =1 and level='permanent'"
                cursor.execute(sql1)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    else:
        return False
def data2dict(dataBase,tagArr):
    numDict = {}
    for item in dataBase:
        item['label_id']=item['label_id'].split(',')
        lenN = len(intersection(tagArr,item['label_id']))
        if(lenN in numDict):
            numDict[lenN] = numDict[lenN]+[item]
        else:
            numDict[lenN] = [item]
    return numDict
def handelSort(dictItem):
    styleSet=[]
    maxStyleTime=0
    dictStyleTime={}
    for item in dictItem:
        styleSet += [item['style']]
        if(item['style'] in dictStyleTime):
            dictStyleTime[item['style']] += 1
        else:
            dictStyleTime[item['style']] = 1
        if dictStyleTime[item['style']] > maxStyleTime:
            maxStyleTime = dictStyleTime[item['style']]
    styleSet.sort()
    styleSet = set(styleSet)
    # 获得style最多次数，以及style生序的set
    return handelListSort(dictItem,styleSet,maxStyleTime)
def handelListSort(dictItem,styleSet,max):
    # 真正处理tempid排序
    styleSet = list(styleSet)
    thisList =[0 for x in range((len(styleSet)+1)*max)]
    dictTime = {}
    styleDict = {}
    for index,value in enumerate(styleSet):
        styleDict[value] = index+1
    for item in dictItem:
        if item['style'] in dictTime:
            dictTime[item['style']] += 1
        else:
            dictTime[item['style']] = 1
        if len(styleSet) == 1:
            thisList.append(item['id'] )
        else:
            thisList[(dictTime[item['style']]-1)*(len(styleSet)-1)+styleDict[item['style']]] = item['id']    
    thisList = [ x for x in thisList if x != 0]
    return thisList
def matchMath(tagArr):
    dataBase=connectMysql()
    numDict={}
    finalList=[]
    if isinstance(dataBase, list) and isinstance(tagArr, list):
        # 处理数据库返回的数组,依据标签匹配个数加入字典
        numDict = data2dict(dataBase,tagArr)
        # 在匹配个数字典依据风格排出顺序
        index = len(tagArr)
        while index >= 0:
            if(index in numDict):
                finalList += handelSort(numDict[index])
            index -= 1
    else:
        return False
    # print(finalList)
    return {'templist':finalList}
    
# matchMath(['1','19'])