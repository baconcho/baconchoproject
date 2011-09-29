# Contains the handle for the canvas

from BaseHandler import BaseHandler

class CanvasHandler(BaseHandler):
    
    def get(self):
        if self.user:   #this will invoke the current_user method and do the authentication
            self.render(u'fbcanvas')
        else:
            self.render(u'fbcanvas')
            
    def post(self):
        self.get()