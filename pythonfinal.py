#Program Contributers: Abhinay Arora,Allan Beldan,Ramon Boyce
#This Program checks the Site suitability for a metro station based upon various factors such as Employment,Population,TripTime,PersonalTimeCost,Cost of trip and infrastructural Cost.

#Import Packages
from math import e
import csv

while True:
    try:
        ##Def Statements##      Created by : Allan Beldan
        def questionchecker(question, upperrange, lowerrange): #introduces error checking at initial input, and gives user chance to enter new values if incorrect values are entered
          while True:
              try:
                  output = -1
                  while output > upperrange or output < lowerrange:
                    output = raw_input(question)
                    outputuni = unicode(output, "utf-8")
                    numeric = outputuni.isnumeric()
                    if numeric == False:
                      print("Error: Non-numeric value selected. Please try again")
                    if output < upperrange or output >lowerrange:
                      continueyn = "purple"
                      while continueyn.lower() != "y" or continueyn.lower() != "n":
                        continueyn = raw_input("Warning: Value is outside of expected range of between " + str(lowerrange) + " and " + str(upperrange) + ". Errors may result. Continue? Y/N.")
                        if continueyn.lower() == "n":
                          output = -1
                          print("Enter new value")
                        elif continueyn.lower() == "y":
                          print("Continuing with selected values. Errors may result.")
                          return float(output)
                          break
                        else:
                          print"please select y or n"
              except ValueError:
                  print "Invalid data. Please try again"
                  
        ##Expected Values##    Created by : Allan Beldan
        employmentupper = 3000
        employmentlower = 1000
        populationupper = 10000
        populationlower = 1000
        CBDEmploymentupper = 5000000
        CBDEmploymentlower = 500000
        triptimeupper = 120
        triptimelower = 20
        buildingcostupper = 2000000000
        buildingcostlower = 500000000
        personaltimecostlower = 10
        personaltimecostupper = 50
        tripcostlower = 0.5
        tripcostupper = 5

##User Inputs##       Created by : Abhinay Arora
## Ask User if data is to be imported from CSV or entered manually
        datasource = ""
        while datasource.lower() != "c" or datasource.lower() != "m":
            datasource = raw_input("Would you like to import the data from a CSV or Manually type in each figure? C for CSV, M for Manually: ")
            if datasource.lower() == "m":


                print "---------------------------SITE SUITABILITY ANALYSIS FOR A METRO STATION---------------------------"
                print "---------------------------------------------------------------------------------------------------"
                employment = questionchecker("Employment Around The Station: ",employmentupper,employmentlower)
                population = questionchecker("Population Around The Station: ",populationupper,populationlower)
                CBDEmployment = questionchecker("Population and Employment at the Main Destination: ",CBDEmploymentupper,CBDEmploymentlower)
                triptime = questionchecker("Time Consumed During Each Trip: ",triptimeupper,triptimelower)
                personaltimecost = questionchecker("Cost of Personal Time(per hour): ",personaltimecostupper, personaltimecostlower)
                tripcost = questionchecker("Cost of Trip, in US Dollars: ",tripcostupper, tripcostlower)
                buildingcost = questionchecker("Cost of Infrastructure, in US Dollars: ",buildingcostupper,buildingcostlower)
                
                ##Algorithim##  Created by : Allan Beldan
                TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
                OutputWeightedIndex=((population+employment)*abs((employment/population)+1)**-(e**-1))/(TripsExpected/buildingcost)
            
            elif datasource.lower() == "c":
                try:
                    filelocation = raw_input("What is the location of the input file?")
                    if filelocation.endwith(".csv") == False:
                        filelocation =  filelocation + ".csv"
                    with open(filelocation) as csvfile:
                        reader = csv.DicReader(csvfile)
                        for row in csvfile:
                            employment = row['Employment']
                            population = row['Population']
                            CBDEmployment = row['CBDEmployment']
                            triptime = row['Trip Time']
                            personaltimecost = row['Personal Time Cost']
                            tripcost = row['Trip Cost']
                            buildingcost = row['Construction Cost']
                            ##Algorithim##  Created by : Allan Beldan
                            TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
                            OutputWeightedIndex=((population+employment)*abs((employment/population)+1)**-(e**-1))/(TripsExpected/buildingcost)
                except csv.Error:
                    print "Problem with input file"
                    print csv.Error
            
        ##Process outputs## Created by: Allan Beldan
        if TripsExpected >= 1000:
          recommendtrips = True
          print "This Site is suitable to build a metro station!"
        else:
          recommendtrips = False
        if OutputWeightedIndex >= 8000:
          recommendweight = True
        else:
          recommendweight = False
          
          
        ##Outputs##
        print recommendtrips
        print recommendweight
        
## Exceptions ##    Created by : Ramon Boyce
    except ValueError:
        print "Error: Non-numeric data detected. Please enter the data again"
        print ValueError
    except Exception:
        print "General Error: Program Failed"
        print Exception
          while True:
              try:
                  output < 0
                except ValueError
                print "Error, No negative values"
            
