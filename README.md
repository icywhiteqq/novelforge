# 🖊️ NovelMind

用 AI 写长篇小说，让每个角色都是有灵魂的 Agent。

你是否遇到过 AI 写长篇时"失忆"、人设崩塌、伏笔丢失的困扰？**NovelForge 就是来解决这些问题。**

## ⭐ 特性

- 🧠 **长期记忆** - 角色记得之前所有章节的事，不会"失忆"
- 🎭 **角色灵魂** - 每个角色有独立性格、目标、秘密，不再是提线木偶
- 🎯 **伏笔管理** - 自动追踪埋下的伏笔，适时提醒回收
- 🌍 **世界统一** - 统一管理世界观设定，拒绝前后矛盾
- 📖 **长篇专属** - 专为百万字级别小说设计

## 🚀 快速开始

```python
from novelforge import Novel, Character

# 创建小说
novel = Novel(title="我的小说", genre="奇幻")

# 创建有灵魂的角色
novel.add_character(Character(
    name="主角",
    role="主角", 
    soul={
        "personality": "沉稳内敛",
        "goals": ["找到真相"],
        "secrets": "体内有神秘血脉"
    }
))

# 生成章节（需配置 API Key）
chapter = novel.write_chapter(
    title="第一章：下山",
    plot_points=["初入江湖", "偶遇女主"],
    use_llm=True
)
print(chapter.content)
```

## ⚙️ 配置

编辑 `novelforge/config.py`，填入你的 API Key：

```python
LLM_API_KEY = "sk-你的KEY"  # 换成你的key
LLM_BASE_URL = "https://models.sjtu.edu.cn/api/v1"  # 或其他兼容API
```

## 📦 安装

```bash
pip install openai
```

## 🤝 贡献

欢迎 Star！欢迎 PR！

## 📝 许可证

MIT