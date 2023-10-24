print("yo what up bigshot this be ye olde GPA Calculator")
print("")
print("Some news just so you know")
print("Make sure in the grades.txt file that you have the courses abbreviated as such:")
print("Career Prep / College Prep: CP")
print("Honors: HR")
print("Advanced Placement: AP")
print("")
print("And in case you have no idea on what to do, lemme tell ya")
print("get a .txt file named grades, and fill it with your grades from all of your courses, in the format of |Course|: |Grade|")
print("Like so:")
print("CP A \nCP B \nHR C")
print("")
print("Then put the .txt file in the same folder as this python program, and just like that, it'll tell ya your GPA, simple as that!")
grades = []## alla this ^ is just the starting code to tell the user how to do stuff

try:##this whole chunka code is here to act as a failsafe incase of a lack of text file to read
  open("grades.txt")
except :
  print("")#prints this section in case of an error
  print("")
  print("Sorry, but it looks like there isn't a file named 'grades.txt'!")
  print("To fix this issue:")
  print("1. Make sure the file is named grades.txt")
  print("2. Make sure the file is in the same folder as the GPA calculator   file")
  print("3. Straight up just make sure the file exists in the first place, this program does not function without a grades.txt file to read from")
  exit()#shuts down program, just to clean up the output to not gunk it up with an error message
with open("grades.txt") as file:
  for i in file:
    grades.append(i)#this takes in all of the text files lines, and does it regardless of length, pretty nifty huh

file.close()#closes the file cause apparently leaving it open is a bad thing

print("")##how do you do automatic line spacing help me
print("")
print("")
print("Looks like your GPA from the submitted grades file will be:")
print("")
curstep = []
currentpoints = 0
for i in range(0,len(grades)):
  
  #this for loop iterates through each item in the grades list, which was defined earier before it was populated with the items from the .txt file
  
  curstep = grades[i]
  if(curstep[0:2] == "AP"):#as per Penn Manor Standards, AP courses get a full point more than CP courses
    currentpoints+=1
  if(curstep[0:2] == "HR"):#Honors courses only get 0.5 more though.
    currentpoints+=0.5
    #CP is not included as thats the baseline, and gets no course bonus.
  
  if(curstep[3] == "A"):#and from there we just add to the total points according to the grade, simple as!
    currentpoints+=4
  if(curstep[3] == "B"):
    currentpoints+=3
  if(curstep[3] == "C"):
    currentpoints+=2
  if(curstep[3] == "D"):
    currentpoints+=1

GPA = currentpoints/len(grades)#calculates total GPA as an average

print(GPA)
if(len(str(GPA)) > 4):#additional code for further readability so the person running ye olde code doesn't have to do any math at all to understand the gibberish this stuff can output.
  print("")
  print("Or, as it probably will be rounded to, ", round(GPA,2))
print("")
print("Currently, if you were an Honors Student you would be:")

if(GPA >= 3.75):
  print("passing!")
else:
  print("failing :(")
print("")
print("*Based on a 3.75 GPA Honors Graduation requirement")