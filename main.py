sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {}
words = sentence.split()

#result = {new_key:new_value for item in list}
result = {word:len(word) for word in words}

print(result)


