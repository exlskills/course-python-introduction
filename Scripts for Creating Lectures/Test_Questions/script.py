import os
from pathlib import Path

Question_Number = input('What is the number of the Code Input Problem that you are building: ')

if int(Question_Number) < 10:
    Question_Number = ''.join(['0',Question_Number])

# Make the folder for the question
Folder_name = ''.join([Question_Number, '_Question', str(int(Question_Number))])
os.mkdir(Folder_name)

# Make the right folder structure
os.mkdir(Folder_name+'/code_input.prob.repl')
os.mkdir(Folder_name+'/code_input.prob.repl/src')
os.mkdir(Folder_name+'/code_input.prob.repl/test')
os.mkdir(Folder_name+'/code_input.prob.repl/tmpl')

# Make the Yaml file
Yaml_Path = Folder_name+'/index.prob.repl.yaml'
Path(Yaml_Path).touch()

with open(Yaml_Path,'w') as f:

    f.write('api_version: 1\n')
    f.write('environment: python_3_6_default_free\n')
    f.write('src_path: code_input.prob.repl/src\n')
    f.write('test_path: code_input.prob.repl/test\n')
    f.write('tmpl_path: code_input.prob.repl/tmpl\n')
    f.write('tests:\n')
    f.write('   junit:\n')
    f.write('       - "cd /workspace/src/main/java/exlcode/"\n')
    f.write('       - "javac OneDArrayLengthPracticeOne.java -d ."\n')

    f.write('display:\n')
    f.write('   height: 500px\n')
    f.close()

#Make the template for the user input
Question_name = input('What is the name of the question that you are creating: ')
Path(Folder_name+'/code_input.prob.repl/tmpl/'+Question_name+'.py').touch()
Path(Folder_name+'/code_input.prob.repl/test/'+Question_name+'_test.py').touch()
Path(Folder_name+'/code_input.prob.repl/src/'+Question_name+'_Solution.py').touch()


# Make the Question:
Question_md = Folder_name+'/00_Code Input.prob.md'
Path(Question_md).touch()
with open(Question_md,'w') as f:
    f.write('>> Question Goes Here <<\n')
    f.write('() Answer 1\n')
    f.write('() Answer 2\n')
    f.write('() Answer 3\n')
    f.write('() Answer 4\n')
    f.write("<<\n = #!exl::repl('index.prob.repl.yaml')\n")
    f.write('|| Hint Goes Here ||\n')

    f.close()
