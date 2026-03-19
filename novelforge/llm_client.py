"""
LLM client wrapper for OpenAI-compatible APIs.
"""
import json
from typing import Dict, Any, Optional
from openai import OpenAI
from .config import Config
from .utils.logger import log


class LLMClient:
    """Wrapper for LLM API calls"""
    
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.LLM_API_KEY,
            base_url=Config.LLM_BASE_URL
        )
        self.model = Config.LLM_MODEL
        self.temperature = Config.LLM_TEMPERATURE
        self.max_tokens = Config.LLM_MAX_TOKENS
    
    def call(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        response_format: Optional[Dict[str, Any]] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Call LLM API with given prompt.
        
        Args:
            prompt: User prompt
            system_prompt: System prompt (optional)
            response_format: JSON schema for structured output (optional)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            
        Returns:
            Response text or JSON string
        """
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature or self.temperature,
            "max_tokens": max_tokens or self.max_tokens
        }
        
        if response_format:
            kwargs["response_format"] = response_format
        
        try:
            log.info(f"Calling LLM API: model={self.model}")
            response = self.client.chat.completions.create(**kwargs)
            result = response.choices[0].message.content
            log.info(f"LLM API call successful, response length: {len(result)}")
            return result
        except Exception as e:
            log.error(f"LLM API call failed: {e}")
            raise
    
    def call_json(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Call LLM API and parse JSON response.
        
        Args:
            prompt: User prompt
            system_prompt: System prompt (optional)
            temperature: Override default temperature
            
        Returns:
            Parsed JSON object
        """
        response_format = {"type": "json_object"}
        result = self.call(
            prompt=prompt,
            system_prompt=system_prompt,
            response_format=response_format,
            temperature=temperature
        )
        
        try:
            return json.loads(result)
        except json.JSONDecodeError as e:
            log.error(f"Failed to parse JSON response: {e}")
            log.error(f"Response content: {result}")
            raise


# Global instance
llm_client = LLMClient()