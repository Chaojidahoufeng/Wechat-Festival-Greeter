# relationship_inference.py

def guess_relationship(remark_name, chat_history):
    """
    根据备注名和最近聊天记录猜测关系类型，返回一个简要描述，如 '母亲', '同事', '朋友' 等。
    :param remark_name: 好友备注名
    :param chat_history: 最近的聊天记录（list of dict），可结合内容进行判断
    :return: str, 表示关系类型
    """

    # 1. 根据备注名简单判断
    if "妈" in remark_name or "母" in remark_name:
        return "母亲"
    elif "爸" in remark_name or "父" in remark_name:
        return "父亲"
    elif "姐" in remark_name or "妹" in remark_name:
        return "姐妹"
    elif "哥" in remark_name or "弟" in remark_name:
        return "兄弟"
    elif "老公" in remark_name or "老婆" in remark_name or "爱人" in remark_name:
        return "配偶"

    # 3. 默认返回“朋友”
    return "朋友"