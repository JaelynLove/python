# -*- coding: utf-8 -*-
# @Time :2020/4/30 17:07
# @Author :song
# @Email :2697013700@qq.com
# @File :handle_yaml.py
import yaml
import ruamel.yaml

from scripts.handle_path import CONFIG_FILE_PATH

class HandleYaml:
    def __init__(self, filename):
        with open(filename, encoding="utf-8") as one_file:
            self.datas = yaml.full_load(one_file)

    def read(self, section, option):
        """
        读数据
        :param section: 区域名
        :param option: 选项名
        :return:
        """
        return self.datas[section][option]

    @staticmethod
    def write(datas, filename):
        """
        写数据
        :param datas: 嵌套字典的字典
        :param filename: yaml文件路径
        :return:
        """
        with open(filename, mode="w", encoding="utf-8") as one_file:
            yaml.dump(datas, one_file, allow_unicode=True)



do_yaml = HandleYaml(CONFIG_FILE_PATH)

if __name__ == '__main__':
    print(do_yaml.read('mysql','select_product_id'))
# #     # do_yaml = HandleYaml("configs/testcase.yaml")
# #     # do_yaml = HandleYaml(r"C:\Users\KeYou\PycharmProjects\LemonAPITest\configs\testcase.yaml")
#     do_yaml = HandleYaml
#     # datas = {
#     #     "excel": {
#     #         "cases_path": "cases.xlsx",
#     #         "result_col": 5
#     #     },
#     #     "msg": {
#     #         "success_result": "通过",
#     #         "fail_result": "Fail"
#     #     }
#     # }
#     datas='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb21wYW55TmFtZSI6InNhczIyMjIyMjIiLCJkZXB0SWQiOiIxMjc4NjM1NTM3NzY2Mjg5NDA4IiwiYXZhdGFyIjpudWxsLCJhdXRob3JpdGllcyI6WyJyb2xlc1BlclNlbCIsInF1b3RlTGlzdEluVXBkIiwicm9sZXNQZXIiLCJyZXBvc2l0b3J5U3RPdCIsInJlcG9zaXRvcnkiLCJTdWJDb21wYW55RGVsIiwic2V0dGluZyIsInJlcG9zaXRvcnlDb3VudCIsInF1b3RlIiwiU3ViQ29tcGFueSIsIm9yZGVyU2FsZVVwZCIsImlucXVpcnlMaXN0QWRkIiwib3JkZXJQdXJjaGFzZSIsImFyY2hEZXB0IiwiY3JtQ3VzVXBkIiwib3JkZXJTYWxlIiwib3JkZXIiLCJxdW90ZUxpc3RJbkRlbCIsImNvbnRyYWN0IiwicmVwb3NpdG9yeVN0SW5TZWwiLCJjb250cmFjdE1vZGVsVXBkIiwiY29tSW5mb1NlbCIsImlucXVpcnlMaXN0SW5VcGQiLCJTdWJDb21wYW55VXBkIiwiaW5xdWlyeUxpc3RJbkRlbCIsInJlcG9zaXRvcnlTdE90U2VsIiwiY29udHJhY3RMaXN0VXBkIiwicmVwb3NpdG9yeVN0b2NrIiwib3JkZXJTYWxlRGVsIiwiaW5xdWlyeUxpc3QiLCJvcmRlclB1cmNoYXNlQWRkIiwicXVvdGVMaXN0VXBkIiwiY29udHJhY3RNb2RlbCIsInF1b3RlTGlzdEluIiwib3JkZXJTYWxlU2VsIiwic2V0dGluZ1Byb2RTZWwiLCJyZXBvc2l0b3J5U3RJbiIsInJlcG9zaXRvcnlTdE90QXBwVXBkIiwiaW5xdWlyeSIsImlucXVpcnlMaXN0U2VsIiwiY29tSW5mbyIsIlN1YkNvbXBhbnlTZWwiLCJjb250cmFjdExpc3RTZWwiLCJpbnF1aXJ5TGlzdEluU2VsIiwicHJvZCIsImlucXVpcnlMaXN0SW4iLCJjcm1DdXNTZWwiLCJyZXBvc2l0b3J5RVhVcGQiLCJyZXBvc2l0b3J5U3RPdEFkZCIsInF1b3RlTGlzdFNlbCIsImNybVN1cFVwZCIsInJlcG9zaXRvcnlQQmlsbFVwZCIsInNldHRpbmdQcm9kIiwicmVwb3NpdG9yeVN0b2NrQWRkIiwicmVwb3NpdG9yeVRyYW5zQWRkIiwicXVvdGVMaXN0SW5TZWwiLCJjaGFydFNhbGUiLCJyZXBvc2l0b3J5U3RJblVwZCIsImFyY2giLCJjaGFydCIsImNvbSIsInJlcG9zaXRvcnlFWCIsInJlcG9zaXRvcnlDb3VudFNlbCIsIm9yZGVyU2FsZUFkZCIsInByb2RMaXN0IiwiaW5xdWlyeUxpc3REZWwiLCJxdW90ZUxpc3RJbkFkZCIsIm9yZGVyUHVyY2hhc2VEZWwiLCJvcmRlclRCUHVyY2hhc2VTZWwiLCJyZXBvc2l0b3J5RVhTZWwiLCJyZXBvc2l0b3J5VHJhbnMiLCJyZXBvc2l0b3J5U3RPdEFwcFNlbCIsImNybUN1c0FkZCIsImNybVN1cFNlbCIsInJlcG9zaXRvcnlQQmlsbFNlbCIsIm9yZGVyVEJQdXJjaGFzZVVwZCIsIlN1YkNvbXBhbnlBZGQiLCJpbnF1aXJ5TGlzdFVwZCIsInJlcG9zaXRvcnlTdG9ja1NlbCIsInF1b3RlTGlzdCIsImFyY2hEZXB0U2VsIiwiY29udHJhY3RNb2RlbEFkZCIsInJlcG9zaXRvcnlDb3VudFVwZCIsImNvbnRyYWN0TGlzdCIsIm9yZGVyUHVyY2hhc2VVcGQiLCJxdW90ZUxpc3RBZGQiLCJjb250cmFjdExpc3RBZGQiLCJxdW90ZUxpc3REZWwiLCJyZXBvc2l0b3J5U3RPdEFwcEFkZCIsInJvbGVzIiwicmVwb3NpdG9yeVRyYW5zU2VsIiwicmVwb3NpdG9yeUNvdW50QWRkIiwib3JkZXJUQlB1cmNoYXNlIiwiY3JtIiwicmVwb3NpdG9yeUVYQWRkIiwicmVwb3NpdG9yeVN0T3RVcGQiLCJvcmRlclB1cmNoYXNlU2VsIiwiY2hhcnRTYWxlU2VsIiwiY3JtQ3VzIiwicmVwb3NpdG9yeVN0T3RBcHAiLCJwcm9kTGlzdFNlbCIsInJlcG9zaXRvcnlTdEluQWRkIiwiY3JtU3VwIiwiY3JtU3VwQWRkIiwicmVwb3NpdG9yeVBCaWxsIiwicmVwb3NpdG9yeVBCaWxsQWRkIiwicmVwb3NpdG9yeVN0b2NrVXBkIiwiY29udHJhY3RNb2RlbFNlbCIsInJlcG9zaXRvcnlUcmFuc1VwZCJdLCJjbGllbnRfaWQiOiJYY1dlYkFwcCIsImNvbXBhbnlJZCI6IjEyNzgyNDU3MzkxMzQxOTM2NjQiLCJjcmVkaXRDb2RlIjoiMTIzMzMzMzMzMzMzMjIyMjIyIiwicGhvbmUiOiIxODkxMTExMTExNSIsInNjb3BlIjpbImFwcCJdLCJuYW1lIjoiMTg5MTExMTExMTUiLCJpZCI6IjEyODA2ODY0OTgzMDMxODQ4OTYiLCJleHAiOjE1OTQ3NTk2NDYsInN0YWZmSWQiOiIxMjgwNjg2Njc5MDMxNTQ5OTUyIiwianRpIjoiMDFhNDEwZTktMWMxMi00ZDA5LTlkZDMtNmU5MDliNjFlNDBkIiwidXNlcm5hbWUiOiIxODkxMTExMTExNSJ9.CBYnKKs5Eb_CIuBSMFmi_L3VfWuvg8_5CXqbhbNRQlG7B_kejenEJXobCpng_5UvA4QQKaaPnlfOvCcou33fvI9VTlfIfWZR6_0GLvSdHtC4F_i1m-08tXb3kzxJVuF-kLtAMJPFXYOH07PeQx8pT3a_6h5Qen-NguLkjnTh7zYX2Eie5GqK0EhItz2yqoc0whG62DGtmDcdg5mB1L3YEahFyYq3nig8S5N3lfqsHl6yujrRqTNY_hdEMTvaSFER9os0XZ8RdRMz9ZTz4go9JmxDs6XczxATzcEMvyUuC2pID8qyoivCnAMYZz28VpScWu5glNKK0h_Buu3Du_cGvg'
#    # do_yaml.write(datas,'write_datas.yaml')
#     do_yaml.set_state(datas,"write_datas.yaml")


