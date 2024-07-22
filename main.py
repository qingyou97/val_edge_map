import os
import time
import sched

# 定义你要监控的文件夹列表
folders = ["folder1", "folder2", "folder3", "folder4", "folder5"]

# 定义一个调度器
scheduler = sched.scheduler(time.time, time.sleep)

def check_folders():
    for folder in folders:
        file_path = os.path.join(folder, "B")
        if os.path.isfile(file_path):
            # 如果文件存在，执行你的代码
            print(f"发现文件 {file_path}，执行代码...")
            # 在这里添加你要执行的代码

            # 如果你只想监控到第一个立即执行，可以在这里返回。如果希望继续检查，删除这行代码就好
            # return

    # 每隔10分钟再执行一次这个函数
    scheduler.enter(600, 1, check_folders)

# 开始的时候立即执行一次
check_folders()

# 启动调度器
scheduler.run()
