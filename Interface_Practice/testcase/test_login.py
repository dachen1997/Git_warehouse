
'''pytest规范：
py测试文件必须要以test_开头或者_test结尾
测试类必须要以Test开头，并且不能有init方法
测试方法必须要以test_开头
断言必须要用assert

一、pytest 单元测试框架
1、什么是单元测试框架？
单元测试是指在软件开发中，针对软件的最小单位（函数、方法）进行测试
2、单元测试框架主要做什么？
-测试发现：
 从多个文件里面去找到我们的测试用例
-测试执行：
 按照一定的顺序和规则去执行，并且生成报告
-测试判断：
 通过断言判断用例的预期结果与实际结果
-测试报告：
 统计测试进度、耗时、通过率、生成测试报告

pytest插件：
pytest-html     生成HTML格式的自动化测试报告
pytest-xdist    测试用例分布式执行
pytest-ordering 改变测试用例的执行顺序
pytest-rerunfailures    用例失败重跑
allure-pytest   生成美观的测试报告
pyyaml  

二、pytest测试用例的执行方式：
1、主函数模式(pytest.main())
(1)运行所有     pytest.main()
(2)指定模块运行   pytest.main('只需加上指定的py文件名称')
(3)指定目录运行   pytest.main('只需指定一个包文件/目录（加上路径）')
(4)通过nodeid指定运行  pytest.main(./目录名称/文件名称::类名称::方法名称)
                        pytest.main(./目录名称/文件名称::函数名称)
2、命令行模式
和主函数模式参数一样

3、通过读取pytest.ini配置文件运行
位置：一般就在项目的根目录下     pytest.ini
编码：必须是ANSI，用notepad++更改编码
作用：修改pytest的默认行为
运行的规则：不管是主函数运行还是命令行模式运行，都会读取这个配置文件
格式：
[pytest] 固定的
#表示命令行参数配置，多个用空格隔开
addopts = -vs  --html ./路径/文件名.html 
#测试文件夹路劲，可自己配置
testpaths = ./testcase
#配置测试搜索的模块文件名称
python_files = test_*.py
#配置测试搜索的测试类名
python_classes = Test*
#配置测试搜索的测试函数名
python_functions = test

markers = 
    #以下均为用例的自定义的标记名称
    smoke:*****
    模块名：****

参数详解：
在列表格式中加入参数 -s  显示执行的语句结果
-v  显示更详细的信息，与-s可以合并使用    -vs
-n  支持多线程运行  -n=2  以2个线程执行用例
--reruns  失败用例重跑    --reruns=3  失败用例重跑3次
-x  表示有用例失败，就停止执行用例
--maxfail=2  表示有2个失败用例数，就停止执行用例
-k 根据测试用例的指定字符串指定用例执行
如：pytest -vs ./目录/文件 -k "包含的字符串"
-m   pytest -m "smoke or 其他标记名称(自定义的标记名称)"  即执行标记用例，多个用and连接

三、pytest执行测试用例的顺序是怎么样的呢
默认：从上到下
改变默认的执行顺序：
@pytest.mark.run(order=1)  order等于几就是第几个执行

四、如何分组执行？（常用场景：冒烟，分模块执行，分接口和web执行）
smoke：冒烟用例，肯定是分布在各个模块里面的
在配置文件做修改，如上的配置示例
配置好后  pytest -m "smoke or 其他标记名称(自定义的标记名称)"  即执行标记用例，多个用and连接
            不想执行标记用例加个not -m " mot smoke"

五、pytest跳过测试用例（场景：比如有时只执行用例级别高，或正常的用例，失败的不执行了）
1、无条件跳过
 @pytest.mark.skip(自定义原因 = ‘哈哈哈哈’)#跳过此用例的意思
2、有条件跳过
@pytest.mark.skipif(条件,没有if关键字，自定义原因)

六、生成HTML报告
--html ./路径/文件名.html  参数，可配置在pytest的配置文件中

@pytest.mark.xfail  表示期望此条用例执行是失败的，用例失败显示xfail，不会显示额外的报错信息；用例成功显示xpass

第二天：
pytest实现前后置（固件、夹具）的处理，常用三种方式：
一、setup、teardown，setup_class、teardown_class

#在每个用例之前和之后执行一次
setup()在每个用例执行前都要执行此操作
testcase
teardown（）在每个用例执行后都要执行此操作

#在类中的所有用例之前和之后只执行一次
setup_class()每个类执行前的初始化的工作（eg：创建日志对象，创建数据库连接，创建接口的请求对象）
testcase
teardown_class()每个类执行后的扫尾的工作（eg：销毁日志对象，销毁数据库连接，销毁接口的请求对象）
eg: 顺序无所谓
class   Testlogin():
    def setup_class(self):
        print("只执行一次的")
    def teardown_class(self):
        print("最后只执行一次的")
    def setup(self):
        print("每个用例执行前都要执行的")
    def teardown(self):
        print("每个用例执行后都要执行的")
    def test_login(self):
        print("111")

二、使用@pytest.fixture()来实现！！部分！！用例的前后置
 @pytest.fixture(scope="",params="",ids="",name="",autouse="")
 scope  表示的是被这个@pytest.fixture()装饰器装饰的方法或函数的作用域是session（package）、module、class、function
 params 参数化（支持list，tuple，字典列表，字典元组）
        @pytest.fixture(scope="function",params=[1,2,3])
        def fixturetest(request):#request接收params的值
            return request.param #获取params的值（循环获取）
 autouse 自动执行，默认是False
 ids     当使用params参数化时，给params中的每个值都取个对应的别名，格式要相同ids = [a,,b,c]
 name    表示被@pytest.fixture（）标记的方法起个别名
eg：
class   Testlogin():

    @pytest.fixture(scope="function")#scope=class的效果和setup_class teardown_class的效果是一样的，在类中的用例开始前和结束后只执行一次
                                      scope=module，这个模块文件只执行一次
        print("前置操作")
        yield#yield后的内容是后置操作
        print("后置操作")

    def test_login1(self,fixturetest):
        print("111")
    def test_login2(self):
        print("222")
    def test_login3(self):
        print("333")
    def test_login4(self):
        print("444")

三、通过conftest.py和@pytest.fixture()混合使用，实现全局的前后置应用（项目的全局登录，模块的全局处理）
1、conftest.py名称不能更改
2、可以在不同的文件中使用同一个fixture函数
3、原则上conftest.py要与用例放在同一层，不用导包

四、断言
assert

五、pytest结合allure，生成测试报告
1、安装
pip install allure-pytest
2、命令生成json格式的临时报告
--alluredir ./tmp
3、生成allure报告
os.system('allure generate ./tmp -o ./report --clean')
allure generate  固定格式命令
-o 表示输出到 ./report
--clean  清除report原有的报告

第三天：
一、@pytest.mark.paramtrize()实现参数化--数据驱动
基本用法：
@pytest.mark.paramtrize(args_name,args_value)
arg_name：参数名称
arg_value：参数值--有多少值用例就会执行几次
第一种：                    参数        参数值
 @pytest.mark.parametrize('inputdata',['哈哈',1111])
    def test_login2(self,inputdata):
        print(inputdata)
第二种：                多个参数         参数值
@pytest.mark.paramtrize('name,age',[['dachen',18],['xiaowang',22]])
def test_002(self,name,age):
    print(name,age)

allure报告的定制？？？
关键字驱动？？？
关键字驱动与数据驱动结合？？？
Python的反射？？？
Jenkins的持续集成？？？
发送邮件？？？
日志监控？？？
'''
import pytest
from libs.login_libs import Login #导入源码包的登录类
from tools.logindata import getting_logindata #导入tools的获取登录数据函数
from tools.token_data import flash_token_data #导入tools的oldtoken函数

flashdatalist = flash_token_data(r'../data/flash_token_data.yaml') #获取刷新token用例的数据

data = getting_logindata(r'../data/test_login_data.yaml',True) #获取登录用例的数据

class   Testlogin():

    @pytest.mark.parametrize('inputdata,reps',data)#数据驱动
    def test_case_login(self,inputdata,reps,Clean_tmpinfo):
        fin = Login().login(inputdata,True)
        assert fin['code']==reps['code'] and fin['msg']==reps['msg']

    @pytest.mark.parametrize('tokedata,res',flashdatalist)
    def test_case_flashtoken(self,tokedata,res):
        finlly = Login().flash_token(tokedata,True)
        assert finlly['code']==res['code']

if __name__ == '__main__':
    pytest.main()