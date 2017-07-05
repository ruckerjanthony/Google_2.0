#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class PassHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write('post handler')
        real_name="josh"
        real_pass="Anthony"

        username= self.request.get("username")
        password= self.request.get("password")


        if username==real_name and password==real_pass:
            self.response.write("Whoopty do, you knew your account info")
        else:
            self.response.write("Try again kid")
        import jinja2

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname("templates")))


class TempHandler(webapp2.RequestHandler)
        def get(self):
            self.request.get()

class FormHandler(webapp2.RequestHandler):
    def get(self):
        data = (self.request.get('name') +
         self.request.get('size') +
         self.request.get('cheese') +
         self.request.get('toppings') +
         self.request.get('checkout'))
        self.response.write(data)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/submission', FormHandler),
    ('/login', PassHandler),
], debug=True)
