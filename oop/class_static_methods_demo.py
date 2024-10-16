# class_static_methods_demo.py

class Calculator:
    calculation_type = "Calculation type: Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the calculation type."""
        print(cls.calculation_type)
        return a * b

# Example usage:
if __name__ == "__main__":
    sum_result = Calculator.add(5, 3)
    print(f"Sum: {sum_result}")

    product_result = Calculator.multiply(5, 3)
    print(f"Product: {product_result}")
