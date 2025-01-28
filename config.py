# config.py

import os

# 实际使用中请从环境变量或其他安全存储中读取
OPENAI_API_KEY = "sk-xxxxxxxxxxx"
OPENAI_BASE_URL = "https://api.deepseek.com"

MODEL_NAME = "deepseek-chat"

# 其他通用配置
MAX_CHAT_HISTORY = 20   # 最大保留聊天记录条数
MAX_TOKENS = 50         # 生成文本时最大token数量

YEAR_TYPE = "蛇年"
DEFAULT_GREETING = "新年快乐！祝你一切顺利！"