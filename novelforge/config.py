"""
Configuration for NovelForge
"""
import os


class Config:
    """LLM 配置"""
    
    # 上海交大 LLM API（默认）
    LLM_API_KEY = os.environ.get("OPENAI_API_KEY", "")
    LLM_BASE_URL = os.environ.get("OPENAI_API_BASE", "https://models.sjtu.edu.cn/api/v1")
    LLM_MODEL = "minimax-m2.5"
    LLM_TEMPERATURE = 0.8
    LLM_MAX_TOKENS = 4000
    
    # 可用模型列表
    AVAILABLE_MODELS = {
        "minimax-m2.5": "minimax-m2.5",
        "gpt-4o": "gpt-4o",
        "gpt-4": "gpt-4",
        "gpt-3.5-turbo": "gpt-3.5-turbo",
    }