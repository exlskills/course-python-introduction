import os
from pathlib import Path

Exam_number = input('What number is the Final Exam in this unit?')

if int(Exam_number) < 10:
    Folder_Name = '0'+ Exam_number

Folder_Name = ''.join([Folder_Name ,'_','Final Exam'])
os.mkdir(Folder_Name)

Question_Number = input('How many questions would you like in this exam?')

for i in range(int(Question_Number)):
    if i < 10:
        name = '0'+str(i)
    else:
        name = str(i)
    name = name + '_Question'+ str(i)
    path = Folder_Name+'/'+name
    os.mkdir(path)
    file_name = path+'/index.prob.md'
    Path(file_name).touch()
    with open(file_name,'w') as f:
        f.write('>> Question Goes Here <<\n')
        f.write('() Answer 1\n')
        f.write('() Answer 2\n')
        f.write('() Answer 3\n')
        f.write('() Answer 4\n')
        f.write('|| Hint Goes Here ||')
        f.close()




# topic_name = input('What number question would you like to create')
#
# if int(topic_name) < 10:
#     topic_name = ''.join(['0',topic_name,'_Question ',topic_name])
# else:
#     topic_name = ''.join([topic_name,'_Question ',topic_name])
#
#
# os.mkdir(topic_name)
# f2 = ''.join([topic_name,'/index.prob.md'])
# Path(f2).touch()
