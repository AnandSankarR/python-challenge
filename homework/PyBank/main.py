import os
import csv
#open CSV File
csvpath = os.path.join('raw_data/budget_data_1.csv')
with open(csvpath) as csvfile:
    #Read and delimit the data
    csvreader=csv.reader(csvfile,delimiter=',')
    #Initialize Variable
    months=0
    revenue=0
    # Counts the Total Rows
    rows=[r for r in csvreader]
    #Defaulting to the First Value available in the Sheet
    change_revenue=int(rows[1][1])
    max = rows[1]
    min=rows[1]
    #Looping through Data
    for i in range(1,len(rows)):
        
        months=months+1
        row=rows[i]
        revenue= int(row[1]) + revenue
        
        #Excluding the Header Row
        if i > 1:
            change_revenue=change_revenue + int(row[1])-int(rows[i-1][1])
        #Finding and Max Revenue
        if int(max[1]) < int(row[1]):
            max=row
        #Finding and Min Revenue
        if int(min[1]) > int(row[1]):
            min=row
#Calculating Average and Average Change in Revenue
average= int(revenue /months)
average_change_revenue=int(change_revenue/months)

#Printing the Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total Revenue: " +"$" +str(revenue))       
print("Average Revenue Change: " +"$"+ str(average))
print("Average Change in Revenue Change: " +"$"+ str(average_change_revenue))
print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")

