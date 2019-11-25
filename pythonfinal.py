import math

##User Inputs
employment = raw_input("")
population = raw_input("")
CBDEmployment = raw_input("")
triptime = raw_input("")
personaltimecost = raw_input("")
tripcost = raw_input("")
buildingcost = raw_input("")

e = math.e()

##Algorithim
TripsExpected = ((population+employment)*(CBDEmployment))/((triptime*personaltimecost)+tripcost)
OutputWeightedIndex=((population+employment)*abs((employment/population)+1)^-(e^-1))/(TripsExpected/buildingcost)

##Outputs

##Exceptions