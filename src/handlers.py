import tornado.web
import json
import base64

import db_funcs


class AddHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            body_json = json.loads(self.request.body)
            key = str(body_json['key']) + str(body_json['value'])
            key = base64.b64encode(key.encode('ascii')).decode('ascii')

            req = db_funcs.find_request(key)
            if req:
                db_funcs.add_duplicate(key)
            else:
                db_funcs.add_request(key, json.dumps(body_json))
            self.write({'key': key})
        except:
            self.write_error(400)


class GetHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            key = self.get_argument('key', None)
            req = db_funcs.find_request(key)
            if req:
                self.write({'body': req['body'], 'duplicates': req['duplicates']})
            else:
                self.write_error(404)
        except:
            self.write_error(400)


class RemoveHandler(tornado.web.RequestHandler):
    def delete(self):
        try:
            body_json = json.loads(self.request.body)
            db_funcs.delete_request(body_json['key'])
        except:
            self.write_error(400)


class UpdateHandler(tornado.web.RequestHandler):
    def put(self):
        try:
            body_json = json.loads(self.request.body)

            db_funcs.delete_request(body_json['key'])

            key = str(body_json['key']) + str(body_json['value'])

            key = base64.b64encode(key.encode('ascii')).decode('ascii')

            db_funcs.add_request(key, json.dumps(body_json))
            self.write({'key': key})
        except:
            self.write_error(400)


class StatisticHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            records = db_funcs.get_all_requests()
            duplicates = 0
            for row in records:
                duplicates += row['duplicates']
            percent = round(duplicates/len(records) * 100, 2)
            self.write({'percent': percent})
        except:
            self.write_error(400)