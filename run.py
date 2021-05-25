# -*- coding: utf-8 -*-
# @Time :2020/4/30 17:07
# @Author :song
# @Email :2697013700@qq.com
# @File :run.py

import unittest
from datetime import datetime
import os

# from cases import test_01_register
# from cases import test_02_login


from scripts.handle_yaml import do_yaml
from scripts.handle_path import REPORTS_DIR, USER_ACCOUNTS_FILE_PATH, CASES_DIR
from scripts.handle_user import generate_users_config
from libs.HTMLTestRunnerNew import HTMLTestRunner
# # 如果用户账号所在文件不存在, 则创建用户账号, 否则不创建
# if not os.path.exists(USER_ACCOUNTS_FILE_PATH):
#     generate_users_config()

# 创建测试套件
# suite = unittest.TestSuite()

# 加载用例用例到套件
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_01_register))
# suite.addTest(loader.loadTestsFromModule(test_02_login))

# 使用discover来加载用例模块
# 第一个参数为查询用例模块所在的目录路径, 第二个参数为通配符(跟shell中类似)
suite = unittest.defaultTestLoader.discover(CASES_DIR)

result_full_path = do_yaml.read('report', 'name') + '_' +  \
                   datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + '.html'
result_full_path = os.path.join(REPORTS_DIR, result_full_path)

with open(result_full_path, 'wb') as fb:
    # 创建测试运行程序
    runner = HTMLTestRunner(stream=fb,
                            title=do_yaml.read('report', 'title'),
                            description=do_yaml.read('report', 'description'),
                            tester=do_yaml.read('report', 'tester'))
    # 执行测试套件中的用例
    runner.run(suite)
