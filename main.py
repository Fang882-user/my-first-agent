
from agent_utils.base_agent import BaseAgent
def read_prompt(filepath):
    try:
        with open(filepath, "r",encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("配置文件不存在,使用默认提示词")
        return "你是一个AI助手"
    except Exception as e:
        print('发生未知错误')
        return e

if __name__ == "__main__":
    prompt=read_prompt('config/prompt.txt')
    print(f"当前正在使用的提示词:{prompt}")
    agent1=BaseAgent("小码")
    agent1.run()

