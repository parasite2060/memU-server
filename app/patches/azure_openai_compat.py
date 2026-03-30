"""Patch memu-py's OpenAISDKClient for Azure OpenAI compatibility.

Azure OpenAI rejects `max_tokens=null` in chat completion requests.
The upstream memu-py SDK passes `max_tokens=None` which serializes to null.
This patch wraps summarize() and vision() to omit max_tokens when it's None.
"""

import logging

from memu.llm.openai_sdk import OpenAISDKClient

logger = logging.getLogger(__name__)

_original_summarize = OpenAISDKClient.summarize
_original_vision = OpenAISDKClient.vision


async def _patched_summarize(self, text, *, max_tokens=None, system_prompt=None):
    prompt = system_prompt or "Summarize the text in one short paragraph."

    system_message = {"role": "system", "content": prompt}
    user_message = {"role": "user", "content": text}
    messages = [system_message, user_message]

    kwargs = {
        "model": self.chat_model,
        "messages": messages,
        "temperature": 1,
    }
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens

    response = await self.client.chat.completions.create(**kwargs)
    content = response.choices[0].message.content
    return content or "", response


async def _patched_vision(self, prompt, image_path, *, max_tokens=None, system_prompt=None):
    import base64
    from pathlib import Path

    image_data = Path(image_path).read_bytes()
    base64_image = base64.b64encode(image_data).decode("utf-8")

    suffix = Path(image_path).suffix.lower()
    mime_type = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(suffix, "image/jpeg")

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})

    messages.append({
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{base64_image}"}},
        ],
    })

    kwargs = {
        "model": self.chat_model,
        "messages": messages,
        "temperature": 1,
    }
    if max_tokens is not None:
        kwargs["max_tokens"] = max_tokens

    response = await self.client.chat.completions.create(**kwargs)
    content = response.choices[0].message.content
    return content or "", response


def apply():
    """Apply Azure OpenAI compatibility patches to memu-py SDK."""
    OpenAISDKClient.summarize = _patched_summarize
    OpenAISDKClient.vision = _patched_vision
    logger.info("Applied Azure OpenAI compatibility patch to memu-py SDK")
