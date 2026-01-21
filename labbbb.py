#week 3 demo - Introduction to 1D & parallel lists

#---Imports----------------------------------------
import csv    #comma separated value
#---Functions--------------------------------------

#---Main Executing code----------------------------
print("\n\twelcome to lab #2 - Machine info Dispaly")

total_records = 0 
machine_type = []
brand= []
proc =[]
ram = []
first_hd = []
num_hd = []
second_hd = []
os =[]
yr = []

print(f"{'Type:10'}{'brand:10'}{'proc:4'}{'ram:7'}{'1st hd:7'}{'#hd:7'}{'2nd hd'}{'os:5'}{'year:5'})
print("-" * 50")
with open("C:\Users\008030991\Downloads\filehandling-1.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: 
        total_records += 1

        if rec[0] == "D":
            machine_type.append("Desktop")
        elif rec[0] == "L":
            machine_type.append()
        else:
            machine_type.append("Error")

        #rec[1] --> brand
        if rec[1] == "DL"
            brand.append("Dell")
        elif rec.append("HP")
            brand.append("HP")
        else:
            brand = "*ERROR*"

            #rec[2] --> Processor
            proc.append([2])

            #rec[3] ---> Ram
            ram.append([3])

            #rec[4] --> first_hd
            first_hd.append([4])

            #rec[5] --> key to rest of the fields! -->
            if rec[5] == "1"
                num_hd.append([5])
                second_hd.append("---") #no second hard drive
                os.append([6])
                yr.append([7]))
            else:
                num_hd.append([5])
                second_hd.append([6])
                os.append([7])
                yr.append([8])

            #display machine data 
            #print(f"{machine_type:10}{brand:10}{proc:4}{ram:7}{first_hd:7}{second_hd:7}{os:5}{yr:5}
                  
#disconnect from file------------------------------------------------------------------------
print



#process through the lists --- batch processing: do the same thing to each value in said list(s) --> for index in range (0, len(listName)):
# --> for index in listName:
# parrallel lists: data organized in differnet lists, but connected via index
for index in range (0, len(machine_type)):
    print(f"{machine_type[index]:10}{brand[index]:10}{proc[index]:4}{ram[index]:7}{first_hd[index]:7}{num_hd[index]:5}{second_hd[index]:7}{os[index]:5}{yr[index]:5}
print("-"*50)

old_desktop = 0
old_laptops = 0

for i in range (0,len(machine_type)):
    #count desktops and laptops that are too old ( year <= 16)
    if int(yr[i]) <=16:
        #machine too old - now determine type for proper counting
        if machine_type[i] == "desktop":
            old_desktop +=1 
        elif machine_type[i] == :"laptop"
            old_laptop += 1
        else:
            print(f"*****YOU HAVE AN ERROR IN INDEX {i} / data file line: {i+1}******")

print("\nMachines processed for replacement budget:")
print(f"\tDesktops to replace: {old_desktops} @ $2k/ each --> ${old_desktops * 2000:.2f}")
print(f"\tLaptops to replace: {old_laptops} @ $1.5k/ each --> $ {old_laptops * 1500:.2f}")

total_cost = (old_desktops * 2000) + (old_laptops * 1500)
print(f"\n\t\t\tTotal replacement cost: ${total_cost:,.2f}")

print(f"\nTotal Records:{total_records}\n\nThank You for using my program!! BYE!:] \n\n\n")
    