# This program takes an input in temperature and wind speed and calculates wind chill
# Program then estimates the amount of time until frostbite will occur

# prompts for temperature and wind speed
temperature = input('Enter temperature in Fahrenheit: ')
windSpeed = input('Enter wind speed in mph: ')

# determines if temperature is a number
if temperature.isnumeric():
    temperature = float(temperature)
    # determines if temperature is greater than or equal to zero
    if temperature >= 0:
        # determines if the wind speed is a number
        if windSpeed.isnumeric():
            windSpeed = float(windSpeed)
            # determines if the wind speed is greater than or equal to zero
            if windSpeed >= 0:
                # calculates wind chill
                windChill = 35.74 + (0.6215 * temperature) - (35.75 * windSpeed ** 0.16) + (.4275 * temperature * windSpeed ** 0.16)
                # formats the wind chill
                formattedWindChill = format(windChill, '10.2f')
                # prints the wind chill
                print('Wind chill is', formattedWindChill, 'degrees Fahrenheit')
                # determines under what circumstances frostbite will occur and prints out a message
                if windChill <= -32:
                    print('Frostbite may occur in 10-30 minutes')
                else:
                    if windChill < -17:
                        print('Frostbite may occur in 30 minutes')
                    else:
                        print('Frostbite may occur in 30+ minutes')
            else:
                print(windSpeed, ' is not a valid value. Wind speed must be an integer >= 0.')
        else:
            print(windSpeed, ' is not a valid value. Wind speed must be an integer >= 0.')
    else:
        print(temperature, ' is not a valid value. Temperature must be an integer >= 0.')
else:
    print(temperature + ' is not a valid value. Temperature must be an integer >= 0.')
