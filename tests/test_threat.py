from src.threat_score import ThreatScorer

def test_critical_threat():
    s = ThreatScorer().score(150, 30, True, 500)
    assert s["level"] == "CRITICAL"

def test_low_threat():
    s = ThreatScorer().score(2000, 5, False, 10)
    assert s["level"] in ("LOW", "MEDIUM")
