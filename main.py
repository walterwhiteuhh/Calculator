import math
import tkinter as tk

class ScientificCalculator:
  def __init__(self, window):
    self.window = window
    self.window.title("Scientific Calculator")

    # Create the entry field
    self.entry = tk.Entry(window, width=30)
    self.entry.pack()

    # Create the calculate button
    self.calculate_button = tk.Button(window, text="Calculate", command=self.calculate_expression)
    self.calculate_button.pack()

    # Create the result label
    self.result_label = tk.Label(window, text="")
    self.result_label.pack()

  def calculate_expression(self):
    expression = self.entry.get()
    try:
      result = eval(expression, {"__builtins__": None}, {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan})
      self.result_label.config(text=f"Result: {result}")
    except:
      self.result_label.config(text="Invalid expression. Please try again.")

  def run(self):
    # Start the main loop
    self.window.mainloop()

if __name__ == "__main__":
  # Create the main window
  window = tk.Tk()

  # Create an instance of the ScientificCalculator class
  calculator = ScientificCalculator(window)

  # Run the calculator
  calculator.run()
