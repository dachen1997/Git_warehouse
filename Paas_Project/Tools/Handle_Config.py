from configparser import ConfigParser,ExtendedInterpolation


#插值时需要导入ExtendedInterpolation     在配置文件中格式${section:option}
class   HandleConfigclass:
    def __init__(self):
        self.config = ConfigParser(interpolation=ExtendedInterpolation())

    def read_config(self,config_file,Section,Section_key):
        self.config.read(config_file)
        return self.config[Section][Section_key]

    def write_config(self,datas,filename):
        '''
        datas是一个嵌套字典，eg datas = {section:{"key":"value"}}
        :param datas:
        :param filename:
        :return:
        '''
        if isinstance(datas,dict):
            for value in datas.values():
                if not  isinstance(value,dict):
                    return "数据不合法，应为嵌套字典的字典"
            for key in datas:
                self.config[key] = datas[key]
            with open(filename,'w',encoding='utf-8') as file:
                self.config.write(file)

if __name__ == '__main__':
    pass