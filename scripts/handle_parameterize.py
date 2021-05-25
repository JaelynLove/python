# -*- coding: utf-8 -*-
# @Time :2020/4/30 17:07
# @Author :song
# @Email :2697013700@qq.com
# @File :handle_parameterize.py

import re
import random
import datetime
import time

from scripts.handle_mysql import HandleMysql
from scripts.handle_yaml import HandleYaml
from scripts.handle_path import USER_ACCOUNTS_FILE_PATH


class Parameterize:
    """
    参数化类
    """
    not_existed_tel_pattern = r'{not_existed_tel}'
    #管理员账号密码，userid,companyid
    admin_user_tel_pattern = r'{mobile_phone}'
    admin_user_pwd_pattern = r'{pwd}'
    admin_user_id_pattern = r'{invest_user_id}'
    admin_companyId_pattern = r'{invest_companyId}'
    do_user_account = HandleYaml(USER_ACCOUNTS_FILE_PATH)
    #产品信息
    product_name=r'{product_name}'
    brand_name=r'{brand_name}'
    manufacturer_name=r'{manufacturer_name}'
    model_name=r'{model_name}'
    originModel_name=r'{originModel_name}'

    @classmethod
    def to_param(cls, data):

        # 不存在的手机号替换
        if re.search(cls.not_existed_tel_pattern, data):
            do_mysql = HandleMysql()
            data = re.sub(cls.not_existed_tel_pattern, do_mysql.create_not_existed_mobile(), data)
            do_mysql.close()

        # 管理员手机号替换
        if re.search(cls.admin_user_tel_pattern, data):
            # do_user_account = HandleYaml(USER_ACCOUNTS_FILE_PATH)
            invest_user_tel = cls.do_user_account.read('admin', 'mobile_phone')
            data = re.sub(cls.admin_user_tel_pattern, invest_user_tel, data)

        # 投资人密码替换
        if re.search(cls.admin_user_pwd_pattern, data):
            invest_user_pwd = cls.do_user_account.read('invest', 'pwd')
            data = re.sub(cls.admin_user_pwd_pattern, invest_user_pwd, data)

        #替换companyId
        if re.search(cls.admin_companyId_pattern,data):
            # invest_companyId = cls.do_user_account.read('invest', 'companyId')
            # data = re.sub(cls.invest_companyId_pattern, invest_companyId, data)
            invest_companyId = getattr(cls, 'companyId')
            data = re.sub(cls.admin_companyId_pattern, str(invest_companyId), data)
        return data


    @classmethod
    def to_product(cls,pro_data):
        strftime=int(time.time())
        print(strftime)
        #添加产品时替换产品信息
        if re.search(cls.product_name,pro_data):
            product_name='产品a-'+str(strftime)
            brand_name ='品牌a-' +str(strftime)
            manufacturer_name ='制造商a-' +str(strftime)
            model_name ='产品型号a-' +str(strftime)
            originModel_name ='制造商型号a-'+str(strftime)

            pro_data=re.sub(cls.product_name,product_name,pro_data)
            brand_data=re.sub(cls.brand_name,brand_name,pro_data)
            manufacturer_data=re.sub(cls.manufacturer_name,manufacturer_name,brand_data)
            model_data=re.sub(cls.model_name,model_name,manufacturer_data)
            pro_data=re.sub(cls.originModel_name,originModel_name,model_data)
        return pro_data


if __name__ == '__main__':
    # companyId = 'eeeeee'
    # setattr(Parameterize, 'companyId', companyId)
    # one='http://128122373737/{invest_companyId}'
    # print(Parameterize.to_param(one))
    one = 'http://128122373737/{product_name}'
    print(Parameterize.to_product(one))


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

