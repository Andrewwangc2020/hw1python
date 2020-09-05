#Author: Andrew Wang aqw5628@psu.edu

def letterToValue():
  if lettergrade == "A":
    return 4.0;
  elif lettergrade == "A-":
    return 3.67;
  elif lettergrade == "B+":
    return 3.33;
  elif lettergrade == "B":
    return 3.0;
  elif lettergrade == "B-":
    return 2.67;
  elif lettergrade == "C+":
    return 2.33;
  elif lettergrade == "C":
    return 2.0;
  elif lettergrade == "D":
    return 1.0;
  else:
    return 0.0;

weight = 0.0;
credits = 0.0;

lettergrade = input("Enter your course 1 letter grade: ");
l = letterToValue();
c = input("Enter your course 1 credit: ");
tempCredit = int(c);
weight += l * tempCredit;
credits += tempCredit;
print(f"Grade point for course 1 is: {l}");

lettergrade = input("Enter your course 2 letter grade: ");
l = letterToValue();
c = input("Enter your course 2 credit: ");
tempCredit = int(c);
weight += l * tempCredit;
credits += tempCredit;
print(f"Grade point for course 2 is: {l}");

lettergrade = input("Enter your course 3 letter grade: ");
l = letterToValue();
c = input("Enter your course 3 credit: ");
tempCredit = int(c);
weight += l * tempCredit;
credits += tempCredit;
print(f"Grade point for course 3 is: {l}");

gpa = weight/credits;
print(f"Your GPA is: {gpa}");