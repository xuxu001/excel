import xlrd
from xlutils.copy import copy

#操作excel

class OperatiomExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/class.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()


    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)#  打开文件
        tables = data.sheets()[self.sheet_id]  #获取文件的内容
        # print(tables)
        return tables

    #获取单元格的行数
    def get_line(self):
        tables = self.data
        # print('---')
        # print(tables)
        # print('---')
        # print( tables.nrows)
        return tables.nrows #获取单元格行数 .nrows
    #获取单元格的内容
    def get_cell_value(self,row,col):

        res = None
        res = self.data.cell_value(row,col)
        # print(res)
        return res

    #写入数据
    def write_value(self,row,col,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    #对应case-id找到对应行的内容
    def get_row_data(self,case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_value(row_num)
        return row_data
    #根据对应行数找到行号
    def get_row_num(self,case_id):
        num = 0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num + 1

    #根据行号，找到行的内容
    def get_row_value(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self,col_id = None):
        cols = None
        if col_id != None:
            cols = self.data.col_value(col_id)
        else:
            cols = self.data.col_value(0)
        return cols
if __name__ == '__main__':
    oper = OperatiomExcel()
    oper.get_data().nrows