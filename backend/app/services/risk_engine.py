def calculate_risk(security, behavior, prompt, legal):

    score = 0

    if "漏洞" in str(security):
        score += 30

    if "风险" in str(behavior):
        score += 20

    if "攻击" in str(prompt):
        score += 30

    if "违法" in str(legal):
        score += 20

    if score >= 70:
        level = "高危"
    elif score >= 40:
        level = "中危"
    else:
        level = "低危"

    return {
        "risk_score": score,
        "risk_level": level
    }