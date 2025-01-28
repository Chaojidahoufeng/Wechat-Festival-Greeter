# config.py

import os

# 这里为了演示，直接写在代码中，不建议把密钥直接暴露在代码中！
# 实际使用中请从环境变量或其他安全存储中读取
OPENAI_API_KEY = "sk-9ff896d22bf44b75966b429170103851"
OPENAI_BASE_URL = "https://api.deepseek.com"

MODEL_NAME = "deepseek-chat"

# 其他通用配置
MAX_CHAT_HISTORY = 20   # 最大保留聊天记录条数
MAX_TOKENS = 50         # 生成文本时最大token数量

YEAR_TYPE = "蛇年"
DEFAULT_GREETING = "新年快乐！祝你一切顺利！"