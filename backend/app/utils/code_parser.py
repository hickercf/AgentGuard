import re


class CodeParser:

    def extract_functions(self, code):

        pattern = r"def\s+(\w+)\("

        return re.findall(pattern, code)


    def extract_imports(self, code):

        pattern = r"import\s+(\w+)"

        return re.findall(pattern, code)


    def find_system_calls(self, code):

        danger = []

        if "os.system" in code:
            danger.append("os.system")

        if "subprocess" in code:
            danger.append("subprocess")

        if "eval(" in code:
            danger.append("eval")

        return danger