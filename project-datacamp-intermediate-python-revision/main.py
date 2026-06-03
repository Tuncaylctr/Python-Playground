# # Import the os module
# import os
# # Get the current working directory
# print("Current working directory:", os.getcwd())
# # Check the environment variables
# print("Environment variables:", os.environ)
# #change directory
# #os.chdir("the path")


# def clean_text(text, lower=True):
#     # Add a multi-line docstring
#     """
#     Clean text by swapping spaces to underscores and converting to lowercase.
    
#     Args:
#     	text (str): A string to be cleaned.
#     	lower (bool): Whether to convert the text to lowercase.
    
#     Detail the Returns:
#     	section: text (str): Cleaned string..
#     """
#     clean_text = text.replace(' ', '_')
#     if lower == False:
#         return clean_text
#     else:
#         return clean_text.lower()
      
# print(help(clean_text))
# print(clean_text.__doc__)

# # Define a function called concat
# def concat(*args):
#   """Concatenates multiple string arguments with spaces between them."""

#   result = ""

#   # Iterate over the Python args tuple
#   for arg in args:
#     result += " " + arg
#   return result

# # Call the function
# print(concat("Python", "is", "great!"))

# # Define a function called concat
# def concat(**kwargs):
#   """Concatenates keyword arguments into a single string with spaces."""
  
#   result = ""
  
#   # Iterate over the Python kwargs
#   for kwargs in kwargs.values():
#     result += " " + kwargs
#   return result

# # Call the function
# print(concat(start="Python", middle="is", end="great!"))
# file_size = 2500
# extra_space = 0.15

# # Call a lambda function in one line
# print((lambda x: x * (1 + extra_space))(file_size))
# colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# # Apply the lambda function to each colleague's name
# cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# # Convert map object to list
# cleaned_list = list(cleaned)
# print(cleaned_list)