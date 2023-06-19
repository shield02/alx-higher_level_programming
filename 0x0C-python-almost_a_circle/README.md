## 0x0C. Python - Almost a circle

* models/base - Base class to be inherited by subsequent classes
* models/base - to_json_string - static method for JSON string serialization of dictionaries
* models/base - save_to_file - class method for writing JSON string representation of list of objects to file
* models/base - from_json_string - static method that returns list of JSON string representation
* models/base - create - create an instance of a class, use the update method to assign all attributes

* models/rectangle - Rectangle class to implement private instance/class variable with setters/getters
* models/rectangle - Updated the class to calculate the area
* models/rectangle - Added display method to print the rectangle using # character
* models/rectangle - Function to print string representation of the rectangle class
* models/rectangle - Updated the display method taking of x and y
* models/rectangle - Added update method that takes variable args and update the class
* models/rectangle - Added update method to take kwargs
* models/rectangle - Added to_dictionary method that prints a dictionary representation of the rectangle class

* models/square - Square class inheritting Rectangle class with constructor and `__str__` method
* models/square - Added public setter and getter for size
* models/square - Update method that assigns value to attributes
* models/square - Added to_dictionary method that prints a dictionary representation of the square class
