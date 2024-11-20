from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import List, Optional
app = FastAPI()

definitions = [
    {
        "term": "Syntax",
        "meaning": "Syntax refers to the rules that define the structure of a programming language. It specifies the correct combinations of symbols, such as keywords, identifiers, literals, and operators, to form a valid program or statement.",
    },
    {
        "term": "Data",
        "meaning": "Syntax refers to the rules that define the structure of a programming language. It specifies the correct combinations of symbols, such as keywords, identifiers, literals, and operators, to form a valid program or statement.",
    },
    {
        "term": "Variable",
        "meaning": "A variable is a named container that stores a piece of data (like a number, text, or other value) which can be changed throughout the program execution, essentially acting as a placeholder that can be assigned different values depending on the program's needs.",
    },
    {
        "term": "Datatype",
        "meaning": "A datatype refers to a classification of data that specifies what kind of value a variable canhold, defining the operations that can be performed on it and how the data is interpreted by the computer; Essentially telling the system how to store and manipulate information based on its type.",
        "example": "Examples include: Int, String, Boolean, etc."
    },
     {
        "term": "Operators",
        "meaning": "In computer science, an operator is a symbol that represents a specific mathematical, relational, or logical operation. Operators are used to manipulate values, perform calculations, and make decisions in programming languages.",
    },
     {
        "term": "Assignment Operators",
        "meaning": "Assign a value to a variable.",
        "example": "x = 10;"
    },    
    {
        "term": "Arithmetic Operators",
        "meaning": "Perform mathematical operations, such as addition (+), subtraction (-), multiplication (*), division (/), modulus (%), and exponentiation (^ or **).",
        "example": "a + b, x / y, b % c , etc."
    },    
    {
        "term": "Relational Operators",
        "meaning": "Compare values and return a boolean (true or false) result.",
        "example": """if (x > 5) { ... } 
				(checks if x is greater than 5)"""
    },
    {
        "term": "Logical Operators",
        "meaning": "Combine boolean values using AND (&&), OR (||), and NOT (!).",
        "example": """if (a && b) { ... }
				 (checks if both a and b are true)"""
    }, 
    {
        "term": "Bitwise Operators",
        "meaning": "Perform bitwise operations, such as AND (&), OR (|), XOR (^), and NOT (~).",
        "example": """a = 5; b = 3; c = a & b;
				(performs a bitwise AND operation on a and b, storing the result in c)"""
    },     
    {
        "term": "Conditional Operator",
        "meaning": "A shorthand for simple if-else statements",
        "example": """result = (x > 5) ? "greater" : "less"; 
				(evaluates x > 5 and assigns the corresponding string to result)"""
    },     
    {
        "term": "State",
        "meaning": "A state is a set of attributes or properties that describe an object’s characteristics",
    },     
    {
        "term": "Integer",
        "meaning": "a data type that represents whole numbers (positive, negative, or zero) without any decimal component.",
        "example": " 1, 1001, 56"
    },     
    {
        "term": "String",
        "meaning": "A string is a sequence of characters, such as letters, digits, or symbols, used to represent text or other types of data. Strings are signified with "" or ''. The quotes are interchangeable.",
        "example": "'bob, '1, 'jim'"
    },     
    {
        "term": "Function",
        "meaning": "A function is a self-contained block of code that performs a specific task. It takes one or more inputs (arguments) and produces a corresponding output. Functions provide modularity, reusability, and abstraction in programming.",
    },  



    {
        "term": "Python Syntax",
        "meaning": "The Python syntax defines a set of rules that are used to create a Python Program. The Python Programming Syntax has many similarities to Perl, C, and Java Programming Languages. However, there are some definite differences between the languages.",
    },
    {
        "term": "Indentation",
        "meaning": "Python uses whitespace (spaces or tabs) to denote block-level structure, such as defining scopes for loops and conditional statements.",
    },
    {
        "term": "Reserved Words",
        "meaning": "Python has a set of reserved words, also known as keywords, which have special meanings and cannot be used as variable or function names.",
        "example": "def, split, strip, words."
    },
    {
        "term": "Identifiers",
        "meaning": "Python identifiers, such as variable names, function names, and module names, consist of letters (both uppercase and lowercase), underscores, and digits. They cannot start with punctuation characters like @, $, or %.",
    },   
    {
        "term": "String Literals",
        "meaning": "Python supports two types of string literals: single quotes and double quotes for regular strings, and triple quotes for multiline strings or raw strings.",
    },    
    {
        "term": "Operators",
        "meaning": "Python has a range of operators for arithmetic, comparison, logical, assignment, and membership operations.",
    },    
    {
        "term": "PIP",
        "meaning": "PIP is a package manager for Python packages/modules.  A package contains all the files you need for a module and Modules are Python code libraries you can include in your project.",
    },    
    {
        "term": "Comments",
        "meaning": "Comments can be used to explain Python code, can be used to make the code more readable and can be used to prevent execution when testing code. Comments starts with a #, and Python will ignore them. Comments also can be placed at the end of a line, 	    and Python will ignore the rest of the line.",
        "example": "# this code is good!"
    },    
    {
        "term": "Python Variables",
        "meaning": "Comments can be used to explain Python code, can be used to make the code more readable and can be used to prevent execution when testing code. Comments starts with a #, and Python will ignore them. Comments also can be placed at the end of a line, and Python will ignore the rest of the line.",
    },    
    {
        "term": "Python Output Variables",
        "meaning": "Python has no command for declaring a variable; so, A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type, and can even change type after they have been set. Note, Python variables are case-sensitive.",
        "example": """
             x = 5
			 y = "John"
			 print(x)
 			 print(y)
             """
    },    
    {
        "term": "Dictionaries",
        "meaning": "A dictionary is a data structure that stores a collection of key-value pairs. Dictionaries are useful for storing and retrieving data efficiently, especially when the data has a natural correspondence between keys and values.",
        "example": "person_info = {'name': 'John', 'age': 30, 'city': ;New York'}"
    },    
    {
        "term": "Key",
        "meaning": "A key is a unique identifier used to access a value in a dictionary. A dictionary is a data structure that stores key-value pairs, where each key is associated with a specific value",
        "example": "'name': 'John', 'age': 30, 'city': 'New York'"
    },    
    {
        "term": "Sets",
        "meaning": "A set in Python is an unordered collection of unique elements. It is defined using curly braces or the set() function.",
        "example": "myset = {1, 2, 3, 4, 5}"
    },    
    {
        "term": " List",
        "meaning": "a list is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets [] and are ordered, meaning that the order of items matters.",
        "example": "fruits = ['apple', 'banana', 'cherry']"
    },
    {
        "term": "Return",
        "meaning": "A return statement is a programming construct that exits a function or subroutine and transfers control back to the calling code, optionally passing a value (also known as a return value) to the caller.",
        "example": """def x(a, b)

				 return x
                """
    },



    {
        "term": "HTML",
        "meaning": " HTML or (HyperText Markup Language) is the standard markup language used to create web pages, describing the structure of a webpage using elements and tags.",
        "example": ""
    },
    {
        "term": "Element",
        "meaning": "A building block of HTML that consists of a start tag, content, and an end tag.",
        "example": ""
    },    
    {
        "term": "Tag",
        "meaning": "A keyword enclosed in angle brackets that defines the start and end of an element.",
        "example": ""
    },    
    {
        "term": "Attribute",
        "meaning": "Additional information about an HTML element, included in the opening tag.",
        "example": ""
    },    
    {
        "term": "Headings",
        "meaning": "Elements used to define the structure of content, ranging from <h1> (most important) to <h6> (least important).",
        "example": ""
    },    
    {
        "term": "Paragraph",
        "meaning": "An element used to define a block of text.",
        "example": ""
    },    
    {
        "term": "Link",
        "meaning": "An anchor (<a>) element used to create hyperlinks to other web pages or resources.",
        "example": ""
    },    
    {
        "term": "Image",
        "meaning": "An element used to embed images in a webpage.",
        "example": ""
    },    
    {
        "term": "List",
        "meaning": "Elements that can be ordered (<ol>) or unordered (<ul>), containing list items (<li>).",
        "example": ""
    },    
    {
        "term": "Table",
        "meaning": "An element used to create a table, consisting of rows (<tr>) and cells (<td>).",
        "example": ""
    },    
    {
        "term": "Form",
        "meaning":"An element used to collect user input, which can include various input elements like text fields, checkboxes, and buttons.",
        "example": ""
    },    
    {
        "term": "Button",
        "meaning": "An element used to create clickable buttons.",
        "example": ""
    },    
    {
        "term": "Div",
        "meaning": "A block-level container used to group other elements for styling or layout purposes",
        "example": ""
    },    
    {
        "term": "Span",
        "meaning": "An inline container used to mark up a part of a text or a document.",
        "example": ""
    },    
    {
        "term": "Semantic Elements",
        "meaning": "Elements that clearly describe their meaning in a human- and machine-readable way, such as <header>, <footer>, <article>, etc.",
        "example": ""
    },   



    {
        "term": "Selector",
        "meaning": "A pattern used to select the elements you want to style.",
        "example": ""
    },
    {
        "term": "Property",
        "meaning": "A characteristic of an element that you can set a value for.",
        "example": ""
    },    
    {
        "term": "Value",
        "meaning": "The setting for a property.",
        "example": ""
    },    
    {
        "term": "Class Selector",
        "meaning": "A selector that targets elements with a specific class.",
        "example": ""
    },    
    {
        "term": "ID Selector",
        "meaning": "A selector that targets an element with a specific ID.",
        "example": ""
    },    
    {
        "term": "Universal Selector",
        "meaning": "Selects all elements in the document.",
        "example": ""
    },    
    {
        "term": "Box Model",
        "meaning": "A concept that describes the rectangular boxes generated for elements.",
        "example": ""
    },    
    {
        "term": "Flexbox",
        "meaning": "A layout model that provides a way to arrange items in a container.",
        "example": ""
    },    
    {
        "term": "Grid",
        "meaning": "A layout system that allows for two-dimensional layouts.",
        "example": ""
    },    
    {
        "term": "Pseudo-class",
        "meaning": "A keyword added to selectors that specifies a special state of the selected elements.",
        "example": ""
    },    
    {
        "term": "Pseudo-element",
        "meaning": "A keyword added to selectors that allows you to style a specific part of an element.",
        "example": ""
    },    
    {
        "term": "Media Query",
        "meaning": "A technique used to apply styles based on the viewport size or device characteristics.",
        "example": ""
    },    
    {
        "term": "Transition",
        "meaning": "A property that allows you to change property values smoothly (over a given duration).",
        "example": ""
    },    
    {
        "term": "keyframes",
        "meaning": "keyframes define the intermediate states of an animation, specifying the styles and properties that an element should have at specific points in time.",
        "example": ""
    },    
    {
        "term": "Overflow",
        "meaning": "A property that controls what happens when content overflows an element's box.",
        "example": ""
    },


    {
        "term": "JavaScript",
        "meaning": "JavaScript is a high-level, dynamic, and interpreted programming language that is primarily used for adding interactive and responsive elements to web pages. It is a scripting language that runs on the client-side (in the user’s web browser) or server-side (on a web server) to create dynamic web content, animate graphics, respond to user events, and update web pages in real-time.",
        "example": ""
    },
    {
        "term": "JSON",
        "meaning": "JSON or (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.",
        "example": ""
    },
    {
        "term": "Variable",
        "meaning": "A named storage location in memory that can hold a value, which can be changed during program execution.",
        "example": ""
    },   
    {
        "term": "Function",
        "meaning": "A block of reusable code designed to perform a particular task, which can be invoked or called with parameters.",
        "example": ""
    },   
    {
        "term": "Object",
        "meaning": "A collection of key-value pairs, where keys are strings (or Symbols) and values can be any data type, including other objects.",
        "example": ""
    },    
    {
        "term": "Array",
        "meaning": "A special type of object used to store ordered collections of values, which can be accessed by their index.",
        "example": ""
    },    
    {
        "term": "Event",
        "meaning": "An action or occurrence that can be detected by the program, such as user interactions (clicks, key presses) or system-generated events.",
        "example": ""
    },    
    {
        "term": "Callback",
        "meaning": "A function passed as an argument to another function, which is executed after a certain event or condition is met.",
        "example": ""
    },    
    {
        "term": "Promise",
        "meaning": "An object representing the eventual completion (or failure) of an asynchronous operation, allowing for cleaner handling of asynchronous code.",
        "example": ""
    },    
    {
        "term": "Asynchronous",
        "meaning": "A programming model that allows operations to run in the background, enabling the program to continue executing without waiting for the operation to complete.",
        "example": ""
    },    
    {
        "term": "Closure",
        "meaning": "A function that retains access to its lexical scope, even when the function is executed outside that scope.",
        "example": ""
    },    
    {
        "term": "Scope",
        "meaning": "The context in which variables and functions are accessible, determining their visibility and lifetime.",
        "example": ""
    },    
    {
        "term": "This",
        "meaning": "A keyword that refers to the context in which a function is executed, which can vary depending on how the function is called.",
        "example": ""
    },    
    {
        "term": "Module",
        "meaning": "A self-contained piece of code that encapsulates functionality and can be imported and exported between different files or components.",
        "example": ""
    },    
    {
        "term": "DOM",
        "meaning": "DOM or (Document Object Model) is a programming interface for web documents that represents the structure of a document as a tree of objects, allowing for dynamic manipulation of the content and structure of web pages.",
        "example": ""
    },
]

# Pydantic model to structure the data
class Definitions(BaseModel):
    term: str
    meaning: str
    example: str

# Endpoint to retrieve specific information by term and field
@app.get("/definitions/{term}/{field}")
async def get_field_by_term(term: str, field: str):
    valid_fields = {"term", "meaning","example"}  # Define valid fields
    if field not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field '{field}'. Valid fields are: {valid_fields}")
    
    for definition in definitions:
        if definition["term"].lower() == term.lower():
            return definition.get(field)  # Return the requested field
    
    raise HTTPException(status_code=404, detail=f"Term '{term}' not found")

# Endpoint to retrieve specific information by definition
@app.get("/definitions/{term}", response_model=Definitions)
async def get_definition_by_term(term: str):
    for definition in definitions:
        if definition["term"].lower() == term.lower():
            return definition
    raise HTTPException(status_code=404, detail=f"Term '{term}' not found")

# Endpoint to allow search with query params
@app.get("/search?query=variable")
async def search_definitions(query: Optional[str] = None):
    if query:
        results = [defn for defn in definitions if query.lower() in defn["term"].lower()]
        return results
    return definitions