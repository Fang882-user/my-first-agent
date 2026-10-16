from logger import logging
class BaseAgent:
    def __init__(self,name):
        self.name = name
    def run(self):
        logging.info(f"Agent[{self.name}] 正在运行...")
        print(f"Agent[{self.name}] 正在运行...")