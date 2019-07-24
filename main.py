# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
jinja_current_directory = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class login (webapp2.RequestHandler):
  def get(self):  # for a get request
    loginpage =jinja_current_directory.get_template("/templates/index.html")
    self.response.write(loginpage.render())

class mainpage (webapp2.RequestHandler):
	def get(self):
		Mainscreen =jinja_current_directory.get_template("/templates/login.html")
		self.response.write(Mainscreen.render())


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', login),
  ('/main', mainpage)
  ], debug=True)