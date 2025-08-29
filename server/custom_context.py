class CustomContext():
    """
    Custom context class to store multiple objects.
    """
    def __init__(self):
        self.context = {}

    def set_context(self, key, value):
        self.context[key] = value
    def get_context(self, key) -> object:
        return self.context.get(key, None)
    def get_all_context(self):
        del self.context
    def clear_all(self):
        self.context = {}
