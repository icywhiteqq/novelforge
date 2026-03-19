"""
Configuration for NovelMind
"""
import os


class Config:
    """LLM 配置 - 在这里修改你的API Key"""
    
    # ===== 在这里填入你的 API Key =====
    LLM_API_KEY = "sk-YOUR-KEY-HERE"  # 替换成你的key
    LLM_BASE_URL = os.environ.get("LLM_BASE_URL", os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1"))
    LLM_MODEL = "gpt-4o-mini"  # 根据你的API支持选择模型
    LLM_TEMPERATURE = 0.8
    LLM_MAX_TOKENS = 4000
    
    # 可用模型列表（根据你的API支持选择）
    AVAILABLE_MODELS = {
        "gpt-4o-mini": "gpt-4o-mini",
        "gpt-4o": "gpt-4o",
    }