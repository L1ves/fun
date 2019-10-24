import tornado.ioloop
import tornado.web
import httplib2

class AsyncHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = httplib2.Http()

    self.response, self.content = http.request("http://ip.jsontest.com/", "GET")
    self._async_callback(self.response, self.content)

