# -*- coding: utf-8 -*-
import requests
import json


class RunMethod:
    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers= header)
            # print (res.status_code)
        else:
            res = requests.post(url=url,data=data)

        # if res:
        #     print(res)
        # else:
        #     print("null", url, data)
        #     # print(res.json(
        return res

    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,headers=header)


        else:
            res = requests.get(url=url,data=data)

        return res

    def run_main(self,method,url,data=None,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)

        # print(res)
        return res

if __name__ == "__main__":
    runmethod = RunMethod()