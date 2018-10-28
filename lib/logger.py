import logging

def getLogger(name):
  logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s - %(message)s',
    level=logging.INFO)
  return logging.getLogger('alt_py:%s:' % name)


