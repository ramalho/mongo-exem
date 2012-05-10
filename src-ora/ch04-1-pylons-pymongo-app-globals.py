
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
from pymongo import Connection
from pylons import config

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.mongodb_conn = Connection(config['mongodb.url'])
        self.mongodb = self.mongodb_conn[config['mongodb.db_name']]
        self.cache = CacheManager(**parse_cache_config_options(config))
