import pdfplumber
import re
import json
import os
# Path to your PDF file
pdf_path = "test.pdf"


# Search And Match Completed or Ongoig Courses from the PDF Based on the Pattern
pattern = r"\((\d{4}-\d{4}),\s*([A-Za-z]+)\)\s*\[([A-F][+-]?| - )\]"
pattern_2 = r"([A-Z]{3}\d{4})"
def completed():
    res= []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            lines = text.splitlines()
            for line in lines:
                if re.search(pattern,line):
                    res.append(line)
            lines = res
            res = []
            for line in lines:
                v = line.split()[0]
                if re.search(pattern_2,v):
                  res.append(v)
    return res
    
#Get the Unlocked Courses Based on the Complated or Ongoig Courses    
def getUnlocked(n) :
    completed_courses = completed()
    os.system('clear')
    data = []
    with open("CourseList.json", "r") as f:
        data = json.load(f)
    data = data[n]
    unlocked = []
    
    for code, (prereqs, course_name) in data.items():
        if prereqs != ["Nil"] and prereqs !=[]:
            
          if all(course in completed_courses for course in prereqs):
              if code not in completed_courses:
                unlocked.append(f"{code}: {course_name}")
    return unlocked


#Main Function    
def main():
    n = 0
    while True:
        n = int(input("Select Your program:\n       1) BSc in CSE\n       2)Bsc in EEE\n       4)BSc in BBA (Not Avilable)\n  Answer (Ex: BSc in CSE enter 1):"))
        if 0 < n < 3:
            break
        else: print("\nWrong Input! Try again...\n")
    for a in getUnlocked(str(n)):
        print(a)
    
#Calling Mian Function
main()

