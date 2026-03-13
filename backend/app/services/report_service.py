class ReportService:

    def generate(
        self,
        security,
        behavior,
        prompt,
        legal,
        static_scan,
        simulation,
        risk
    ):

        report = {

            "security_analysis": security,

            "behavior_analysis": behavior,

            "prompt_injection": prompt,

            "legal_analysis": legal,

            "static_scan": static_scan,

            "simulation": simulation,

            "risk_score": risk["risk_score"],

            "risk_level": risk["risk_level"]

        }

        return report