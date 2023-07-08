n = int(input("Enter the number of students : "))
students = {}
for _ in range(n):
  line = input("Enter the name of student and their marks : ").split()
  name,scores = line[0],line[1:]
  scores = map(float,scores)
  students[name]=scores  
query_name = input("Enter the student name : ")
marks = 0
  
for i in students[query_name]:
  marks =marks+i
avg = float()
avg = marks/3
print("The percentage of student name : ","\n","_"*40)
print()
print("The average : ","%.2f"%avg)
