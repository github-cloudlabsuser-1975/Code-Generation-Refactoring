MAX = 100

def calculate_sum(arr):
   return sum(arr)

def get_number_of_elements():
   """
   Prompts the user to enter the number of elements within a specified range.

   Continuously asks for input until the user provides a valid integer between 1 and MAX (inclusive).
   Handles invalid input by displaying appropriate error messages.

   Returns:
      int: The number of elements entered by the user within the valid range.
   """
   while True:
      try:
         n = int(input(f"Enter the number of elements (1-{MAX}): "))
         if 1 <= n <= MAX:
            return n
         print(f"Invalid input. Please provide a number between 1 and {MAX}.")
      except ValueError:
         print("Invalid input. Please enter a valid integer.")

def get_elements(n):
   arr = []
   print(f"Enter {n} integers:")
   while len(arr) < n:
      try:
         num = int(input(f"Element {len(arr)+1}: "))
         arr.append(num)
      except ValueError:
         print("Invalid input. Please enter a valid integer.")
   return arr

def main():
   try:
      n = get_number_of_elements()
      arr = get_elements(n)
      total = calculate_sum(arr)
      print("Sum of the numbers:", total)
   except KeyboardInterrupt:
      print("\nProgram terminated by user.")

if __name__ == "__main__":
   main()
