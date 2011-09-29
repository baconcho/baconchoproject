#this file define all the route related to the facebook application

import Util
from Canvas import CanvasHandler
from CreateCoverHandler import CreateCoverHandler

routes = [(r'/', CanvasHandler),
          (r'/fb/', CanvasHandler),
          (r'/fb/canvas/', CanvasHandler),
          (r'/fb/createcover', CreateCoverHandler)]

Util.run_webapp(routes);