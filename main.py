import streamlit as st
import itchat
from openai_agent import generate_greeting
from relationship_inference import guess_relationship

# 全局只登录一次
if "logged_in" not in st.session_state:
    itchat.auto_login(hotReload=True)
    st.session_state["friends"] = itchat.get_friends(update=True)
    st.session_state["logged_in"] = True

st.title("WeChat Greeting - Streamlit版")

# 展示好友列表
for friend in st.session_state["friends"]:
    remark_name = friend.get('RemarkName', '')
    if not remark_name:
        continue

    with st.expander(f"备注名: {remark_name}", expanded=False):
        # 关系 (默认推断)
        default_rel = guess_relationship(remark_name, [])
        rel = st.text_input("关系", value=default_rel, key=f"rel_{remark_name}")

        # 祝福语
        if "greeting_" + remark_name not in st.session_state:
            st.session_state["greeting_" + remark_name] = ""
        
        if st.button(f"生成祝福_{remark_name}"):
            msg = generate_greeting(remark_name, rel)
            st.session_state["greeting_" + remark_name] = msg

        greeting = st.text_area("祝福语", value=st.session_state["greeting_" + remark_name], key=f"greet_txt_{remark_name}")

        if st.button(f"发送_{remark_name}"):
            if not greeting.strip():
                st.warning("祝福语不能为空！")
            else:
                # 查找 user
                user = next((f for f in st.session_state["friends"] if f.get('RemarkName','') == remark_name), None)
                if user:
                    itchat.send_msg(msg=greeting, toUserName=user["UserName"])
                    st.success(f"已发送给 {remark_name}")
                else:
                    st.error("未找到该用户")
