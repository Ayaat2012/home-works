#Program to open files in different ways

# Opening the file in read mode
file_read = open('Codingal.txt', 'r')
print("File in read mode")
print(file_read.read())
file_read.close()

# Opening the file in write mode
file_write = open('Codingal.txt', 'w')
# Writing in the file
file_write.write("File in write mode ....")
file_write.write("Hi! I'm Penguin. And I am 1 y/o")
file_write.close()

# Opening the file in append mode
file_append = open('Codingal.txt', 'a')
# Appending in the file
file_append.write("\n File in append mode ....")
file_append.write("Hi! I'm Penguin. And I am 1 y/o")
file_append.close()