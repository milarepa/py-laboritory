import math as m
grades = raw_input("Enter grades in  list[] form :")

def print_grades(grades):
  for grade in grades:
    print grade

def grades_sum(grades):
  total = 0
  for grade in grades: 
    total += grade
  return total
    
def grades_average(grades):
  sum_of_grades = grades_sum(grades)
  average = sum_of_grades / len(grades)
  return average

def grades_variance(grades, average):
  sum_of_differences = 0.0
  for i in grades:
    difference = (average - i) ** 2
    sum_of_differences += difference
  variance = sum_of_differences / len(grades)
  return variance

def grades_std_deviation(variance):
  return m.sqrt(variance)

average = grades_average(grades)
variance = grades_variance(grades, average)

print "Grade List :"
print print_grades(grades)
print "Sum :"
print grades_sum(grades)
print "Average :"
print grades_average(grades)
print "Variance :"
print grades_variance(grades, average)
print "Standard Deviation :"
print grades_std_deviation(variance)
