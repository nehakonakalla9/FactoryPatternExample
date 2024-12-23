# course.py

from module import ExerciseModule, ConceptModule, IntroModule, SummaryModule, DemoModule

class Course:
    def __init__(self, name):
        self.name = name
        self.modules = self.create_modules()

    def create_modules(self):
        # In a real scenario, we might decide which modules to return based on the course type
        return [
            ExerciseModule(f"{self.name} Exercise"),
            ConceptModule(f"{self.name} Concept"),
            IntroModule(f"{self.name} Intro"),
            SummaryModule(f"{self.name} Summary"),
            DemoModule(f"{self.name} Demo")
        ]

    def display_modules(self):
        print(f"\nModules for {self.name}:")
        for module in self.modules:
            module.display()
