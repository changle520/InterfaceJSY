::进入需执行的测试用例所在的目录
cd D:/work/jishiyu/Interface_Test/test_case
::执行测试用例
pytest -sq ./opsPC/test_homePage.py --alluredir=../Report/tmp
::生成测试报告
allure generate ../Report/tmp -o ../Report/report --clean

