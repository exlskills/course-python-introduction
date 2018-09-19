import os

from pathlib import Path

unit_number = input('What Unit Number would you like to create? ')
print('\n','--'*50,'\n')
topic_name = input('What is the name of the topic you would like to create? ')
print('\n','--'*50,'\n')


if int(unit_number) < 10:
    unit_number = ''.join(['0',unit_number,'_'])
else:
    unit_number = ''.join([unit_number,'_'])
topic_name = ''.join([unit_number,topic_name])
os.mkdir(topic_name)


lecture_names = input('Please enter the names of the lectures, each serperated by a space: ')

for i,name in enumerate(lecture_names.split(' ')):
    if i <10:
        lecture_name = (''.join([str(0)+str(i)+'_',name[:]]))
    else:
        lecture_name = (''.join([str(i)+'_',name[:]]))
    file_path = ''.join([topic_name+'/'+lecture_name])
    os.mkdir(file_path)
    f2 = ''.join([file_path,'/index.md'])
    Path(f2).touch()

print('\n','--'*50,'\n')
print('Lectures created, check your working directory')
