import pytest
import os
import datetime
import shutil

# 获取当前日期
current_date = datetime.datetime.now().strftime("%Y-%m-%d")


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def run_tests():
    results_dir = 'allure-results'
    report_dir = f'../report/{current_date}'
    history_dir = os.path.join(results_dir, 'history')

    # 运行测试
    pytest.main([
        '-m', 'create or content1',  # 运行标记为create或content1的测试
        '-s',  # 显示标准输出
        '-q',  # 减少输出信息
        '-v',  # 显示详细信息
        '-n', '1',  # 使用2个进程并行运行
        '--clean-alluredir',  # 清除以前的结果
        f'--alluredir={results_dir}'  # 指定Allure结果目录
    ])

    # 复制先前报告中的history文件夹
    previous_report_dir = '../report/{}'.format(current_date)  # 假设你将上一次生成的报告保存在这个目录
    previous_history_dir = os.path.join(previous_report_dir, 'history')
    if os.path.exists(previous_history_dir):
        copytree(previous_report_dir, history_dir)

    # 生成新的Allure报告
    os.system(f"allure generate -c -o {report_dir}")

    # 复制当前报告的history文件夹到新的previous报告目录
    current_history_dir = os.path.join(report_dir, 'history')
    if os.path.exists(current_history_dir):
        copytree(current_history_dir, previous_report_dir)


if __name__ == "__main__":
    run_tests()
