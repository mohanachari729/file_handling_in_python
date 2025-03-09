# ## 'r'---->read operation
# file = open("sample.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()

# #readline()
# file = open("sample.txt",mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()

# #readlines()
# file = open("sample.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()


# # 'a' ----> write operation
# file = open("sample.txt",mode = 'a')
# write_data = file.write("\npython life is good platform for learning skills")
# print(write_data)
# file.close()

# ##'w' ---> write operation
# empty_data = ["mohan\n","phani"]
# file = open("sample.txt",mode = 'w')
# write_data = file.writelines(empty_data)
# file.close()

# # tell method and seek method by using '+w' operation
# file = open("sample.txt",mode = '+w')
# write_data = file.write("my name is mohan")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

# ## '+w' create a new file
# file = open("sample1.txt",mode = '+w')
# read_data = file.write('my name is mohan and i learn python in python life')
# write_data = file.read()
# print(write_data and read_data)
# file.close()

# ##  '+r' operation
# file = open("C:\\Users\\ma986\\OneDrive\\Desktop\\python.txt",mode = '+r')
# read_data = file.readlines()
# print(read_data)
# write_data = file.writelines("\n my name is mohanachari")
# print(write_data)
# file.close()


###creating a new  file on desktop
empty_file = ["mohan is the student of python life\n","he can be learn the python\n","python is teached venu sir"]
file = open("C:\\Users\\ma986\\OneDrive\\Desktop\\python1.txt", mode = 'a+')
# read_data = file.read()
# print(read_data)
write_data= file.writelines(empty_file)
print(write_data)
file.close()