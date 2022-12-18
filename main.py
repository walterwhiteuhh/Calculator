def scientific_calculator():
  # Print a welcome message
  print("Welcome to the scientific calculator!")
  
  # Loop until the user enters "q" to quit
  while True:
    # Get the user's input
    expression = input("Enter an expression (or 'q' to quit): ")
    
    # If the user wants to quit, break out of the loop
    if expression.lower() == "q":
      break
    
    # Try to evaluate the expression using Python's built-in eval function
    try:
      result = eval(expression)
      print(f"Result: {result}")
    except:
      print("Invalid expression. Please try again.")

# Call the calculator function to start the program
scientific_calculator()
