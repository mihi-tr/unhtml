import webapp2
import lxml.html
import urllib

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-type']="text/html; charset=utf-8"
    f=open("index.html")
    self.response.write("\n".join(f))
    f.close()

class Escape(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-type']="text/plain; charset=utf-8"
    self.response.write(lxml.html.fromstring(urllib.unquote(self.request.query)).text_content())

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/escape', Escape),
  ], debug=True)

