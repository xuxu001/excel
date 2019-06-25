# -*- coding: utf-8 -*-
from unit.operation_excel import OperatiomExcel
from data import dataconfig
from unit.operation_json import OperationJson
import json

class GetData:
    def __init__(self):
        self.operation_excel = OperatiomExcel()

    #获取行数
    def get_case_lines(self):
        cow = int(self.operation_excel.get_line())
        return cow

    #是否携带header
    def is_header(self,row):
        col = int(dataconfig.get_header())
        header = self.operation_excel.get_cell_value(row,col)
        if header == '1':
            return dataconfig.get_header_value()
        else:
            return dataconfig.get_header_value_two()
        # print(header)

    #获取请求方式
    def get_request_method(self, row):
        col = int(dataconfig.get_method())
        request_method = self.operation_excel.get_cell_value(row,col)
        # print(request_method)
        return request_method

    #获取url
    def get_request_url(self, row):
        col = int(dataconfig.get_url())
        url = self.operation_excel.get_cell_value(row,col)
        # print(url)
        # print(col)
        return url

    #获取请求数据
    def get_request_data(self, row):
        col = int(dataconfig.get_data())
        data = self.operation_excel.get_cell_value(row,col)
        # print(data)
        if data == '':
            return None
        return data


    #通过获取关键字拿到关键字
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data


    #获取预期结果
    def get_expcet_data(self,row):
        col = int(dataconfig.get_expect())
        expect = self.operation_excel.get_cell_value(row,col)
        if expect == '':
            return None
        return expect

    def write_result(self,row,value):
        col = int(dataconfig.get_result())
        self.operation_excel.write_value(row,col,value)


    def get_depend_key(self,row):
        col =int(dataconfig.get_data_depend())
        depent_key = self.operation_excel.get_cell_value(row,col)
        if depent_key == '':
            return None
        else:
            return depent_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(dataconfig.get_field_depend())
        depend_case_id = self.operation_excel.get_cell_value(row,col)
        if depend_case_id =='':
            return None
        else:
            return depend_case_id

    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(dataconfig.get_field_depend())
        data = self.operation_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data