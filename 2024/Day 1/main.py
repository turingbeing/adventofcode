from collections import Counter
# Read the Imput file and process it
def read_input_file(file_path):
  left_list = []
  right_list = []
  with open(file_path, 'r') as file:
    # Read the input from file and split it into two lists
    for line in file:
      left, right = map(int, line.strip().split())
      left_list.append(left)
      right_list.append(right)
  find_total_difference(left_list, right_list)
  find_similarities(left_list, right_list)
    
def find_total_difference(left_list, right_list):
  # Sort the lists
  left_list.sort()
  right_list.sort()

  # Calculate the total difference
  total_difference = 0
  for left, right in zip(left_list, right_list):
    # For each element in left and right list, calculate the difference and add it to the total difference
    difference = abs(left - right)
    total_difference += difference
    # print(f'Difference between {left} and {right}: {difference}')
    
  print(f'Total Records Read: {len(left_list)}\n\n')
  print(f'Total Difference is: {total_difference}')

def find_similarities(left_list, right_list):
  right_list_counter = Counter(right_list)
  similarity_score = 0

  for num in left_list:
    count_in_right_list = right_list_counter[num]
    similarity_score += num * count_in_right_list
    # print(f'Number {num} appears {count_in_right_list} times in the right list\n')
  print(f'Total Similarity Score: {similarity_score}')

# main function
def main():
  file_path = 'files/Input_A.txt'
  print(f'File path: {file_path} \n')
  read_input_file(file_path)

if __name__ == '__main__':
  main()