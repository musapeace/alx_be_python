def safe_divide(numerator, denominator):

  try:
    return float(numerator) / float(denominator)
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Invalid input. Please enter numbers."