import logging
import logging.config

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%d/%m/%Y %H:%M:%S')
# logging.debug('This is a debug message')
# logging.info('This is a info message')
# logging.warning('This is a warning message')
# logging.error('This is a error message')
# logging.critical('This is a critical message')


# logger = logging.getLogger(__name__)
# 
# create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('logging_part/file.log')
# 
# level and format
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)
# 
# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)
# 
# logger.addHandler(stream_h)
# logger.addHandler(file_h)
# 
# logger.warning('this is a warning')
# logger.error('this is an error')


# logging.config.fileConfig('logging_part/logging.conf')

# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')


# import traceback
# try:
#     a = [1,2,3]
#     val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
#     or
#     logging.error("The error is %s", traceback.format_exc())


# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2KB and keep backup logs app.log.1, app.log.2, etc
# handler = RotatingFileHandler('logging_part/app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info("Hello, world!")

import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# s, m, h, d, midnight, w0
handler = TimedRotatingFileHandler('logging_part/timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Hello, world!")
    time.sleep(5)