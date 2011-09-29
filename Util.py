# Some convenient function

from google.appengine.ext.webapp import util
from google.appengine.ext import webapp
import os
import base64

def base64_url_decode(data):
    data = data.encode(u'ascii')
    data += '=' * (4 - (len(data) % 4))
    return base64.urlsafe_b64decode(data)

# this function run a wsgi application using the webapp framework
def run_webapp(routes):
    application = webapp.WSGIApplication(routes,
        debug=os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'))
    util.run_wsgi_app(application)