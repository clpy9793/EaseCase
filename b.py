import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def fn():
    print('b.py, fn')
    logger.info('msg')


def zoo():
    print('b.py, zoo')
    logger.info('msg')
