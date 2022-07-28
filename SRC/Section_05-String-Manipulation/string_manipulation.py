name = "animesh"
age = 41
# Standard message format
message = "Hello {} ({})".format(name, age)

# Change the argument order
message_2 = "Hello {1} ({0})".format(age, name)

# Kwargs
message_3 = "Hello {name} ({age})".format(name=name, age=age)

print(message)
print(message_2)
print(message_3)
