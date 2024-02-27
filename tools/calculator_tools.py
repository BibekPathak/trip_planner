from langchain.tools import tool

class CalculatorTools():
    @tool("Make a calculation")
    def calculate(operation):
        """
        Evaluates a given mathematical operation expressed as a string and returns the result.
        If the operation is invalid, returns an error message.
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression."
