# FactoryPatternExample
Project Overview
This project demonstrates the Factory Design Pattern used to create different types of courses and modules for an online learning platform. The pattern abstracts the object creation logic from the client code, allowing the client to interact with the factory class without needing to know the details of how courses or modules are created.

Project Structure
demo_class.py: Contains the client code (DemoClass) that interacts with the factory.
course_factory.py: The factory class (CourseFactory) responsible for creating different courses.
course.py: Contains concrete classes representing different courses (Course1, Course2, etc.).
module.py: Contains the different types of modules that belong to each course (ExerciseModule, ConceptModule, etc.).
main.py: The entry point for running the program, showcasing how the factory method works.
How to Run the Project
Prerequisites
Ensure you have Python 3.x installed. You can download it from python.org.

Steps to Run the Code
Clone the repository or download the files to your local machine.
Open a terminal or command prompt.
Navigate to the directory where the project files are located.
Run the main.py file using Python:
bash
Copy code
python main.py
Expected Output
The program will demonstrate how the DemoClass interacts with the CourseFactory to get specific courses and their associated modules, such as exercises, concepts, intros, etc., all without the client code needing to know about the concrete class implementations.

Code Explanation
Factory Pattern: The CourseFactory class is responsible for instantiating the correct course object based on the type requested. The client class (DemoClass) only interacts with the factory and the course interface, without needing to know the details of how courses are instantiated or their modules are created.

Modules: Each course contains various modules like exercise, concept, intro, summary, and demo. These modules are created dynamically by the factory when requested.

Extending the Project
You can extend the project by adding new courses or modules. To add a new course:

Create a new concrete class that implements the Course interface.
Add a corresponding method in the CourseFactory class to handle the new course type.
Contributing
Feel free to fork the project and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on the repository.
