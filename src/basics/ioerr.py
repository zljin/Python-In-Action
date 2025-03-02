'''
subject: 文件读写和异常处理

'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

try:
    with open('resource/1.txt', 'r', encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            print(line.strip())
except FileNotFoundError as e:
    logging.exception("文件未找到:{%s}",e)
    raise FileNotFoundError('错误')
except IOError:
    logging.info("读取文件时出错")
except Exception as e:
    raise Exception('错误')