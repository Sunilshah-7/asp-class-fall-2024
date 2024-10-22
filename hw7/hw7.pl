% Define the structure for storing student grades
:- dynamic(student/7).

% Rule to calculate the final grade based on weights
final_grade(Name, FinalGrade):-
    student(Name, HW1, HW2, HW3, Midterm, FinalExam, Project),
    HWWeight is (HW1 + HW2 + HW3) / 3 * 0.2,
    ExamWeight is (Midterm + FinalExam) / 2 * 0.4,
    ProjectWeight is Project * 0.4,
    FinalGrade is HWWeight + ExamWeight + ProjectWeight.

% Rule to convert point grade to letter grades
letter_grade(FinalGrade, 'A') :- FinalGrade >= 90, FinalGrade =< 100.
letter_grade(FinalGrade, 'A-') :- FinalGrade >= 85, FinalGrade < 90.
letter_grade(FinalGrade, 'B+') :- FinalGrade >= 80, FinalGrade < 85.
letter_grade(FinalGrade, 'B') :- FinalGrade >= 75, FinalGrade < 80.
letter_grade(FinalGrade, 'B-') :- FinalGrade >= 70, FinalGrade < 75.
letter_grade(FinalGrade, 'C+') :- FinalGrade >= 65, FinalGrade < 70.
letter_grade(FinalGrade, 'C') :- FinalGrade >= 60, FinalGrade < 65.
letter_grade(FinalGrade, 'F') :- FinalGrade < 60.

% Rule to query letter grade by student name
student_letter_grade(Name, LetterGrade):-
    final_grade(Name, FinalGrade),
    letter_grade(FinalGrade, LetterGrade).

% Rule to query students by letter grade
students_with_letter_grade(LetterGrade, Students):-
    findall(Name, student_letter_grade(Name, LetterGrade), Students).

% Sample data
student('Marry Lou', 90, 90, 90, 90, 90, 90).
student('Tom Brown', 85, 85, 80, 80, 80, 80).
student('Nicole Scott', 90, 80, 78, 98, 76, 92).
student('Alex Green', 50, 50, 50, 50, 50, 50).

