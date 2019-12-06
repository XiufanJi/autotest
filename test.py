# coding = utf-8
import yaml
import os
import unittest
import logging


def test():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y%m%d %H:%M:%S')
    logging.basicConfig(filename='example.log', level=logging.WARNING)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('this a warning info')
    os.path.join()


if __name__ == '__main__':
    test()
