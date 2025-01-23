from robust_division_calculator import safe_divide

if __name__ == "__main__":
  try:
    num1, num2 = map(float, input("Enter two numbers separated by a space: ").split( ))
    result = safe_divide(num1, num2)
    if isinstance(result, str):
      print(result)
    else:
      print(f"Result:{result}")
  except ValueError:
    print("Error: Please enter numeric values only.")