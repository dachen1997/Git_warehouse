import yaml

def getting_logindata(file,is_list=False):
    yamlfile = open(file,'r',encoding='utf-8')
    res = yaml.load(yamlfile,Loader=yaml.FullLoader)
    logindatalist = []
    for i in range(len(res)):
        logindatalist.append((res[i]['data'],res[i]['result']))
    if is_list==False:
        return res
    elif is_list==True:
        return logindatalist

if __name__ == '__main__':
    print(getting_logindata(r'../Data/loginData.yaml',is_list=True))
