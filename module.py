# module.py

class Module:
    def __init__(self, name):
        self.name = name

    def display(self):
        pass

class ExerciseModule(Module):
    def display(self):
        print(f"{self.name} - Exercise Module")

class ConceptModule(Module):
    def display(self):
        print(f"{self.name} - Concept Module")

class IntroModule(Module):
    def display(self):
        print(f"{self.name} - Intro Module")

class SummaryModule(Module):
    def display(self):
        print(f"{self.name} - Summary Module")

class DemoModule(Module):
    def display(self):
        print(f"{self.name} - Demo Module")
