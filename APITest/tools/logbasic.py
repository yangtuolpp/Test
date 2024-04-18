# logbasic
# 2024/4/14
import logging
import datetime
import os

def logger():
    fail='../log/'
    for one in os.listdir(fail):
        if one in os.listdir(fail):
            os.remove(os.path.join(fail, one))

    logging.basicConfig(format='%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s',
                        filename=f'../log/{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt',
                        level=logging.DEBUG,
                        filemode='a')

    return logging


if __name__ == '__main__':
    log = logger()
    log.debug('------hello------')
