#Program Contributers: Abhinay Arora,Allan Beldan
#This Program checks the Site suitability for a metro station based upon various factors such as Employment,Population,TripTime,PersonalTimeCost,Cost of trip and infrastructural Cost.

import math

##User Inputs##       Created by : Abhinay Arora
Print "---------------------------SITE SUITABILITY ANALYSIS FOR A METRO STATION---------------------------"
Print "---------------------------------------------------------------------------------------------------"
employment = raw_input("Employment Around The Station: ")
population = raw_input("Population of the City: ")
CBDEmployment = raw_input("")
triptime = raw_input("Time Consumed During Each Trip: ")
personaltimecost = raw_input("Cost of Personal Time(per hour): ")
tripcost = raw_input("Cost of Trip: ")
buildingcost = raw_input("Cost of Infrastructure: ")

e = math.e() #Initialize e as Euler's Numbeer

##Algorithim##  Created by : Allan Beldan
TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
OutputWeightedIndex=((population+employment)*abs((employment/population)+1)^-(e^-1))/(TripsExpected/buildingcost)
##Outputs##
Print ""

##Exceptions##
except Exception:
  print Exception
