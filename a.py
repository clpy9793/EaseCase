import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def fn():
    print('a.py, fn')
    logger.info('msg')


def zoo():
    print('a.py, zoo')
    logger.info('msg')
