# openai_agent.py

import openai
from config import OPENAI_API_KEY, OPENAI_BASE_URL, MODEL_NAME, MAX_TOKENS, DEFAULT_GREETING, YEAR_TYPE

# 设置 OpenAI API 访问参数
openai.api_key = OPENAI_API_KEY
openai.base_url = OPENAI_BASE_URL

def generate_greeting(friend_name, relationship):
    """
    使用OpenAI生成个性化的新年祝福语。
    :param friend_name: 好友姓名（备注名）
    :param relationship: 当前推断出的关系类型（母亲、父亲、同事、朋友等）
    :return: 祝福语字符串
    """

    prompt = f"""
        你是一位智能助理，现在需要根据用户与好友的关系，为好友“{friend_name}”生成一段温暖的新年祝福。注意，今年是{YEAR_TYPE}
        关系类型：{relationship}
        要求：
        1. 内容积极向上，适合日常微信交流风格。
        2. 带有一些贴近{relationship}的关怀或交流方式。
        3. 不超过50字。
    """

    try:
        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=MAX_TOKENS
        )
        # 获取返回内容
        message_content = response.choices[0].message.content
        return message_content.strip()
    except Exception as e:
        print(f"生成祝福语失败: {e}")
        return DEFAULT_GREETING  # 默认备用祝福语
