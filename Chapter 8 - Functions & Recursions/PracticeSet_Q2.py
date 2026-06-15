def CelsiusToFahrenheit(celsius):
  return (celsius * 1.8) + 32

num = int(input('Enter the temperature in celsius: '))

result = CelsiusToFahrenheit(num)
print(result)