#Program Contributers: Abhinay Arora,Allan Beldan
#This Program checks the Site suitability for a metro station based upon various factors such as Employment,Population,TripTime,PersonalTimeCost,Cost of trip and infrastructural Cost.

import math

def questionchecker(question, upperrange, lowerrange): #introduces error checking at initial input, and gives user chance to enter new values if incorrect values are entered
  output = -1
  while output > upperrange or output < lowerrange:
    output = raw_input(question)
    numeric = output.numeric()
    if numeric == False:
      print("Error: Non-numeric value selected. Please try again")
    if output < upperrange or output >lowerrange:
      continue = raw_input("Warning: Value is outside of expected range of between " + lowerrange + " and " + upperrange + ". Errors may result. Continue? Y/N.")
      if continue.lower() == "n":
        output = -1
        print("Enter new value")
      else:
        print("Continuing with selected values. Errors may result.")

##Expected Values##    Created by: Allan Beldan
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

##User Inputs##       Created by : Abhinay Arora
Print "---------------------------SITE SUITABILITY ANALYSIS FOR A METRO STATION---------------------------"
Print "---------------------------------------------------------------------------------------------------"
employment = raw_input("Employment Around The Station: ")
population = raw_input("Population of the City: ")
CBDEmployment = raw_input("")
triptime = raw_input("Time Consumed During Each Trip: ")
personaltimecost = raw_input("Cost of Personal Time(per hour): ")
tripcost = raw_input("Cost of Trip, in US Dollars: ")
buildingcost = raw_input("Cost of Infrastructure, in US Dollars: ")

e = math.e() #Initialize e as Euler's Number

##Algorithim##  Created by : Allan Beldan
TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
OutputWeightedIndex=((population+employment)*abs((employment/population)+1)**-(e**-1))/(TripsExpected/buildingcost)

##Process outputs## Created by: Allan Beldan
if TripsExpected >= 1000:
  recommendtrips = True
else:
  recommendtrips = False
if OutputWeightedIndex >= 8000:
  recommendweight = True
else:
  recommendweight = False
##Outputs##
Print ""

##Exceptions##
except Exception:
  print Exception
