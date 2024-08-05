# @Time：2024/8/3 10:45
# @Author: Allan
import pytest
import os

if __name__ == '__main__':
    # html报告
    # pytest.main(['-m create', '--html=../report/report.html'])
    # allure报告
    pytest.main(['-m create and content', '-s', '-q', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o ../report")
