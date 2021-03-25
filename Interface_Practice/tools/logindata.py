import yaml

def getting_login_testdata(files):
    datalist = []
    obj = open(files,'r',encoding='utf-8')
    res = yaml.load(obj,Loader=yaml.FullLoader)
    #yaml.load()  yaml格式反序列化===将yaml格式转化为字典格式
    for i in range(len(res)):
        datalist.append((res[i]['data'],res[i]['result']))
    return datalist

if __name__ == '__main__':
    print(getting_login_testdata(r'../data/test_login_data.yaml'))
