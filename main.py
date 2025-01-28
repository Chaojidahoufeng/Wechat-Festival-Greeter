import streamlit as st
import itchat
from openai_agent import generate_greeting
from relationship_inference import guess_relationship

# 全局只登录一次
if "logged_in" not in st.session_state:
    itchat.auto_login()
    st.session_state["friends"] = itchat.get_friends(update=True)
    st.session_state["logged_in"] = True

st.title("WeChat Greeting - Streamlit版")

# 展示好友列表
for friend in st.session_state["friends"]:
    # 获取好友的微信昵称、备注名和唯一标识符
    nick_name = friend.get('NickName', '未知昵称')
    remark_name = friend.get('RemarkName', '')
    user_id = friend.get('UserName')  # 微信好友的唯一标识符

    # 将昵称和备注名拼接显示
    display_name = f"{nick_name}（备注: {remark_name or '无'}）"

    with st.expander(f"好友: {display_name}", expanded=False):
        # 关系 (默认推断)
        default_rel = guess_relationship(remark_name, [])
        rel = st.text_input("关系", value=default_rel, key=f"rel_{user_id}")

        # 祝福语
        if f"greeting_{user_id}" not in st.session_state:
            st.session_state[f"greeting_{user_id}"] = ""
        
        if st.button(f"生成祝福_{user_id}"):
            msg = generate_greeting(nick_name, rel)
            st.session_state[f"greeting_{user_id}"] = msg

        greeting = st.text_area("祝福语", value=st.session_state[f"greeting_{user_id}"], key=f"greet_txt_{user_id}")

        if st.button(f"发送_{user_id}"):
            if not greeting.strip():
                st.warning("祝福语不能为空！")
            else:
                # 查找 user
                user = next((f for f in st.session_state["friends"] if f.get('UserName', '') == user_id), None)
                if user:
                    itchat.send_msg(msg=greeting, toUserName=user["UserName"])
                    st.success(f"已发送给 {nick_name}")
                else:
                    st.error("未找到该用户")