# def find_high_scorers(score_list, passing_grade):
#     high_scorers = []
#     for current_score in score_list:
#         if current_score >= passing_grade:
#             high_scorers.append(current_score)

#     return high_scorers

# grades = [45, 82, 71, 49, 95, 60]
# required_minimum = 60
# final_results = find_high_scorers(grades, required_minimum)
# print("Studentw who passed: ", final_results)

# def find_high_scorers(score_list, passing_grade):
#     high_scorers = []
#     failures = []                                    # CHANGE 1
    
#     for current_score in score_list:
#         if current_score >= passing_grade:
#             high_scorers.append(current_score)
#         else:                                        # CHANGE 2
#             failures.append(current_score)           # CHANGE 3
    
#     return high_scorers, failures                    # CHANGE 4

# grades = [45, 82, 71, 49, 95, 60]
# required_minimum = 60
# final_results, failed_students = find_high_scorers(grades, required_minimum)   # CHANGE 5
# print("Students who passed: ", final_results)
# print("Students who failed: ", failed_students)      # CHANGE 6

# def find_high_scorers(score_list, passing_grade):
#     # Guard clauses - like input validation in C
#     if not isinstance(score_list, list):
#         raise TypeError("score_list must be a list")
#     if not isinstance(passing_grade, (int, float)):
#         raise TypeError("passing_grade must be a number")
#     if len(score_list) == 0:
#         raise ValueError("score_list is empty")

#     high_scorers = []
#     failures = []

#     for current_score in score_list:
#         if not isinstance(current_score, (int, float)):  # skip bad entries
#             raise TypeError(f"Invalid score found: {current_score}")
#         if current_score >= passing_grade:
#             high_scorers.append(current_score)
#         else:
#             failures.append(current_score)

#     return high_scorers, failures

# grades = [45, 82, 71, 49, 95, 60]
# required_minimum = 60
# final_results, failed_students = find_high_scorers(grades, required_minimum)   # CHANGE 5
# print("Students who passed: ", final_results)
# print("Students who failed: ", failed_students)      # CHANGE 6
