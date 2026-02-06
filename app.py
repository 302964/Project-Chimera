
---

# 3. CONVERTED TO FASTAPI (Production-Grade)

### `app.py`
```python
from fastapi import FastAPI
from agents.orchestrator import Orchestrator
from agents.trend_agent import TrendAgent
from agents.content_agent import ContentAgent
from agents.engagement_agent import EngagementAgent
from agents.analytics_agent import AnalyticsAgent

app = FastAPI(title="Project Chimera")

orch = Orchestrator(
    TrendAgent(),
    ContentAgent(),
    EngagementAgent(),
    AnalyticsAgent()
)

@app.post("/run-cycle")
def run_cycle():
    result = orch.run_cycle()
    return {"status": "success", "result": result}
