# Accessing the file
file = open('Coding.txt') #Default-ly read mode
print(file.read())
file.close

# Reading mode
r_mode = open('Coding.txt', 'r')
print(r_mode.read())
r_mode.close()

# Appending mode
a_mode = open('Coding.txt', 'a')
a_mode.write("Hi! I'm Penguin. And I am 1 y/o")
a_mode.close()

# Writing mode
w_mode = open('Coding.txt', 'w')
w_mode.write("Hi! I'm Penguin. And I am 1 y/o")
w_mode.close()