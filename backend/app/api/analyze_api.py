from fastapi import APIRouter

from app.models.analyze_model import AnalyzeRequest

from app.agents.security_agent import analyze_security
from app.agents.behavior_agent import analyze_behavior
from app.agents.prompt_injection_agent import detect_prompt_injection
from app.agents.legal_agent import analyze_legal

from app.services.static_scan_service import StaticScanner
from app.services.simulation_service import SimulationService
from app.services.risk_engine import calculate_risk
from app.services.report_service import ReportService

from app.database.crud import save_report

router = APIRouter(
    prefix="/api",
    tags=["analysis"]
)


@router.post("/analyze")
def analyze(data: AnalyzeRequest):

    security = analyze_security(data.code)

    behavior = analyze_behavior(data.task)

    prompt = detect_prompt_injection(data.task)

    legal = analyze_legal(data.task)

    scanner = StaticScanner()

    static_scan = scanner.scan(data.code)

    simulator = SimulationService()

    simulation = simulator.simulate(data.task)

    risk = calculate_risk(
        security,
        behavior,
        prompt,
        legal
    )

    report_service = ReportService()

    report = report_service.generate(
        security,
        behavior,
        prompt,
        legal,
        static_scan,
        simulation,
        risk
    )

    save_report(data.task, report)

    return report