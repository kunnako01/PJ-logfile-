import json

def imp1():
    cou = 0
    filename = "data.json"
    file = open(filename, "r")
    data_list = []
    listdata = []
    for line in file:
        data_list.append(line)
        data_dic1 = json.loads(line)
        listdata.append(data_dic1)
    print (listdata)

