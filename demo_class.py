print("demo_class.py loaded")

from course_factory import CourseFactory

class DemoClass:
    def __init__(self):
        self.factory = CourseFactory()

    def show_course_modules(self, course_type):
        course = self.factory.create_course(course_type)
        course.display_modules()