# Regular function
def remove_exclamation_marks(s):
    return s.replace('!', '')

print(remove_exclamation_marks("Hello World!"))

# Lambda function
remove_exclamation_marks_lambda = lambda s : s.replace('!', '')

print(remove_exclamation_marks_lambda("Hello World!"))
