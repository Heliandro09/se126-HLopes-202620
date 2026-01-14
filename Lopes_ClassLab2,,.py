#Heliandro Lopes
#W2 In class LAb
#1/13/2026

#PROGRAM PROMPT
#Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#VARIABLE DICTIONARY:
#name            name of the room
#people          number of people attending
#max             maximum amount of people allowed in the room



#--IMPORTS--------------------------------------------------------
import csv 
#--FUNCTIONS------------------------------------------------------
def difference(people, max_cap) :
    '''this function is passed 2 values and returns the differnece between the'''
    diff = max_cap - people
    return diff
#--MAIN EXECUTING CODE---------------------------------------------

#intialize known or needed values (counting varibles!)
total_records = 0          #total records in file (1 room per record) -> 8
rooms_over = 0             #total number of rooms over capacity -> 3

print(f"\n\n{'ROOM NAME':20}   {'MAX':5}    {'PPL':5}   {'!REMOVE!':5}")
print("-" *50)
#connect to files
with open ("classLab2.csv") as csvfile: 
    #read text file data into 'file'
    file = csv.reader(csvfile)
    #process each 'record' in 'file' (for loop)
    for record in file:
        total_records += 1 

        #assign each firld of data to a variable 
        name = record [0]
        max = int(record[1])
        ppl = int(record[2])                #all file data is read in a string type

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        if remaining <0:
            rooms_over += 1
            print(f"{name:20}   {max:5}    {ppl:5} {-remaining:5}")
print("-" *50)
#disconnect from file

#display final values: total rooms counted, number of rooms over capacity 
print(f"\n\nROOMS OVER CAPACITY: {rooms_over}\nTOTAL ROOMS in FILE : {total_records}:")