# coding=utf8
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import json
import match.match0116 as match
import photo.photo as photo
import fontCut.fontTool as fontTool
app = Flask(__name__)
# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = 'Content-Type,XFILENAME,XFILECATEGORY,XFILESIZE,my_flag'
    resp.headers['Connection'] = 'close'
    return resp

app.after_request(after_request)
api = Api(app)

parser = reqparse.RequestParser()

# 标签数组
parser.add_argument('tagArr')
# parser.add_argument('hasArr', type=list)
# 有没有替换标题，副标题，主图，logo

# 抠图参数
parser.add_argument('access_key', type=str)
parser.add_argument('secret_key', type=str)
parser.add_argument('path', type=str)

# 压缩字体参数
parser.add_argument('user_id', type=int)
parser.add_argument('font_name', type=str)
parser.add_argument('text', type=str)
# 匹配接口
class matchf(Resource):
    def post(self):
        args = parser.parse_args()
        taglist = args['tagArr'].split(',')
        msg=match.matchMath(taglist)
        return msg

api.add_resource(matchf, '/match')

# 抠图接口
class photoshop(Resource):
    def post(self):
        args = parser.parse_args()
        # res=photo.getImage(args['access_key'],args['secret_key'],args['path'])
        res=photo.getImage('DD172E92190A75A6A93623FCCE4D6B4C','C1D959EF1553AD6B8F53AAFEE59E13CB',args['path'])
        return json.dumps(res)

api.add_resource(photoshop, '/getImage')

# 字体压缩
class cut(Resource):
    def post(self):
        args = parser.parse_args()
        res=fontTool.init(args['user_id'],args['font_name'],args['text'])
        # res=fontTool.init()
        return res

api.add_resource(cut, '/cutFont')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
