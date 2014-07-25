#import sys

from stor import root
from util import log
#import util.log

def main():
#    reload(sys)
#    sys.setdefaultencoding('utf-8')
    log.init("stor_log_1.log");
    root.start(1);

if __name__ == '__main__':
    main()