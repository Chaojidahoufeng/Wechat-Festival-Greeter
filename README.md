# WeChat Greeting with Streamlit

这是一个基于 [Streamlit](https://streamlit.io/) 的微信祝福工具，使用 [itchat](https://github.com/littlecodersh/ItChat) 来登录并获取好友列表，结合 LLM（OpenAI/DeepSeek 接口）自动生成祝福语后发送给指定好友。你可以对生成的文案进行手动编辑，并可自定义与好友之间的关系，从而生成更贴切的祝福内容。

---

## 功能介绍

1. **微信登录**：程序启动后会使用 itchat 登录微信（可使用二维码扫码或调用缓存登录）。
2. **好友列表展示**：页面会列出所有有备注名的好友。
3. **关系输入**：可手动输入或修改预估的关系（如“母亲”、“父亲”、“朋友”等），以便针对性生成祝福语。
4. **自动生成文案**：点击 “生成” 按钮，会根据备注名和关系调用 LLM 接口生成一段简短的祝福。
5. **祝福语可编辑**：用户可在生成后对文案进行二次调整、个性化修改。
6. **一键发送**：完成编辑后，可点击 “发送” 按钮，将文案发送至指定好友。


## 快速开始

### 1. 克隆或下载项目

```bash
git clone https://github.com/Chaojidahoufeng/Wechat-Festival-Greeter.git
cd Wechat-Festival-Greeter
```

### 2. 安装依赖

确保使用 Python 3.7+，可在当前目录新建虚拟环境后安装依赖：

```bash
pip install -r requirements.txt
```

示例依赖项包括:
- `streamlit`
- `itchat`
- `openai`

### 3. 配置 OpenAI/DeepSeek API

在 `config.py` 中配置你的 API Key、模型名称及 API Base URL：

```python
# config.py
OPENAI_API_KEY = "sk-xxxxxx"
OPENAI_BASE_URL = "https://api.deepseek.com"  # 若使用OpenAI官方，可改为默认'https://api.openai.com/v1'
MODEL_NAME = "deepseek-chat"                  # 或者使用 "gpt-3.5-turbo" 等
```

> 请勿将敏感信息（如 API Key）直接暴露到公共仓库中，可改用环境变量或其他安全方案。

### 4. 运行应用

```bash
streamlit run app.py
```

- 首次运行时，会在终端输出一个访问链接，默认为 [http://localhost:8501](http://localhost:8501)  
- 在浏览器中打开该链接后，会自动触发 itchat 的登录流程；  
  - 如果 `hotReload=True`，短期内可以无需重复扫码。

### 5. 体验功能

1. **登录成功后**，页面会展示有备注名的好友列表，每个好友下方有关系输入框、按钮“生成祝福”以及祝福语编辑框和按钮“发送”。  
2. 你可以修改关系字段（如“母亲”、“朋友”、“同事”），然后点击“生成祝福”即可调用 LLM 接口生成一段简短问候。  
3. 编辑框中可对生成的内容进行再修改；  
4. 点击“发送”后，会通过 itchat 将内容发送给该好友。

---

## 目录结构示例

```
my_wechat_agent/
├── config.py                 # 存放API Key、模型名称等配置
├── openai_agent.py           # 调用OpenAI/DeepSeek接口生成祝福内容
├── relationship_inference.py # 根据备注名等推断关系
├── main.py                    # Streamlit主程序入口
├── requirements.txt          # 安装依赖
└── README.md                 # 当前文档
```

---

## 注意事项

- **微信封号风险**：大规模或频繁发送消息可能有被风控的风险。请在合理范围内使用，并遵守微信的相关规则。
- **API Key 安全**：请勿将包含敏感信息的文件直接上传至公共仓库，可以使用环境变量或其他加密措施来配置 `OPENAI_API_KEY`。
- **依赖兼容**：如在 macOS 上使用 itchat 和 Streamlit，需要保证 Python 版本与各种库之间的兼容性。
- **网络配置**：如使用代理或 VPN，需要确保 itchat 与 OpenAI/DeepSeek API 可以正常连通，否则会出现登录/生成失败等问题。

---

<!-- ## 后续扩展

1. **批量操作**：如果需要一次给所有好友群发，可在界面中添加“全部生成”或“全部发送”功能，但要小心触发微信的安全策略。
2. **关系推断升级**：可结合更多信息（如好友昵称、历史聊天内容）来自动推断更准确的关系。
3. **后台数据库**：可将当前生成或发送的记录保存到数据库（如 SQLite、MySQL 等）做审计或回放。
4. **部署**：可将 Streamlit 应用部署到云端（如 Streamlit Cloud、AWS、Docker 等）共享给团队使用，需要注意 itchat 的二维码登录和微信 Web 端在服务器环境的可行性。 -->

---

## 许可协议

根据你项目的实际情况选择相应的开源或商业授权协议。通常，可以使用 [MIT License](https://mit-license.org/) 等。

如有疑问或改进建议，欢迎在 Issues 中讨论，感谢你的使用！