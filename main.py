import utilities.calculator as calculator
import utilities.string_operation as string_operation 


sample_string = "Hello World"
reversed_string = string_operation.reverse_string(sample_string)
capitalized_string = string_operation.capitalize_string(sample_string)
lowercase_string = string_operation.lowercase_string(sample_string)
uppercase_string = string_operation.uppercase_string(sample_string)
print("Reversed String:", reversed_string)
print("Capitalized String:", capitalized_string)
print("Lowercase String:", lowercase_string)
print("Uppercase String:", uppercase_string)

a = 10
b = 5
sum_result = calculator.add(a, b)
difference_result = calculator.subtract(a, b)
product_result = calculator.multiply(a, b)
quotient_result = calculator.divide(a, b)
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)