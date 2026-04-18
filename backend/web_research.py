class WebResearch:
    def search(self, query):
        results = self._google_search(query)
        summary = self.get_wikipedia_summary(query)
        return results, summary

    def _google_search(self, query):
        # Placeholder for Google search implementation
        return ["result1", "result2", "result3"]  # Example results

    def get_wikipedia_summary(self, query):
        # Placeholder for Wikipedia summary retrieval
        return "Summary of the topic: {}".format(query)  # Example summary