class ThreatScorer:
    def __init__(self, distance_warning=500, distance_critical=200):
        self.warn = distance_warning
        self.crit = distance_critical

    def score(self, distance_m, speed_mps, heading_towards=True, size_px=0):
        score = 0
        if distance_m < self.crit: score += 50
        elif distance_m < self.warn: score += 25
        score += min(speed_mps * 2, 20)
        if heading_towards: score += 20
        score += min(size_px / 100, 10)
        level = "LOW"
        if score > 70: level = "CRITICAL"
        elif score > 40: level = "HIGH"
        elif score > 20: level = "MEDIUM"
        return {"score": round(score, 1), "level": level}
