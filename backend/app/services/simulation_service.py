class SimulationService:

    def simulate(self, task):

        steps = []

        steps.append("解析用户任务")

        if "download" in task.lower():
            steps.append("Agent下载外部资源")

        if "execute" in task.lower():
            steps.append("Agent执行系统命令")

        if "api" in task.lower():
            steps.append("Agent调用外部API")

        if "file" in task.lower():
            steps.append("Agent读取本地文件")

        return steps