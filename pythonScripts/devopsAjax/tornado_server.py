#!/usr/bin/env  python3
#coding:UTF-8
"""#coding=UTF-8
"""
#！ -*- coding: utf8 -*-
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("uid")


class LoginHandler(BaseHandler):

    def get(self):
        self.render("templates/index.html")
        # self.finish("请使用post方法提交username/password,并且两个值保持一致")

    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if username == password:
            self.set_secure_cookie('uid', username)
            self.finish({"code":0,"msg":"OK HAHA ---ok"})
        else:
            self.finish({"code":404,"msg":"用户名和密码不正确"})


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.write("Hello, world")


def make_app():
    settings = dict(
        debug=True,
        xsrf_cookies=False,
        login_url='/login',
        cookie_secret='61oETzKXQAGaYdkL5gEmGEJJFuYh7EQnp2XdTP1o/Vo=',
    )
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler)        
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


