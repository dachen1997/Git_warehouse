'''
日志等级（level）
debug       最详细的日志信息，典型应用场景是--问题诊断
info        信息详细程度仅次于debug，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
waring      当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
error       由于一个更严重的问题导致某些功能不能正常运行时记录的信息
critical    当发生严重错误，导致应用程序不能继续运行时记录的信息

日志级别等级排序：critical > error > warning > info > debug

级别越高打印的日志越少，反之亦然
debug    : 打印全部的日志( notset 等同于 debug )
info     : 打印 info, warning, error, critical 级别的日志
warning  : 打印 warning, error, critical 级别的日志
error    : 打印 error, critical 级别的日志
critical : 打印 critical 级别

一、 Logging 模块日志记录方式
Logging 模块提供了两种日志记录方式：
1、一种方式是使用 Logging 提供的模块级别的函数
2、另一种方式是使用 Logging 日志系统的四大组件记录

1、Logging 定义的模块级别函数
函数	                            说明
logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)	对root logger进行一次性配置

关键字	        描述
filename	    创建一个 FileHandler，使用指定的文件名，而不是使用 StreamHandler。
filemode	    如果指明了文件名，指明打开文件的模式（如果没有指明 filemode，默认为 'a'）。
format	handler 使用指明的格式化字符串。
datefmt	handler 使用指明的格式化字符串。
level	        指明根 logger 的级别。
                如：logging.basicconfig(Level=logging.DEBUG)后面跟的日志级别要大写，显示>=该等级的日志信息
stream	        使用指明的流来初始化 StreamHandler。该参数与 'filename' 不兼容，如果两个都有，'stream' 被忽略。
！！注意！！：Logging.basicConfig() 需要在开头就设置，在中间设置并无作用

format格式：
格式	        描述
%(levelno)s	    打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径
%(filename)s	打印当前执行程序名称
%(funcName)s	打印日志的当前函数
%(lineno)d	    打印日志的当前行号
%(asctime)s	    打印日志的时间
%(thread)d	    打印线程 ID
%(threadName)s	打印线程名称
%(process)d	    打印进程 ID
%(message)s	    打印日志信息

1.1 设置日志显示级别
通过 logging.basicConfig() 可以设置 root 的日志级别，和日志输出格式
logging.basicConfig() 关键字参数：
eg：logging.basicConfig(level=logging.INFO)

1.2 将日志信息记录到文件
logging.basicConfig(level=logging.DEBUG,filename=r'./logs/loginfo.log',filemode='w')

1.3 多个模块记录日志信息（多个模块调用时，也记录对应模块的日志信息）
eg:
myapp.py 模块

import logging
import mylib
def main():
    logging.basicConfig(filename='myapp.log',level=logging.DEBUG)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
==================================================================
mylib.py 模块

import logging

def do_something():
    logging.info('Doing something')
执行 myapp.py 模块会打印相应日志，在文件 myapp.log 中显示信息如下：

INFO:root:Started
INFO:root:Doing something
INFO:root:Finishe

1.4 显示信息的日期及更改显示消息格式
显示消息日期：
logging.basicConfig(level=logging.DEBUG,filename=r'./logs/loginfo.log',filemode='w',
                        format='%(asctime)s  %(message)s')
更改显示消息格式：
logging.basicConfig(level=logging.DEBUG,filename=r'./logs/loginfo.log',filemode='w',
                        format='%(levelname)s  %(asctime)s  %(message)s')

！！注意！！重新定义的格式修改了默认输出方式，只按照format内的格式展示

2、logging 模块四大组件
组件名称	对应类名	功能描述
日志器	    Logger	    暴露函数给应用程序，基于日志记录器和过滤器级别决定哪些日志有效
处理器	    Handler	    将 logger 创建的日志记录发送到合适的目的输出
过滤器	    Filter	    提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
格式器	    Formatter	决定日志记录的最终输出格式

'''
import logging
#只有级别在warning及以上才展示报错信息
# logging.debug("dubuginfo")
# logging.info("info")
# logging.warning("warninginfo")
# logging.error("errorinfo")
# logging.critical("criticalinfo")

def logging_test():
    logging.basicConfig(level=logging.DEBUG,filename=r'./logs/loginfo.log',filemode='w',
                        format='%(levelname)s  %(asctime)s  %(message)s')
    logging.debug("dubuginfo")
    logging.info("info")
    logging.warning("warninginfo")
    logging.error("errorinfo")
    logging.critical("criticalinfo")

logging_test()



