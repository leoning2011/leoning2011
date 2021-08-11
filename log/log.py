import logging
import threading

from api.config.config import Config
#pip install ConcurrentLogHandler
#pip install pywin32
# from cloghandler import ConcurrentRotatingFileHandler
class Log:
    def __init__(self, name=__name__, path=Config().logPath, level='INFO'):
        print(path)
        self._name = name
        self._path = path + '/' + '当天日期.txt'
        self._level = level
        self._logger = logging.getLogger(self._name)
        self._logger.setLevel(self._level)
    def _init_handler(self):
        """初始化handler"""
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(self._path, encoding='utf-8')

        return stream_handler, file_handler
    def _set_handler(self, stream_handler, file_handler, level = 'INFO'):
        """设置handler级别并添加到logger收集器"""
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        self._logger.addHandler(stream_handler)
        self._logger.addHandler(file_handler)

    def _set_formatter(self, stream_handler, file_handler):
        """设置日志输出格式"""
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
                                      '-%(levelname)s-[日志信息]: %(message)s',datefmt = '%a, %d %b %Y %H:%M:%S')
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
    def _close_handler(self,stream_handler, file_handler):
        """关闭handler"""
        stream_handler.close()
        file_handler.close()

    @property
    def Logger(self):
        """构造收集器，返回logger"""
        stream_handler, file_handler = self._init_handler()
        self._set_formatter(stream_handler, file_handler)
        self._set_handler(stream_handler, file_handler)
        self._close_handler(stream_handler, file_handler)
        return self._logger
logger = Log().Logger


#
# logger.info('哈哈')
# logger.error('嘻嘻')

