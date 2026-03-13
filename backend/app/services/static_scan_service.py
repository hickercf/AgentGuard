class StaticScanner:

    def __init__(self):

        self.danger_patterns = [

            "os.system",
            "subprocess",
            "eval(",
            "exec(",
            "pickle.loads",
            "rm -rf",
            "curl",
            "wget"

        ]

    def scan(self, code):

        findings = []

        for pattern in self.danger_patterns:

            if pattern in code:

                findings.append(
                    f"检测到危险函数: {pattern}"
                )

        return findings