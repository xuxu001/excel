from unit.operation_excel import OperatiomExcel
from data.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
class Dependent:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperatiomExcel()
        self.data = GetData()
    def get_case_line_data(self,case_id):
        rows_data = self.opera_excel.get_row_data(self.case_id)
        return rows_data

#
    def run_dependent(self):
        run_method = RunMethod()
        row = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_request_data(row)
        header = self.data.is_header(row)
        method = self.data.get_request_method(row)
        url = self.data.get_request_url(row)
        res = run_method.run_main(method,url,request_data,header)
        return res

    #根据依赖的key去获取执行依赖测试case的响应，然后返回

    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]

