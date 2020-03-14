# Python Challenge
# PyBoss.py


import csv 
import datetime

# variables
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

empID = []
firstName = []
lastName = []
dateOfBirth = []
ssn = []
state = []

# open data file and grap save them
with open("employee_data.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header

    # loop through each row and save data to lists
    for row in reader:
        
        # employee id at column 1
        empID.append(row[0])

        # firstName and lastName at column 2
        names = row[1].split(" ")
        firstName.append(names[0])
        lastName.append(names[1])

        # date of birth at column 3
        nums = row[2].split("-")
        dob = datetime.datetime(int(nums[0]), int(nums[1]), int(nums[2]))
        dateOfBirth.append(dob.strftime('%m/%d/%Y'))

        # SSN at column 4
        ssn_tokens = row[3].split("-")
        ssn.append("***-**-" + ssn_tokens[2])

        # State at column 5
        state.append(us_state_abbrev[row[4]])

cleanData = zip(empID, firstName, lastName, dateOfBirth, ssn, state)

# write clean data to output file
with open("output.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Emp ID","First Name", "Last Name", "DOB", "SSN", "State"])
    writer.writerows(cleanData)
   
