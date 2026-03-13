from app.services.llm_service import call_llm

def analyze_legal(task):

    prompt = f"""
你是AI法律合规专家。

请分析以下任务是否存在法律风险。

任务：
{task}

规则：
1 如果没有法律风险，返回“未发现法律风险”
2 只分析明显风险
3 总字数不超过100字

输出JSON：

{{
"legal_risk": false,
"description": "",
"risk_level": "低"
}}
"""

    return call_llm(prompt)