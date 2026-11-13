"""啟發式風險分類；不是安全性保證或攻擊成功率預測。"""

from analyzer import AnalysisResult


def assess_risk(result: AnalysisResult) -> tuple[str, str]:
    """根據不同規則的加權總分回傳風險等級及解釋。

    0–1 分為 Low、2–5 分為 Medium、6 分以上為 High。
    多條不同規則會累加；同一規則無論出現幾次只計一次。
    """
    score = result.score
    if score >= 6:
        return "High", "累積分數至少 6，代表同時出現多種或多項明顯可疑特徵。"
    if score >= 2:
        return "Medium", "發現至少一項值得人工檢視的可疑文字特徵。"
    return "Low", "未發現足以達到中風險門檻的已知規則特徵。"
