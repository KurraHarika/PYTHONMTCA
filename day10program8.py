fo1=open(r"D:\PythonPractice17\Day10\day10a.txt","r")
fo2=open(r"D:\PythonPractice17\Day10\test.txt","w+")

temp=fo1.read()
fo2.write(temp)


fo1.close()
fo2.close()
print("File Copied")
