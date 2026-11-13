"""將分析結果格式化為 CLI 純文字報告。"""

from analyzer import AnalysisResult
from risk import assess_risk


def format_report(result: AnalysisResult) -> str:
    """將完整分析結果格式化成使用者可讀的報告字串。"""
    level, explanation = assess_risk(result)
    lines = [
        "=" * 60,
        "Prompt Injection Analyzer — 分析報告",
        "=" * 60,
        f"風險等級：{level}（啟發式分數：{result.score}）",
        f"是否觸發可疑規則：{'是' if result.is_suspicious else '否'}",
        "",
        "原始輸入：",
        result.original_text if result.original_text else "（空字串）",
        "",
        "觸發規則：",
    ]

    if result.findings:
        for finding in result.findings:
            lines.extend(
                [
                    f"- {finding.name} [{finding.category}]（+{finding.weight}）",
                    f"  原因：{finding.reason}",
                    f"  命中片段：{finding.matched_text!r}",
                ]
            )
    else:
        lines.append("- 無")

    lines.extend(
        [
            "",
            f"簡短分析：{explanation}",
            "注意：這是有限規則的教育用途啟發式分析，不能證明輸入安全或確認攻擊。",
            "=" * 60,
        ]
    )
    return "\n".join(lines)
