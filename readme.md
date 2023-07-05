# gochat-AIemoji-version

此项目后端和前端代码来自于github上开源项目Lockgit/gochat。并基于其的基础上进行魔改，进行了前端的重写和新功能的增设。

## idea

### 情感判断器

将AI(sentiment_classify)用于对话情感的识别，并基于在每一个新对话上增设根据其对话内容自动生成的emoji。

在聊天室和私聊中根据对话文本AI判断对应emoji，在服务器端调用对应模型判断(logic/publish)代码完成判断后用websocket传到客户端。

灵感来源（new bing)

### 好感显示

根据最近对话的内容，在私聊列表处显示好感条。

### AI判断(表情)

由于在go中调用依赖复杂的python AI代码几乎是不可能的，即使可以也会极大的对性能产生影响，同时，AI计算对GPU的高需求也和普通服务器对CPU的需求不同，故在实际应用的过程中，把AI模型和后端服务器分离，即在前端收到后端服务器的消息后，通过RPC调用的方式申请GPU服务器调用模型计算传输消息。（这一部分尚未完成)

### AI判断(好感度)

好感度显示需要的不仅仅是单条的消息，也是两个用户之间消息的内容和时间频率，这里如果要实时显示变化，即在每一次用户发送消息后，同时对GPU服务器发起请求，要求计算，GPU服务器应该同时拥有所有消息的存档的数据库（在计算表情的同时被存储)，这样就不用再请求后端服务器发送数据。同时，好感度判断应该考虑到将一段时间 $T_1$ 以前的好感度，同时就不用去计算 $T_1$ 之前的好感度以求计算的简便性（考虑到人对另一个人情感的细微变化随着时间的淡化后应当变成总体的感觉）（这里的科学性还有待论文的查证）

也就是说，GPU服务器应当保存$T_1$后的所有消息和$T_1$前计算出的好感度状态。

## 目前完成状态

初步完成前端部分的改进（gochat-ui）和表情，好感度状态条的绘制(gochat-ui/src/assets)

初步完成模型(使用snownlp)判断表情(sentiment_classify/test.py)和好感度(sentiment_classify/favor.py)的功能(sentiment_classify)

## TODO

AI服务端业务代码编写。

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
