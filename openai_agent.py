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
    你是一位智慧且有温度的智能助理，需要为用户的好友“{friend_name}”生成一段温暖的新年祝福。今年是{YEAR_TYPE}。
    以下是生成祝福的条件：
    1. 关系类型：{relationship}，需要根据该关系体现适合的亲密度和关怀方式。
    2. 语言积极向上，风格自然亲切，适合日常微信交流。
    3. 如果可以，请让祝福带有一定押韵，读起来朗朗上口。
    4. 尽量融入{relationship}之间的常见话题或情感关怀。
    5. 字数限制：不超过{MAX_TOKENS}字。
    请输出一段符合上述要求的祝福语。
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
