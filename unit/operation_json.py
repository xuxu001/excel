import json

class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open('../dataconfig/login.json')as fp:
            data = json.load(fp)
            print(data)


    def get_data(self,id):
        res = None
        res = self.data[id]
        # print(res)
        return self.data[id]

if __name__ ==  '__main__':
    opjson = OperationJson()
    # print(opjson.get_data('login'))
    # # print(opjson.get_data('login'))
