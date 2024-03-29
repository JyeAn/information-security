import logging

logging.basicConfig(level=logging.DEBUG,
filename='./output.log',
datefmt='%Y/%m/%d %H:%M:%S',
format='%(asctime)s-%(name)s-%(levelname)s-%(lineno)s-%(module)s-%(message)s')
logger=logging.getLogger(__name__)
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
