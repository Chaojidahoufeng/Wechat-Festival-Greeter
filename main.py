import streamlit as st
import itchat
from openai_agent import generate_greeting
from relationship_inference import guess_relationship

# 登录微信并获取好友列表
if "logged_in" not in st.session_state:
    itchat.auto_login()
    st.session_state["friends"] = itchat.get_friends(update=True)
    st.session_state["logged_in"] = True

# 标题
st.title("WeChat Greeting - Streamlit版")

# 搜索功能
search_query = st.text_input("搜索好友（昵称或备注名）：", value="", key="search_query").strip()

# 配置分页参数
friends_per_page = 10  # 每页显示的好友数

# 根据搜索结果过滤好友
filtered_friends = [
    friend for friend in st.session_state["friends"]
    if search_query.lower() in friend.get("NickName", "").lower()
    or search_query.lower() in friend.get("RemarkName", "").lower()
]

total_friends = len(filtered_friends)
total_pages = (total_friends + friends_per_page - 1) // friends_per_page  # 计算总页数

# 当前页码
current_page = st.number_input(
    "选择页面", min_value=1, max_value=max(total_pages, 1), value=1, step=1, key="current_page"
)

# 当前页好友索引范围
start_index = (current_page - 1) * friends_per_page
end_index = min(start_index + friends_per_page, total_friends)
current_friends = filtered_friends[start_index:end_index]

# 初始化状态存储
if "friend_states" not in st.session_state:
    st.session_state["friend_states"] = {
        friend.get("UserName"): {"greeting": "", "relation": ""}
        for friend in st.session_state["friends"]
    }

# 遍历当前页的好友列表
for friend in current_friends:
    # 获取好友信息
    nick_name = friend.get("NickName", "未知昵称")
    remark_name = friend.get("RemarkName", "")
    user_id = friend.get("UserName")  # 微信好友唯一标识符

    # 显示好友昵称和备注名
    display_name = f"{nick_name}（备注: {remark_name or '无'}）"

    # 延迟加载控件，仅在展开时生成
    with st.expander(f"好友: {display_name}", expanded=False):
        # 获取该好友的状态
        state = st.session_state["friend_states"][user_id]

        # 默认关系推断
        default_rel = state["relation"] or guess_relationship(remark_name, [])
        state["relation"] = st.text_input("关系", value=default_rel, key=f"rel_{user_id}")

        # 生成祝福语按钮
        if st.button(f"生成祝福_{user_id}"):
            state["greeting"] = generate_greeting(nick_name, state["relation"])
            st.success("祝福语生成成功！")

        # 显示祝福语文本框
        state["greeting"] = st.text_area(
            "祝福语", value=state["greeting"], key=f"greet_txt_{user_id}"
        )

        # 发送按钮
        if st.button(f"发送_{user_id}"):
            if not state["greeting"].strip():
                st.warning("祝福语不能为空！")
            else:
                try:
                    itchat.send_msg(msg=state["greeting"], toUserName=user_id)
                    st.success(f"已成功发送给 {nick_name}！")
                except Exception as e:
                    st.error(f"发送失败: {e}")

# 添加分页提示
if total_friends > 0:
    st.markdown(f"**搜索结果: {total_friends} 位好友，当前显示第 {current_page} 页，共 {total_pages} 页**")
else:
    st.warning("未找到匹配的好友，请更换搜索关键词！")