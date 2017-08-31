print('Table displaying Celsius to Fahrenheit conversion:')
print("")							# creates a horizontal space
print('Celsius       Fahrenheit')	# gives column head name
print('--------     ------------')	# draws underline for column head
for Celsius in range(0,105,5):		# outputs number from 0 to 100 with interval of 5
    Farenheit = (9/5)*Celsius+32	# converts Celsius into Fahrenheit
    print(Celsius,'\t','\t', format(Farenheit, '.1f'))
