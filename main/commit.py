#coeing:utf-8
# import main.run_main
# import unittest
from xlutils.compat import unicode


class CommonUtil:

    # def is_same(self):
    def is_contain(self,str_one,str_two):

        # res = None
        # if isinstance(str_one,unicode):
        #     str_one = str_one.encode('unicode-escape').decode('str_escape')

        if str_one == str_two:
            res = True
        else:
            res = False
        return res
