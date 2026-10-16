import logging
import os

# 1. 找到当前文件（logger.py）的绝对路径
# __file__ 就是当前文件的路径
# os.path.abspath() 就是把它变成这种格式：D:\my-first-agent\agent_utils\logger.py
full_path = os.path.abspath(__file__)

# 2. 往上找两层文件夹
# os.path.dirname() 的作用就是“去掉最后一部分，取上一级的路径”
# 第一次去掉文件名：D:\my-first-agent\agent_utils
# 第二次去掉文件夹：D:\my-first-agent （这就是你的项目根目录！）
base_dir = os.path.dirname(os.path.dirname(full_path))

# 3. 把项目根目录和文件名拼起来
# os.path.join() 会根据你的操作系统，自动加上正确的斜杠（Windows自动用\，Mac自动用/）
# 结果变成：D:\my-first-agent\agent.log
log_path = os.path.join(base_dir, 'agent.log')

# 4. 把这个绝对路径交给 logging
logging.basicConfig(
        filename=log_path, # 无论你从哪个文件夹运行代码，日志都会稳稳地落在项目的根目录
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        encoding='utf-8')
if __name__ == '__main__':
    logging.info("日志模块加载成功")