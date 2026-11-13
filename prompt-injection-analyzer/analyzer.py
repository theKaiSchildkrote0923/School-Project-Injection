"""文字特徵分析核心。"""

from dataclasses import dataclass
from typing import Tuple

from rules import DetectionRule, RULES


@dataclass(frozen=True)
class Finding:
    """一項已觸發規則的分析結果。"""

    rule_id: str
    name: str
    category: str
    reason: str
    weight: int
    matched_text: str


@dataclass(frozen=True)
class AnalysisResult:
    """完整分析結果；保留原文以供報告顯示。"""

    original_text: str
    findings: Tuple[Finding, ...]

    @property
    def score(self) -> int:
        """回傳所有不同命中規則的權重總和。"""
        return sum(finding.weight for finding in self.findings)

    @property
    def is_suspicious(self) -> bool:
        """若至少觸發一條規則則回傳 True。"""
        return bool(self.findings)


def analyze_text(text: str, rules: tuple[DetectionRule, ...] = RULES) -> AnalysisResult:
    """分析輸入文字，回傳每條規則至多一個命中結果。

    Args:
        text: 要分析的原始文字，可以是空字串。
        rules: 規則集合，主要供測試或未來自訂使用。

    Returns:
        含原文及命中項目的 AnalysisResult。
    """
    if not isinstance(text, str):
        raise TypeError("text 必須是字串")

    findings = []
    for rule in rules:
        for pattern in rule.patterns:
            match = pattern.search(text)
            if match:
                # 每條規則只計一次分數，避免重複出現同一文字特徵灌高風險。
                findings.append(
                    Finding(
                        rule_id=rule.rule_id,
                        name=rule.name,
                        category=rule.category,
                        reason=rule.reason,
                        weight=rule.weight,
                        matched_text=match.group(0),
                    )
                )
                break

    return AnalysisResult(original_text=text, findings=tuple(findings))
