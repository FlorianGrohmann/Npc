class Memory:
    def __init__(self):
        self.events = []

    def remember(self, event: str):
        self.events.append(event)

    def get_memory(self) -> list:
        return self.events
