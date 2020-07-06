#!/usr/local/bin/python

import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
