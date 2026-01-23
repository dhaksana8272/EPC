class BranchClassifier:
    def __init__(self):
        self.branch_keywords = {
            "civil": [
                "concrete", "foundation", "beam", "column",
                "structural", "excavation", "slab", "reinforcement"
            ],
            "electrical": [
                "transformer", "cable", "switchgear",
                "substation", "earthing", "panel", "voltage"
            ],
            "mechanical": [
                "pump", "valve", "compressor",
                "turbine", "boiler", "pipeline", "hvac"
            ],
            "procurement": [
                "vendor", "purchase order", "rfq",
                "quotation", "delivery", "supply chain"
            ],
            "project_management": [
                "schedule", "timeline", "milestone",
                "risk", "planning", "progress", "delay"
            ]
        }

    def classify(self, text: str) -> str:
        text = text.lower()
        scores = {}

        for branch, keywords in self.branch_keywords.items():
            score = sum(1 for kw in keywords if kw in text)
            scores[branch] = score

        return max(scores, key=scores.get)