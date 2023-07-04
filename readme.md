# gochat-AIemoji-version

此项目后端和前端代码来自于github上开源项目Lockgit/gochat。并基于其的基础上进行魔改，进行了前端的重写和新功能的增设。

## idea

### 情感判断器

将AI(sentiment_classify)用于对话情感的识别，并基于在每一个新对话上增设根据其对话内容自动生成的emoji。

在聊天室和私聊中根据对话文本AI判断对应emoji，在服务器端调用对应模型判断(logic/publish)代码完成判断后用websocket传到客户端。

logic

灵感来源（new bing)

### 好感显示

根据最近对话的内容，在私聊列表处显示好感条。

## 安装

如果安装过程出现错误，请参照read.md文件

（除m1芯片或arm架构)

提前安装git yarn docker

```bash
docker pull lockgit/gochat:1.18 # 目前使用的是1.18版本
git clone git@github.com:iku50/gochat.git
cd gochat && sh run.sh dev 127.0.0.1
```

访问  `localhost:8080`
