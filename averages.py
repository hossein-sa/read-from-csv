import csv
from statistics import mean

"""
    This function reads a CSV file containing student grades, calculates
    the average grades for each student, stores them in a dictionary, and
    returns the dictionary and the name of the student with the lowest average grade.
"""


def calculate_averages(grades_file):
    # Dictionary to store the average grades of each student
    student_averages = {}
    # Variable to track the lowest average grade, initialized with a high value
    lowest_average = float('inf')
    # Variable to track the name of the student with the lowest average grade
    lowest_student = None

    # Open the CSV file for reading
    with open(grades_file, newline='') as f:
        reader = csv.reader(f)  # Create a CSV reader object to iterate over the file
        for row in reader:  # Iterate over each row in the CSV file
            name = row[0]  # The first column is the student's name
            # Convert the rest of the columns to integers representing the grades
            grades = [int(grade) for grade in row[1:]]  # List comprehension for grades
            # Calculate the average grade for the student
            average = mean(grades)

            # Store the calculated average in the dictionary
            student_averages[name] = average

            # Check if the current student's average is lower than the lowest recorded average
            if average < lowest_average:
                lowest_average = average  # Update the lowest average
                lowest_student = name  # Update the name of the student with the lowest average

    # Return the dictionary of student averages and the name of the student with the lowest average
    return student_averages, lowest_student


if __name__ == "__main__":
    grades_file = 'grades.csv'  # The name of the CSV file containing the grades
    # Call the function to calculate averages and get the student with the lowest average
    student_averages, lowest_student = calculate_averages(grades_file)

    # Sort the dictionary of averages by average grade in ascending order
    sorted_averages = dict(sorted(student_averages.items(), key=lambda item: item[1]))

    # Print the name of the student with the lowest average
    print(f"Student with the lowest average: {lowest_student}")

    # Iterate over the sorted dictionary and print each student's name and their average grade
    for student_name, student_average in sorted_averages.items():
        print(f"Average for {student_name}: {student_average:.2f}")  # Format the average to 2 decimal places
