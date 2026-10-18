# create a dictionary of student records,where key represents their roll nos and values 
# contains the name and marks in 3 subjects

d={}
n=int(input('Enter no of students: '))
for i in range (0,n):
  roll=int(input('Enter the roll no: '))
  name=input('Enter name: ')
  m1=int(input('Marks in sub 1: '))
  m2=int(input('Marks in sub 2: '))
  m3=int(input('Marks in sub 3: '))
  d[roll]={'name':name,'marks':[m1,m2,m3]}
print('Marks of all students')
max=0
m1=m2=m3=0
for r in d:
  total=sum(d[r]['marks'])
  print('Name: ',d[r]['name'],'\tMarks: ',d[r]['marks'],'\tTotal: ',total)
  if total>max:
    max=total
    details=d[r]
    name=d[r]['name']
    roll=r
  if d[r]['marks'][0]>m1:
    m1=d[r]['marks'][0]
    n1=d[r]['name']
  if d[r]['marks'][1]>m2:
    m2=d[r]['marks'][1]
    n2=d[r]['name']
  if d[r]['marks'][2]>m3:
    m3=d[r]['marks'][2]
    n3=d[r]['name']


print("Details of class topper: ")
print("Roll: ",roll,details)
print("Sub 1 topper",n1)
print("Sub 2 topper",n2)
print("Sub 3 topper",n3)