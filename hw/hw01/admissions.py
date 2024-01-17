# Provided code
# This function checks to ensure that a list is of length
# 8 and that each element is type float
# Parameters:
# row - a list to check
# Returns True if the length of row is 8 and all elements are floats
def check_row_types(row):
    if len(row) != 8:
        print("Length incorrect! (should be 8): " + str(row))
        return False
    ind = 0
    while ind < len(row):
        if type(row[ind]) != float:
            print("Type of element incorrect: " + str(row[ind]) + " which is " + str(type(row[ind])))
            return False
        ind += 1
    return True


# converting rows to floats
def convert_row_type(work_row):
    line_data = []
    for item in work_row:
        line_data.append(float(item))
    return line_data


# calculating weighted score
def calculate_score(performance_data):
    return ((performance_data[0] / 160) * 0.3) + ((performance_data[1] * 2) * 0.4) + (
            (performance_data[2]) * 0.1) + ((performance_data[3]) * 0.2)


# checking for outliers (standardized GPA > standardized SAT or interest == 0)
def is_outlier(info):
    if info[2] == 0 or (2 * info[1] > (info[0] / 160) + 2):
        return True
    else:
        return False


# improved calculate score function. if true, it will write to better_improved.csv with all academic information
def calculate_score_improved(performance_data):
    score = ((performance_data[0] / 160) * 0.3) + ((performance_data[1] * 2) * 0.4) + (
            (performance_data[2]) * 0.1) + ((performance_data[3]) * 0.2)
    if score >= 6 or is_outlier(performance_data):
        return True
    else:
        return False


# checking for grade improvement for special cases
def grade_improvement(grades):
    if grades[0] <= grades[1] <= grades[2] <= grades[3]:
        return True
    else:
        return False


# checking for outlier semesters for special cases (use AFTER grade_improvement() bc semester_grades is now sorted)
def grade_outlier(grades2):
    def sort_list():
        grades2.sort(reverse=True)
        return grades2

    if (sort_list()[-2] - sort_list()[-1]) > 20:
        return True
    else:
        return False


# define your functions here


def main():
    filename = "admission_algorithms_dataset.csv"
    input_file = open(filename, "r")

    # opening files to write to
    scores_file = open("student_scores.csv", "w")
    chosen_file = open("chosen_students.csv", "w")
    outliers_file = open("outliers.csv", "w")
    improved_file = open("chosen_improved.csv", "w")
    better_file = open("better_improved.csv", "w")
    composite_file = open("composite_chosen.csv", "w")

    print("Processing " + filename + "...")
    # grab the line with the headers
    headers = input_file.readline()

    # loop to read in and process our data line-by-line
    for line in input_file:

        # cleaning up lines with .split()
        clean_line = line.split(",")

        # removing names to use later
        name = clean_line[0]
        del clean_line[0]

        # converting lines to floats
        float_line = convert_row_type(clean_line)

        # slicing list to use academic information separately from semester grades
        academics = float_line[:4]
        semester_grades = float_line[4:8]

        # calculating weighted score
        weighted_score = calculate_score(academics)

        # writing output to student_scores.csv
        output = f"{name},{weighted_score:.2f}\n"

        scores_file.write(output)

        # adding students with scores 6 or higher to chosen_students.csv
        if weighted_score >= 6:
            chosen_file.write(f"{name}\n")

        # adding outliers to outliers.csv
        if is_outlier(academics):
            outliers_file.write(f"{name}\n")

        # adding outliers and high-scorers to chosen_improved.csv
        if weighted_score >= 6 or (is_outlier(academics) and weighted_score >= 5):
            improved_file.write(f"{name}\n")

        # adding outliers and high-scorers to better_improved.csv with all academic information
        if calculate_score_improved(academics):
            better_file.write(f"{name},{academics[0]},{academics[1]},{academics[2]},{academics[3]}\n")

        # function checking for outliers, grade improvement, and semester grade outliers
        def special_case():
            if is_outlier(academics) or grade_improvement(semester_grades) or grade_outlier(semester_grades):
                return True
            else:
                return False

        # final write to composite_chosen.csv
        if (special_case() and weighted_score >= 5) or weighted_score >= 6:
            composite_file.write(f"{name}\n")

    # closing files
    scores_file.close()
    chosen_file.close()
    outliers_file.close()
    improved_file.close()
    better_file.close()
    composite_file.close()
    input_file.close()
    # TODO: loop through the rest of the file

    # TODO: make sure to close all files you've opened!

    print("done!")


# this bit allows us to both run the file as a program or load it as a
# module to just access the functions
if __name__ == "__main__":
    main()
