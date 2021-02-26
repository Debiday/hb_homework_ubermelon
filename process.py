log_file = open("um-server-01.txt")
#open the file


def sales_reports(log_file):
    #create a function to log the day's sales
    for line in log_file:
        #get each line in log_file
        line = line.rstrip()
        #get 3 characters in the line
        day = line[0:3]
        #determine the correct day from log_file
        if day == "Mon":
            print(line)

#call 'sales_reports' and pass in 'log_file'
sales_reports(log_file)
