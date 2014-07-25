#import sys

from server import root
from util import log
#import util.log

def main():
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    log.init("stor_reg.log");
    root.start();

if __name__ == '__main__':
    main()