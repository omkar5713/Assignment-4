# Assignment 4 ,  Task 1

try:
        file = open('sample.txt','r')
        reading = file.read()
        print(reading)
        file.close()
except FileNotFoundError:
        print('Error: sample.txt file not found.')