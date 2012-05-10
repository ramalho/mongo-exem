
import logging

from pylons import app_globals as g, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pylonsfoo.lib.base import BaseController, render

log = logging.getLogger(__name__)

class MongodbController(BaseController):

    def index(self):
        new_doc = g.mongodb.counters.find_and_modify({"counter_name":"test_counter"},
            {"$inc":{"counter_value":1}}, new=True, upsert=True , safe=True)
        return "MongoDB Counter Value: %s" % new_doc["counter_value"]
