class AppreciationMessage(Exception):
    def __init__(self, calories):
        self.message = f"Enjoy your meal with {calories}"
        super().__init__(self.message)