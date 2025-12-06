country_code = {'india' : "0091",
                'australia' : "0025",
                'nepal' : "00977"}
print("country code for india - ")
print(country_code.get('india', 'not found'))
print("country code for japan - ")
print(country_code.get('japan', 'not found'))