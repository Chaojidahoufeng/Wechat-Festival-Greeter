# main.py

from wechat_bot import WeChatBot

if __name__ == "__main__":
    bot = WeChatBot()
    # 在启动后直接调用
    bot.send_new_year_greetings()

    # # 之后进入侦听模式，保持程序不退出，以便持续收集历史消息
    # bot.run_forever()