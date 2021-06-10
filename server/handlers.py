# coding:utf-8

from tornado import web, gen
import asyncio
import json


class BaseHandler(web.RequestHandler):
    def get_json(self):
        req_data = self.request.body
        return json.loads(req_data)

    def set_res(self, ret_dict):
        self.set_header('content-type', 'application/json')
        self.write(json.dumps(ret_dict, ensure_ascii=False))
        self.set_status(200)
        self.finish()


class TestHandler(BaseHandler):
    @gen.coroutine
    def post(self):
        data = self.get_json()
        print(data['param1'])
        yield asyncio.sleep(0.5)  # processing time
        self.set_res({'result': 0})


__all__ = ['TestHandler']
