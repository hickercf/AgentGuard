from app.services.llm_service import call_llm


def analyze_security(code):

    prompt = f"""
你是AI代码安全审计专家。

请分析以下代码是否存在安全漏洞。

代码：
{code}

规则：
1 只分析真实存在的漏洞
2 如果没有漏洞，返回“未发现安全漏洞”
3 不要猜测不存在的攻击
4 总字数不超过100字

输出JSON：

{{
"vulnerabilities": [],
"summary": "",
"risk_score": 0
}}

风险评分规则：
0-20 无风险
20-40 低风险
40-60 中风险
60-80 高风险
80-100 严重风险
"""

    return call_llm(prompt)