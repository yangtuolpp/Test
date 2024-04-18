# test
# 2024/4/17
from tools.logbasic import logger
import traceback
log=logger()
def test():
    try:
        1/0
    except Exception as error:
        log.info(traceback.format_exc())


if __name__ == '__main__':
    test()

