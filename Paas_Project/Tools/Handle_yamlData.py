import yaml

#导入响应配置文件路径
from Tools.Handle_Path import REPOSECONFIG_PATH

#处理配置文件
from Tools.Handle_Config import HandleConfigclass
config = HandleConfigclass()
refresh_token = config.read_config(REPOSECONFIG_PATH,'succeedLogin','token') #读取响应配置文件的token

class Handle_yamlDtaClass(object):

    @staticmethod
    def Handle_yamlDtaFunction(file,is_paramlist=True):
        with open(file,'r',encoding='utf-8') as fileobj:
            Normal_res = yaml.load(fileobj,Loader=yaml.FullLoader)

        if  is_paramlist == False:
            return Normal_res
        else:
            paramlist = []
            for i in range(len(Normal_res)):
                paramlist.append((Normal_res[i]['data'],Normal_res[i]['result'],Normal_res[i]['title']))
            return paramlist


    @staticmethod
    def Handle_RefreshyamlDtaFunction(file,is_paramlist=True):
        with open(file,'r',encoding='utf-8') as fileobj:
            Normal_res = yaml.load(fileobj,Loader=yaml.FullLoader)
        Normal_res[0]['data']['token'] = refresh_token

        if  is_paramlist == False:
            return Normal_res
        else:
            paramlist = []
            for i in range(len(Normal_res)):
                paramlist.append((Normal_res[i]['data'],Normal_res[i]['result'],Normal_res[i]['title']))
            return paramlist

    @staticmethod
    def Handle_VerifyDatalistFunction(file,is_paramlist=True):
        with open(file,'r',encoding='utf-8') as fileobj:
            Normal_res = yaml.load(fileobj,Loader=yaml.FullLoader)

        if  is_paramlist == False:
            return Normal_res
        else:
            paramlist = []
            for i in range(len(Normal_res)):
                paramlist.append((Normal_res[i]['data'],Normal_res[i]['result'],Normal_res[i]['Authorization'],Normal_res[i]['title']))
            return paramlist

if __name__ == '__main__':
    data = Handle_yamlDtaClass()
    print(data.Handle_yamlDtaFunction(r'../Datas/Login_yamlData.yaml'))
    # print(data.Handle_yamlDtaFunction(r'../Datas/Refresh_tokenyamlData.yaml',is_paramlist=False))