# -*- coding: utf-8 -*-
# @Time :2020/4/30 17:07
# @Author :song
# @Email :2697013700@qq.com
# @File :handle_parameterize.py

import re

from scripts.handle_mysql import HandleMysql
from scripts.handle_yaml import HandleYaml
from scripts.handle_path import USER_ACCOUNTS_FILE_PATH


class Parameterize:
    """
    参数化类
    """
    not_existed_tel_pattern = r'{not_existed_tel}'
    invest_user_tel_pattern = r'{invest_user_tel}'
    invest_user_pwd_pattern = r'{invest_user_pwd}'
    invest_user_id_pattern = r'{invest_user_id}'
    invest_companyId_pattern = r'{invest_companyId}'
    do_user_account = HandleYaml(USER_ACCOUNTS_FILE_PATH)

    @classmethod
    def to_param(cls, data):

        # 不存在的手机号替换
        if re.search(cls.not_existed_tel_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern, do_mysql.create_not_existed_mobile(), data)
            do_mysql.close()

        # 投资人手机号替换
        if re.search(cls.invest_user_tel_pattern, data):
            # do_user_account = HandleYaml(USER_ACCOUNTS_FILE_PATH)
            invest_user_tel = cls.do_user_account.read('invest', 'mobile_phone')
            data = re.sub(cls.invest_user_tel_pattern, invest_user_tel, data)

        # 投资人密码替换
        if re.search(cls.invest_user_pwd_pattern, data):
            invest_user_pwd = cls.do_user_account.read('invest', 'pwd')
            data = re.sub(cls.invest_user_pwd_pattern, invest_user_pwd, data)
        #替换companyId
        if re.search(cls.invest_companyId_pattern,data):
            # invest_companyId = cls.do_user_account.read('invest', 'companyId')
            # data = re.sub(cls.invest_companyId_pattern, invest_companyId, data)
            invest_companyId = getattr(cls, 'companyId')
            data = re.sub(cls.invest_companyId_pattern, str(invest_companyId), data)
        return data


if __name__ == '__main__':
    companyId = 'eeeeee'
    setattr(Parameterize, 'companyId', companyId)
    one='http://128122373737/{invest_companyId}'
    print(Parameterize.to_param(one))

    # 注册接口参数化
    # one_str = '{"mobile_phone": "{not_existed_tel}", "pwd": "12345678", "type": 1, "reg_name": "KeYou"}'
    # two_str = '{"mobile_phone": "", "pwd": "12345678"}'
    # three_str = '{"mobile_phone": "{not_existed_tel}", "pwd": "12345678901234567", "reg_name": "KeYou"}'
    # four_str = '{"mobile_phone": "{invest_user_tel}", "pwd": "12345678", "reg_name": "KeYou"}'
    #
    # # 登录接口参数化
    # five_str = '{"mobile_phone":"{invest_user_tel}","pwd":"{invest_user_pwd}"}'
    # six_str = '{"pwd":"{invest_user_pwd}"}'

    # param = Parameterize()
    # print(param.to_param(one_str))
    # print(param.to_param(two_str))
    # print(param.to_param(three_str))
    # print(param.to_param(four_str))

    # print(Parameterize.to_param(one_str))
#     # print(Parameterize.to_param(two_str))
#     # print(Parameterize.to_param(three_str))
#     # print(Parameterize.to_param(four_str))
#     # print(Parameterize.to_param(five_str))
#     # print(Parameterize.to_param(six_str))

