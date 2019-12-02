#Program Contributers: Abhinay Arora,Allan Beldan,Ramon Boyce
#This Program checks the Site suitability for a metro station based upon various factors such as Employment,Population,TripTime,PersonalTimeCost,Cost of trip and infrastructural Cost.
from math import e
def questionchecker(question, upperrange, lowerrange): #introduces error checking at initial input, and gives user chance to enter new values if incorrect values are entered
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
personaltimecostlower = 10
personaltimecostupper = 50
tripcostlower = 0.5
tripcostupper = 5

##User Inputs##       Created by : Abhinay Arora
print "---------------------------SITE SUITABILITY ANALYSIS FOR A METRO STATION---------------------------"
print "---------------------------------------------------------------------------------------------------"
employment = questionchecker("Employment Around The Station: ",employmentupper,employmentlower)
population = questionchecker("Population of the City: ",populationupper,populationlower)
CBDEmployment = questionchecker("CBDEmployment",CBDEmploymentupper,CBDEmploymentlower)
triptime = questionchecker("Time Consumed During Each Trip: ",triptimeupper,triptimelower)
personaltimecost = questionchecker("Cost of Personal Time(per hour): ",personaltimecostupper, personaltimecostlower)
tripcost = questionchecker("Cost of Trip, in US Dollars: ",tripcostupper, tripcostlower)
buildingcost = questionchecker("Cost of Infrastructure, in US Dollars: ",buildingcostupper,buildingcostlower)

##Algorithim##  Created by : Allan Beldan
TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
OutputWeightedIndex=((population+employment)*abs((employment/population)+1)**-(e**-1))/(TripsExpected/buildingcost)

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

##Exceptions##
#==============================================================================
# while True:
#    try:
#      pop = int(input("Please the population density: "))
#      break
#      if pop < 0:
#          raise ValueError("Sorry, no values less than 0")
# 
# while True:
#     pop = input ("Please enter poulation density: ")
#     emp = input ("Please enter employment density: ")
#     try:
#         pop = int(pop)
#         emp = int(emp)
#         #raise ValueError("Non numeric value")
#     except :
#         print ('Non numeric data found.')
#         continue    
#     if pop > 150:
#       print( "Not a valid input for density")
#         # anything over150 density
#     else : 
#         print("Values accepted, proceed for output")
#==============================================================================
