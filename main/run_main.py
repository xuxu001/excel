# -*- coding: utf-8 -*-


from data.runmethod import RunMethod
from data.get_data import GetData

from  main.commit import CommonUtil
from unit.send_email import SendEmail

from unit.dependent import Dependent


class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
    #程序执行的主入口

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        # print('---')
        # print(rows_count)
        # print('---')

        # print(rows_count)
        for i in range(1,rows_count):
            # print(i)
            # method = self.data.get_request_method(i)
            # print(method)
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            data = self.data.get_request_data(i)
            header = self.data.is_header(i)
            expect = self.data.get_expcet_data(i)
            depend_case = self.data.is_depend(i)

            # print(method,url,data,header)

            # print(res)
            # print(expect)
            # res = res.status_code
            # print(res.status_code)
            # print(res)
            # if depend_case != None:
                # self.depend_data = Dependent()
                #获取的依赖享用数据
                # depend_response_data = self.depend_data.get_data_for_key(i)
                #获取依赖的KEY
                # depend_key = self.data.get_depend_field(i)
                # request_data[depend_key] = depend_response_data
            res = self.run_method.run_main(method, url, data, header)

            if self.com_util.is_contain(expect,res):
                # print('测试通过')
                self.data.write_result(i,'pass')
                pass_count.append(i)
            else:
                # print('测试失败')
                self.data.write_result(i,res)
                fail_count.append(i)
        # print (len(pass_count))
        # print(len(fail_count))



        self.send_email.send_main(pass_count,fail_count)

if __name__  == '__main__':
    run = RunTest()
    run.go_on_run()

