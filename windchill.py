temp_c = float(input("Enter the temperature in celsius: "))
windspeed = float(input("Enter the windspeed (km/h): "))

# compute windchill
windchill = 13.12 + (0.6215*temp_c) - (11.37 * windspeed**0.16) + (0.3965 * temp_c * windspeed**0.16)

# output windchill
print("With the windchill factor, it feels like " + str(windchill) + "° outside.")

