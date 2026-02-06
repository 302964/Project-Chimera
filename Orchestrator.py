class Orchestrator:
    def __init__(self, trend, content, engagement, analytics):
        self.trend = trend
        self.content = content
        self.engagement = engagement
        self.analytics = analytics

    def run_cycle(self):
        trends = self.trend.get_trends()
        post = self.content.generate(trends)
        engagement_data = self.engagement.simulate(post)
        self.analytics.record(engagement_data)
        return engagement_data
