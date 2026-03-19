# 🖊️ NovelForge

> 用 AI 写长篇小说，每个角色都是有灵魂的 Agent

你是否曾被 AI 写小说时的"失忆"问题困扰？写到后面忘前面，角色性格前后矛盾，伏笔埋了等于没埋？

**NovelForge 就是来解决这些问题的。**

## 🎯 解决痛点

- ❌ 写了后面忘前面，AI 总是丢失上下文
- ❌ 角色写着写着就变味儿了，人设崩塌
- ❌ 埋下的伏笔后来完全忘记回收
- ❌ 世界观设定前后矛盾

## ✨ 核心特性

| 特性 | 说明 |
|------|------|
| 🧠 **长期记忆** | 角色记得所有章节发生的事情，不会"失忆" |
| 🎭 **角色灵魂** | 每个角色都有独立的 SOUL（性格、目标、秘密） |
| 🎯 **伏笔管理** | 自动追踪所有伏笔，适时提醒回收 |
| 🌍 **世界状态** | 统一管理世界观，确保设定一致 |
| 📖 **长篇支持** | 专为百万字级别长篇小说设计 |

## 🏗️ 架构一览

```
┌─────────────────────────────────────────────────┐
│                   NovelForge                    │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐   ┌────────────────────┐    │
│  │  世界管理器   │   │    伏笔管理器       │    │
│  └──────────────┘   └────────────────────┘    │
│                                                 │
│  ┌────────────────────────────────────────┐   │
│  │          记忆系统 (AgentScope)          │   │
│  │  角色记忆 · 伏笔线索 · 世界设定          │   │
│  └────────────────────────────────────────┘   │
│                                                 │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐             │
│  │主角 │ │女主 │ │反派 │ │配角 │             │
│  │Agent│ │Agent│ │Agent│ │Agent│             │
│  └─────┘ └─────┘ └─────┘ └─────┘             │
└─────────────────────────────────────────────────┘
```

## 🚀 快速开始

```python
from novelforge import Novel, Character

# 创建小说
novel = Novel(
    title="我的仙侠小说",
    genre="奇幻",
    world_settings={"灵气体系": "五行", "境界": "炼气→化神"}
)

# 创建有灵魂的角色
主角 = Character(
    name="李云",
    role="主角",
    soul={
        "personality": "沉稳内敛，关键时刻果断",
        "goals": ["找出灭门真相", "拯救宗门"],
        "secrets": "体内藏有上古血脉"
    }
)
novel.add_character(主角)

# 生成章节（需要配置 LLM）
chapter = novel.write_chapter(
    title="第一章：下山",
    plot_points=["初入江湖", "偶遇女主", "发现线索"],
    use_llm=True
)
print(chapter.content)
```

## 📦 安装

```bash
pip install novelforge
```

## ⚙️ 配置 LLM

NovelForge 支持任意 OpenAI 兼容的 API：

```python
import os
os.environ["OPENAI_API_KEY"] = "your-key"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com/v1"
# 或使用其他兼容 API
```

## 📖 示例

```bash
# 运行科幻小说示例
python examples/scifi_novel.py

# 运行基础演示
python examples/demo.py
```

## 🤝 贡献

欢迎 Star！欢迎 Fork！欢迎 PR！

## 📝 许可证

MIT License

---

<p align="center">
Made with ❤️ by NovelForge Team
</p>