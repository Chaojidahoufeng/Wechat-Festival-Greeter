# wechat_bot.py

import itchat
from itchat.content import TEXT

from openai_agent import generate_greeting
from relationship_inference import guess_relationship
import time

class WeChatBot:
    def __init__(self):
        # 登录
        itchat.auto_login()


    def send_new_year_greetings(self):
        """
        根据好友列表自动发送新年祝福
        """
        friends = itchat.get_friends(update=True)
        for friend in friends:
            remark_name = friend.get('RemarkName', '')
            user_name = friend['UserName']

            # 如果没有备注名，通常可以跳过或使用昵称 friend['NickName']
            if not remark_name:
                continue

            # 示例：只给特定备注名发送，避免批量发送过多
            # if remark_name != "妈二":
            #     continue

            # 推断关系
            relationship = guess_relationship(remark_name)

            # 生成祝福语
            try:
                message = generate_greeting(remark_name, relationship)
                print(f"向 {remark_name} ({relationship}) 发送消息: {message}")
                itchat.send_msg(msg=message, toUserName=user_name)
                time.sleep(1)  # 防止发送过快被限制
            except Exception as e:
                print(f"发送给 {remark_name} 时出错: {e}")

        print("所有消息已发送完成！")

    def run_forever(self):
        """
        让程序保持运行，可以在此做一些守护进程或其他后台任务
        """
        itchat.run()
