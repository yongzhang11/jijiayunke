import pytest
import os
import datetime

# 获取当前日期
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


def run_tests():
    pytest.main([
        '-m', 'content1 or create  ',  # 运行标记为create或content1的测试
        '-s',  # 显示标准输出
        '-q',  # 减少输出信息
        '-v',  # 显示详细信息
        '-n', '1',  # 使用2个进程并行运行
        '--clean-alluredir',  # 清除以前的结果
        '--alluredir=allure-results'  # 指定Allure结果目录
    ])
    os.system(r"allure generate -c -o ../report/{}".format(current_date))  # 生成Allure报告


if __name__ == "__main__":
    run_tests()
