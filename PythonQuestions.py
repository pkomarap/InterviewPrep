# Combine 2 lists into a dictionary using zip()
# Two separate lists
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

# Convert to a single dictionary
result_dict = dict(zip(keys, values))

print(result_dict)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

################################################################################
# Sorts a list of words by their length
words = ["banana", "pie", "apple", "watermelon"]

# Sorts by length of the words (shortest to longest)
words.sort(key=len)

print(words)
# Output: ['pie', 'apple', 'banana', 'watermelon']

#################################################################################

# Sorts a list of words by their length using bubble sort algorithm
def sort_words_by_length(words_list):
    n = len(words_list)
    
    # Outer loop to traverse through all list elements
    for i in range(n):
        # Last i elements are already in place, no need to re-check them
        for j in range(0, n - i - 1):
            
            # Compare the LENGTHS of the adjacent words instead of alphabetical values
            if len(words_list[j]) > len(words_list[j + 1]):
                # Swap the elements if the current word is longer than the next word
                words_list[j], words_list[j + 1] = words_list[j + 1], words_list[j]
                
    return words_list

# Test Data
words = ["watermelon", "pie", "banana", "apple"]
print("Sorted list:", sort_words_by_length(words))

#################################################################################
# Removes duplicates from a string while preserving the order of characters
text = "programming"

# Removes duplicates while preserving order
unique_text = "".join(dict.fromkeys(text))

print(unique_text)
# Output: progamin

# Removes duplicates from a string while preserving the order of characters using a set
text = "programming"
seen = set()
result = ""

for char in text:
    if char not in seen:
        seen.add(char)
        result+= char

print(result)
# Output: progamin

##################################################################################
# Converts a binary string to a decimal number
binary_str = "1011"
decimal_num = 0

# Loop through the string and keep track of the power/index
for index, digit in enumerate(reversed(binary_str)):
    if digit == '1':
        decimal_num += 2 ** index

print(decimal_num)
# Output: 11

###################################################################################
# Converts a decimal number to a binary string

decimal_num = 11
binary_digits = ""

# Guard case for zero
if decimal_num == 0:
    binary_str = "0"
else:
    # Loop until the number hits 0
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits += str(remainder)
        decimal_num = decimal_num // 2  # Floor division

    # Reverse the remainders to get correct order
    binary_str = "".join(reversed(binary_digits))
    # binary_str = binary_digits[::-1]  # Alternatively, you can use slicing to reverse

print(binary_str)
# Output: 1011

#####################################################################################

# Finds all prime numbers between 2000 and 3000

prime_numbers = []

# Loop through the range from 2000 to 3000 inclusive
for num in range(2000, 3001):
    is_prime = True
    
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  # Found a factor, so it is not prime
            break             # Stop checking further
            
    # If no factors were found, add it to our list
    if is_prime:
        prime_numbers.append(num)

# Print the final list of prime numbers
print(prime_numbers)

#######################################################################################

# Decorator example to print the start and end of a function execution

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        func(*args, **kwargs)
        print(f"Ending {func.__name__}")
    return wrapper

@my_decorator
def sumoftwo(a,b):
    print(f"Sum={a+b}")

    
sumoftwo(2,3)
"""
OUTPUT:
===========
Starting sumoftwo
Sum=5
Ending sumoftwo
"""

########################################################################################

# Device Inventory Management System

devices = {"Router": 10, "Switch": 10, "Firewall": 10}

def inventory_management():

    req_r = int(input("Enter the number of Routers required: "))
    req_s = int(input("Enter the number of Switches required: "))
    req_f = int(input("Enter the number of Firewalls required: "))

    if req_r <= devices["Router"] and req_s <= devices["Switch"] and req_f <= devices["Firewall"]:
        devices["Router"] -= req_r
        devices["Switch"] -= req_s
        devices["Firewall"] -= req_f
        print("Devices allocated successfully.")
    else:
        print("Insufficient inventory for the requested devices.")

    print(f"Remaining Inventory: {devices}")


##########################################################################################

# Function to check if a given string is a palindrome
def is_palindrome_interview(text):
    clean_text = text.lower()
    left = 0
    right = len(clean_text) - 1
    
    while left < right:
        if clean_text[left] != clean_text[right]:
            return False  # Characters do not match, break early
        left += 1         # Move left pointer inward
        right -= 1        # Move right pointer inward
        
    return True

print(is_palindrome_interview("racecar")) # Output: True

##########################################################################

# Generate all possible IP addresses in the range

for octet1 in range(224, 240):
    # Loop through the second octet (0 to 255)
    for octet2 in range(256):
        # Loop through the third octet (0 to 255)
        for octet3 in range(256):
            # Loop through the fourth octet (0 to 255)
            for octet4 in range(256):
                # Print the IP address using string formatting
                print(f"{octet1}.{octet2}.{octet3}.{octet4}")


###########################################################################

import re
mactable = """
VLAN    MAC Address         Type             Ports
----               -----------          --------              -----
1001      00:11:22:33:44:55   DYNAMIC    Gi1/0/1
2020     aa:bb:cc:dd:ee:ff     DYNAMIC    Gi1/0/2
1002      66:77:88:99:aa:bb   STATIC         Gi1/0/3
1001      55:77:88:89:aa:bb   STATIC         Gi1/0/3
"""
def func_parser(text):
    lines = text.splitlines()
    exp_to_match=r'^([0-9]{4})\s*([0-9a-f:]+)\s*(DYNAMIC|STATIC)\s*([A-Za-z0-9/]+)$'
    for line in lines:
        match = re.search(exp_to_match, line)
        if match:
            print(f"VLAN ID: {match.group(1)}, MAC Address: {match.group(2)}, Type: {match.group(3)}, Port: {match.group(4)}")

        
func_parser(mactable)
"""OUTPUT
VLAN ID: 1001, MAC Address: 00:11:22:33:44:55, Type: DYNAMIC, Port: Gi1/0/1
VLAN ID: 2020, MAC Address: aa:bb:cc:dd:ee:ff, Type: DYNAMIC, Port: Gi1/0/2
VLAN ID: 1002, MAC Address: 66:77:88:99:aa:bb, Type: STATIC, Port: Gi1/0/3
VLAN ID: 1001, MAC Address: 55:77:88:89:aa:bb, Type: STATIC, Port: Gi1/0/3
"""


###########################################################################################

# Function to generate the next n IP addresses from a given starting IP address
def generate_next_ips(start_ip, n):
    # Split the IP string into 4 numeric octets manually
    octets = [int(x) for x in start_ip.split('.')]
    
    for _ in range(n):
        # Print the current state of the IP address
        print(f"{octets[0]}.{octets[1]}.{octets[2]}.{octets[3]}")
        
        # Increment the last octet
        octets[3] += 1
        
        # Handle the overflow math across all 4 IP segments
        if octets[3] == 256:
            octets[3] = 0
            octets[2] += 1
            
            if octets[2] == 256:
                octets[2] = 0
                octets[1] += 1
                
                if octets[1] == 256:
                    octets[1] = 0
                    octets[0] += 1
                    
                    if octets[0] == 256:
                        octets[0] = 0  # Hard reset if it hits 255.255.255.255

# --- User Input Execution ---
user_ip = input("Enter starting IP address (e.g., 192.168.1.254): ")
count = int(input("Enter number of IP addresses required: "))

print(f"\nThe next {count} IP addresses are:")
generate_next_ips(user_ip, count)

###############################################################################################
