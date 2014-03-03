import webapp2

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
      template_values = {
            'greeting': 'Hello World',
      }

      template = jinja_environment.get_template('html/index.html')
      self.response.out.write(template.render(template_values))

class GridPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
#            'greeting': 'Hello World',
            }

        template = jinja_environment.get_template('html/bootstrap_grid.html')
        self.response.out.write(template.render(template_values))

class LayoutPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            #            'greeting': 'Hello World',
        }

        template = jinja_environment.get_template('html/bootstrap_layout.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', MainPage),('/grid', GridPage),('/layout', LayoutPage)],
                              debug=True)