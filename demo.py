#week 3 demo - Introduction to 1D & parallel lists

#---Imports----------------------------------------
import csv    #comma separated value
#---Functions--------------------------------------

#---Main Executing code----------------------------
print("\n\twelcome to lab #2 - Machine info Dispaly")

total_records = 0 

print(f"{'Type:10'}{'brand:10'}{'proc:4'}{'ram:7'}{'1st hd:7'}{'2nd_hd:7'}{'os:5'}{'year:5'})
print("-" * 50")
with open

with open("C:\Users\008030991\Downloads\filehandling-1.csv")

    file = csv.reader(csvfile)

    for rec in file: 
        total_records += 1

        if rec[0] == "D":
            machine_type = "Desktop"
        elif rec[0] == "L":
        else:
            machine_type = "Error"

        #rec[1] --> brand
        if rec[1] == "DL"
            brand= "Dell"
        elif rec[1] == "HP"
            brand == "HP"
        else:
            brand = "*ERROR*"

            #rec[2] --> Processor
            proc = rec [2]

            #rec[3] ---> Ram
            ram = rec[3]

            #rec[4] --> first_hd
            first_hd = rec [4]

            #rec[5] --> key to rest of the fields! -->
            if rec[5] == "1"
                num_hd = rec[5]
                second_hd = "---" #no second hard drive
                os = rec[6]
                yr = rec[7]
            else:
                num_hd = rec[5]
                second_hd = rec[6]
                os = rec[7]
                yr = rec[8]

            #display machine data 
            print(f"{machine_type:10}{brand:10}{proc:4}{ram:7}{first_hd:7}{second_hd:7}{os:5}{yr:5}
                  
#disconnect from file