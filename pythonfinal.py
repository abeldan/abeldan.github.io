#Program Contributers: Abhinay Arora,Allan Beldan,Ramon Boyce,Navjot Kaur Sodhi
#This Program checks the Site suitability for a metro station based upon various factors such as Employment,Population,TripTime,PersonalTimeCost,Cost of trip and infrastructural Cost.

#Import Packages
from math import e
import csv
import sys

print "---------------------------SITE SUITABILITY ANALYSIS FOR A METRO STATION---------------------------"
print "---------------------------------------------------------------------------------------------------"

while True:
    try:
        while True:
            ##Def Statements##      Created by : Allan Beldan
            def questionchecker(question, upperrange, lowerrange): #introduces error checking at initial input, and gives user chance to enter new values if incorrect values are entered
             ## Exceptions##  Created by: Ramon Boyce
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
            
            ##Outputs## Created by Navjot K Sodhi
            def outputs(TripsExpected, OutputWeightedIndex, employment, population, CBDEmployment, triptime, personaltimecost, tripcost, buildingcost): ##Outputs## Created by: Navjot Kaur Singh
                if TripsExpected >= 1000:
                   recommendtrips = True
                else:
                    recommendtrips = False
                if OutputWeightedIndex >= 8000:
                    recommendweight = True
                else:
                    recommendweight = False
                
                print ""
                print ""
                print "Location statistics"
                print "Employment: " + str(employment)
                print "Population: " + str(population)
                print "Population and jobs at primary destination: " + str(CBDEmployment)
                print "Average trip time: " + str(triptime)
                print "Personal Time Cost: " + str(personaltimecost)
                print "Trip Fare Cost: " + str(tripcost)
                print "Construction Cost: " + str(buildingcost)
                print ""
                if recommendtrips == True:
                    print"Based on the number of projected trips of " + str(TripsExpected) + ", construction is recommended."
                else:
                    print"Based on the raw number of projected trips of " + str(TripsExpected) + ", construction is not recommended."
                if recommendweight == True:
                    print"Based on the weighted index of " + str(OutputWeightedIndex) + ", construction is recommended."
                else:
                    print"Based on the weighted index of " + str(OutputWeightedIndex) + ", construction is not recommended."
                if recommendtrips == True and recommendweight == True:
                    print "Since both measures recommend construction, construction is recommended"
                elif (recommendtrips == False and recommendweight == True) or (recommendtrips == True and recommendweight == False):
                    print "Since one index does not recommend construction, futher study is recommended"
                else:
                    print "Since both indexes do not recommend construction, construction is not recommended"
                      
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
                datasource = raw_input("Would you like to import the data from a CSV or Manually type in each figure, or Exit? C for CSV, M for Manually E for Exit: ")
                if datasource.lower() == "m":
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
                    
                    #Outputs
                    outputs(TripsExpected, OutputWeightedIndex)
                
                elif datasource.lower() == "c":
                    try:
                        filelocation = raw_input("What is the location of the input file?")
                        if filelocation.endswith(".csv") == False:
                            filelocation =  filelocation + ".csv"
                        if filelocation == 'd.csv': #Default Test Data location
                            filelocation = r"c:\Users\awbel\TestData.csv"
                        input_employment = []
                        input_population = []
                        input_CBDEmployment = []
                        input_triptime = []
                        input_personaltimecost = []
                        input_tripcost = []
                        input_buildingcost = []
                        with open(filelocation) as csvfile:
                            reader = csv.DictReader(csvfile) #CSV Reader and Processing lifted from Allan's Windspeed 3.0 file
                            for row in reader:
                                try:
                                    #Backup values
                                    input_employment_old = input_employment
                                    input_population_old = input_population
                                    input_CBDEmployment_old = input_CBDEmployment
                                    input_triptime_old = input_triptime
                                    input_personaltimecost_old = input_personaltimecost
                                    input_tripcost_old = input_tripcost
                                    input_buildingcost_old = input_buildingcost
                                    
                                    #append new values
                                    input_employment.append(int(row['Employment']))
                                    input_population.append(int(row['Population']))
                                    input_CBDEmployment.append(int(row['CentralBusinessDistrictPopEmployment']))
                                    input_triptime.append(int(row['TripTime']))
                                    input_personaltimecost.append(float(row['PersonalTimeCost']))
                                    input_tripcost.append(float(row['TripCost']))
                                    input_buildingcost.append(int(row['BuildingCost']))
                                    print("Data imported successfully")
                                except TypeError, err:
                                    print "Error in row " + str(row) + ". Skipping row"
                                    #Revert to old values in event of failure
                                    input_employment = input_employment_old
                                    input_population = input_population_old
                                    input_CBDEmployment = input_CBDEmployment_old
                                    input_triptime = input_triptime_old
                                    input_personaltimecost = input_personaltimecost_old
                                    input_tripcost = input_tripcost_old
                                    input_buildingcost = input_buildingcost_old
                                    print TypeError
                                except ValueError, err:
                                    print "Error in row " + str(row) + ". Skipping row"
                                    input_employment = input_employment_old
                                    input_population = input_population_old
                                    input_CBDEmployment = input_CBDEmployment_old
                                    input_triptime = input_triptime_old
                                    input_personaltimecost = input_personaltimecost_old
                                    input_tripcost = input_tripcost_old
                                    input_buildingcost = input_buildingcost_old        
                                    print ValueError
                                except Exception:
                                    print "Error in row " + str(row) + ". Skipping row"
                                    input_employment = input_employment_old
                                    input_population = input_population_old
                                    input_CBDEmployment = input_CBDEmployment_old
                                    input_triptime = input_triptime_old
                                    input_personaltimecost = input_personaltimecost_old
                                    input_tripcost = input_tripcost_old
                                    input_buildingcost = input_buildingcost_old
                                    print Exception
                            ##Algorithim##  Created by : Allan Beldan
                            for index in range(0, len(input_employment)):                                 
                                TripsExpected = ((input_population[index]+input_employment[index])*(input_CBDEmployment[index]))/((input_triptime[index]*input_personaltimecost[index])+input_tripcost[index])
                                OutputWeightedIndex=((input_population[index]+input_employment[index])*abs((input_employment[index]/input_population[index])+1)**-(e**-1))/(TripsExpected/input_buildingcost[index])
                                
                                #Run Outputs## Created by Navjot K Sodhi
                                outputs(TripsExpected, OutputWeightedIndex, input_employment[index], input_population[index], input_CBDEmployment[index], input_triptime[index], input_personaltimecost[index], input_tripcost[index], input_buildingcost[index])
                            
    
                    except csv.Error:
                        print "Problem with input file"
                        print csv.Error
                    except IndexError:
                        print "Reached end of list unexpectedly"
                        print IndexError
                elif datasource.lower() == "e":
                    sys.exit()
                else:
                    print "Invalid entry. Please try again"
    # Exceptions ##    Created by : Ramon Boyce
    except ValueError:
        print "Error: Non-numeric data detected. Please enter the data again"
        print ValueError
    except Exception:
        print "General Error: Program Failed"
        print Exception
