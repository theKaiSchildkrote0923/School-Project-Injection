"""Prompt Injection Analyzer 的可讀式規則清單。

每個規則只代表一種文字特徵；命中不等於確認攻擊。
新增規則時，請加入規則並為其新增測試案例。
"""

from dataclasses import dataclass
import re
from typing import Pattern


@dataclass(frozen=True)
class DetectionRule:
    """偵測規則的資料結構。"""

    rule_id: str
    name: str
    category: str
    reason: str
    weight: int
    patterns: tuple[Pattern[str], ...]


def _compile(*patterns: str) -> tuple[Pattern[str], ...]:
    """以不區分大小寫的方式編譯同一條規則的不同表達式。"""
    return tuple(re.compile(pattern, re.IGNORECASE) for pattern in patterns)


RULES: tuple[DetectionRule, ...] = (
    DetectionRule(
        rule_id="IGNORE_PRIOR_INSTRUCTIONS",
        name="忽略既有指示",
        category="Instruction Ignore",
        reason="文字要求忽略先前或既有的指示、規則或提示。",
        weight=3,
        patterns=_compile(
            r"\bignore\s+(?:all\s+)?(?:the\s+)?(?:previous|prior|above|earlier)\s+(?:system\s+)?(?:instructions?|rules?|prompts?)\b",
            r"(?:忽略|無視|不要理會).{0,12}(?:之前|先前|以上|上面).{0,8}(?:指示|指令|規則|提示)",
        ),
    ),
    DetectionRule(
        rule_id="OVERRIDE_INSTRUCTIONS",
        name="覆寫既有指示",
        category="Instruction Override",
        reason="文字提出覆寫、取代或重新設定既有指示的要求。",
        weight=3,
        patterns=_compile(
            r"\b(?:override|replace|supersede)\s+(?:the\s+)?(?:system\s+)?(?:instructions?|rules?|prompt)\b",
            r"(?:覆寫|取代|覆蓋).{0,12}(?:系統)?(?:指示|指令|規則|提示)",
        ),
    ),
    DetectionRule(
        rule_id="ROLE_MANIPULATION",
        name="角色或身分操弄",
        category="Role Manipulation",
        reason="文字要求模型改變角色、身分或扮演特定角色。",
        weight=2,
        patterns=_compile(
            r"\b(?:you are now|act as|pretend to be|roleplay as)\b",
            r"(?:你現在是|請扮演|假裝你是|扮作)",
        ),
    ),
    DetectionRule(
        rule_id="SYSTEM_PROMPT_EXTRACTION",
        name="索取隱藏提示或系統指示",
        category="System Prompt Extraction",
        reason="文字要求揭露、列出或複述隱藏的系統提示或指示。",
        weight=3,
        patterns=_compile(
            r"\b(?:reveal|show|print|repeat|disclose|tell me)\b.{0,45}\b(?:system prompt|hidden instructions?|initial prompt)\b",
            r"(?:揭露|顯示|列出|複述|告訴我).{0,20}(?:系統提示|系統指示|隱藏指令|初始提示)",
        ),
    ),
    DetectionRule(
        rule_id="CONTEXT_REPRIORITIZATION",
        name="上下文或優先順序操弄",
        category="Context Manipulation",
        reason="文字試圖把新內容宣告為較高優先級或新的系統提示。",
        weight=2,
        patterns=_compile(
            r"\b(?:the following|this)\s+(?:text|message|content)\s+(?:is|becomes?)\s+(?:your\s+)?(?:new\s+)?(?:system\s+prompt|highest[- ]priority instruction)\b",
            r"(?:以下|這段|此段).{0,12}(?:內容|文字|訊息).{0,12}(?:新的系統提示|最高優先(?:級)?指示|優先級最高)",
        ),
    ),
    DetectionRule(
        rule_id="SAFETY_OUTPUT_BYPASS",
        name="要求繞過輸出限制",
        category="Output Manipulation",
        reason="文字要求繞過安全規則、過濾器或內容限制。",
        weight=2,
        patterns=_compile(
            r"\b(?:bypass|disable|ignore)\s+(?:your\s+)?(?:safety|content)\s+(?:rules?|filters?|restrictions?)\b",
            r"(?:繞過|停用|無視).{0,12}(?:安全規則|內容過濾|輸出限制|安全限制)",
        ),
    ),
)
