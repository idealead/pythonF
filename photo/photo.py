# coding=utf8
# 抠图接口
from jdcloud_apim_sdk.simpleclient import SimpleClient
from jdcloud_apim_sdk.simplerequest import SimpleRequest
from jdcloud_apim_sdk.core.credential import Credential
from jdcloud_apim_sdk.core.config import Config
import json
# 抠图接口
def getImage(access_key, secret_key, path):
    if isinstance(path,str):
        pass
    else:
        return '路径出错'
    resp=''
    url='http://wko7luloi5tj.cn-north-1.jdcloud-api.net/api/cutout'
    method = 'POST'
    scheme = 'http'
    endpoint = 'wko7luloi5tj.cn-north-1.jdcloud-api.net'
    url = '/api/cutout'
    headers = {
        'Content-Type': 'application/octet-stream'
    }
    credential = Credential(access_key, secret_key)
    config = Config(endpoint, scheme)

    file_path = path
    image_file = open(file_path, 'rb')
    client = SimpleClient(config, credential)
    request = SimpleRequest(url, method, None, None, headers, image_file)
    try:
        resp = client.send(request)
        resp=json.loads(resp.content.decode())
        # return resp
        try:
            if resp['code']==10000:
                return {'path':resp['result']['cutout_image_url']}
            else:
                #do some thing you need
                msg=str(resp['msg'])
                return {'err':msg}
        except AttributeError as e:
            #error: has not attribute
            return {'err':'ttributeError'}
        except NameError as e:
            return {'err':'NameError'}
        except KeyError as e:
            return {'err':'KeyError'}    
    finally:
        image_file.close()
        
        

