# Traditional way to access file
# mode r(ead) and w(rite)
file = open('file.txt', mode='r')
# Read file
print(file.read())
# Close file
file.close()
# Check if file close
print(file.closed)

# Using the with so after function runs file closes
with open('file.txt', mode='r') as file:
    print(file.readLine())