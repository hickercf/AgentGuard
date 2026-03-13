from app.services.llm_service import call_llm


def generate_fix(code):

    prompt = f"""
你是代码安全专家。

以下代码存在安全风险：

{code}

请给出：

1 安全修复代码
2 修改建议
"""

    result = call_llm(prompt)

    return result