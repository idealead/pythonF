from fontTools import subset
import functools
import time
from pathlib import Path
import os
import math
# options = subset.Options() # dir(options)
# font = subset.load_font('ZQKHYT.otf', options)
# subsetter = subset.Subsetter(options)
# subsetter.populate(text = 'QQAABBb的功夫更热很急很关键不那么你们二天二u一样UI在线充值卡里反倒是我大神分vvs问问v不能一样圆通 方法更好吃v报道和规范化')
# subsetter.subset(font)
# options.flavor = 'woff'
# print('开始'+str(time.time()))
# subset.save_font(font, 'Rotf.woff', options)

uid = 0
font_name = 'pfht'
text="abcABC"
relative_path='/home/creative/venv/userFont/user'
user_file = Path(relative_path+str(uid))
file_name='pfht.woff'

fontFamily={'pfht':'fontCut/font/pfht.ttf','japanhymc':'fontCut/font/japanhymc.ttf','yrdzsl-Bold':'fontCut/font/yrdzsl-Bold.ttf','fzchft':'fontCut/font/fzchft.ttf','fzmhft':'fontCut/font/fzmhft.ttf','fzytft':'fontCut/font/fzytft.ttf','bulmer_bt':'fontCut/font/bulmer_bt.ttf','FZHLFW':'fontCut/font/FZHLFW.ttf','fzxlft':'fontCut/font/fzxlft.ttf','hkktlj':'fontCut/font/hkktlj.ttf','fzwbft':'fontCut/font/fzwbft.ttf','fzfmjt':'fontCut/font/fzfmjt.ttf','fzzch':'fontCut/font/fzzch.ttf','fzmshljt':'fontCut/font/fzmshljt.ttf','ygytkjt':'fontCut/font/ygytkjt.ttf','jhrhz':'fontCut/font/jhrhz.ttf','syht':'fontCut/font/syht.otf','fzmhjt':'fontCut/font/fzmhjt.ttf','hyzzsdh':'fontCut/font/hyzzsdh.ttf','tttgb':'fontCut/font/tttgb.otf','czsldkpj':'fontCut/font/czsldkpj.ttf','hkpp':'fontCut/font/hkpp.ttf','fzcygbk':'fontCut/font/fzcygbk.ttf','alba':'fontCut/font/alba.ttf','fzxs24':'fontCut/font/fzxs24.ttf','fzyx':'fontCut/font/fzyx.otf','fzljdkt':'fontCut/font/fzljdkt.ttf','hydsyxt':'fontCut/font/hydsyxt.ttf','hyjsj':'fontCut/font/hyjsj.ttf','bdzyjt':'fontCut/font/bdzyjt.ttf','fzltzch_gbk':'fontCut/font/fzltzch_gbk.ttf','fzchyjt':'fontCut/font/fzchyjt.ttf','fzcysbft':'fontCut/font/fzcysbft.otf','fzdz':'fontCut/font/fzdz.ttf','fzyht':'fontCut/font/fzyht.ttf','hkstw12':'fontCut/font/hkstw12.ttf','adobefs':'fontCut/font/adobefs.otf','adobeht':'fontCut/font/adobeht.otf','fzhlgbk':'fontCut/font/fzhlgbk.ttf','fzht_gbk':'fontCut/font/fzht_gbk.ttf','myrzzyt':'fontCut/font/myrzzyt.ttf','rzrxnfhj':'fontCut/font/rzrxnfhj.ttf','fzqkst':'fontCut/font/fzqkst.otf','mcst':'fontCut/font/mcst.otf','Herculanum':'fontCut/font/Herculanum.ttf','fzdbs':'fontCut/font/fzdbs.ttf','fzdbsjt':'fontCut/font/fzdbsjt.ttf','ymct':'fontCut/font/ymct.ttf','fzdhjt':'fontCut/font/fzdhjt.otf','fzzys_gbk':'fontCut/font/fzzys_gbk.ttf','fztcghjt':'fontCut/font/fztcghjt.ttf','fzjtjt':'fontCut/font/fzjtjt.otf','fzgljt':'fontCut/font/fzgljt.ttf','syht_bold':'fontCut/font/syht.otf','adobehtstd':'fontCut/font/adobehtstd.otf','fzzyft':'fontCut/font/fzzyft.ttf','fzhpft':'fontCut/font/fzhpft.ttf','fzxs14':'fontCut/font/fzxs14.ttf','fzzyjt':'fontCut/font/fzzyjt.ttf','hwkt':'fontCut/font/hwkt.ttf','hyqh35':'font/hyqh35.otf','hyqh45':'font/hyqh45.otf','hyqh55':'font/hyqh55.otf','hyqh85':'font/hyqh85.otf'}
##############################################################
def returndata(code,path='',woffPath=''):
    if code==1:
        return {'path':path,'woffPath':woffPath,'code':code,'msg':'压缩完毕'}
    elif code==0:
        return{'code':code,'msg':'字体包不存在','path':path}
def callback(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return cut_obj.backF()
    return wrapper

def writeCss(uid, font_name, file_name):
    cssPath=relative_path+str(uid)+'/'+file_name+'.css'
    with open(cssPath, "w+") as f:
        f.write(
            "@font-face { \nfont-family: '%s';\nsrc: url('%s.woff') format('woff');\nfont-weight: normal;\nfont-style: normal;\n}" % (font_name, file_name))
    print('写入css成功')
    return returndata(1,'/user'+str(uid)+'/'+file_name+'.css','/user'+str(uid)+'/'+file_name+'.woff')

class fontCut(object):
    def __init__(self, file_path, output_path, text):
        self.file_path = file_path
        self.output_path = output_path
        self.text = text

    def initOption(self, **kwargs):
        # 设置选项
        self.options = subset.Options()
        self.options.flavor = 'woff'
        for k, v in kwargs.items():
            if not hasattr(self.options, k):
                setattr(self.options, k, v)
        # 实例化字体
        self.font = subset.load_font(self.file_path, self.options)
        # 设置配置器
        self.subsetter = subset.Subsetter(self.options)
        self.subsetter.populate(text=self.text)
        self.subsetter.subset(self.font)
        # 设置配置器

    @callback
    def startCut(self):
        subset.save_font(self.font, self.output_path, self.options)

class cutClass(object):
    def cutF(self):
        if user_file.exists():
            pass    
        else:
            os.makedirs(relative_path+str(uid))
        cut = fontCut(fontFamily[font_name], relative_path+str(uid)+'/'+file_name+'.woff', text)
        cut.initOption()
        #运行主函数并返回回调结果
        return cut.startCut()
    def backF(self):
        if user_file.exists():
            print('文件目录存在，可以写入文件')
            return writeCss(uid, font_name, file_name)
        else:
            os.makedirs(relative_path+uid)
            print('创建成功,可以写入文件')
            return writeCss(uid, font_name, file_name)


cut_obj=cutClass()
def init(get_id=0,get_font_name='pfht',get_text='abcABC'):
    global uid,font_name,text,user_file,file_name
    if get_font_name in fontFamily:
        uid=get_id
        font_name=get_font_name
        file_name=get_font_name+str(math.floor(time.time()))
        user_file=Path(relative_path+str(uid))
        text=get_text
        return cut_obj.cutF()
    else:
        return returndata(0)

init(1,'hyqh85','0123456789qwertyuiopasdfghjklzxcvbnm广东联通5G升级包')














