from course import Course

class CourseFactory:
    def create_course(self, course_type):
        if course_type == "course1":
            return Course("Course 1")
        elif course_type == "course2":
            return Course("Course 2")
        elif course_type == "course3":
            return Course("Course 3")
        else:
            raise ValueError("Invalid course type")