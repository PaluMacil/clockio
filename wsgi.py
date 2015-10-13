__author__ = 'dan'
from ladon.server.wsgi import LadonWSGIApplication
from os.path import abspath, dirname


path = dirname(abspath(__file__))
application = LadonWSGIApplication('clockio',
                                   path_list=path,
                                   catalog_name='My Ladon webservice catalog',
                                   catalog_desc='This is the root of my cool webservice catalog')
