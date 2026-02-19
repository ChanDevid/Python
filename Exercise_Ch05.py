# def sample_function():
#     """
#     A simple sample function that prints a message.
#     """
#     print("This is a sample function.")

# # Call the function to test it
# if __name__ == "__main__":
#     sample_function()

import random

# 1. Define a function called calculate_average
def calculate_average(grades):
    return sum(grades) / len(grades) if len(grades) > 0 else 0 