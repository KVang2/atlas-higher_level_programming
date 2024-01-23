'''
# Json test

# Test case 1:
>>> to_json_string({"key": "value"})
'{"key": "value"}'

# Test 2: String
>>> to_json_string({})
'{}'

# Test 3:
my_list = [2, 4, 8]
print(type(my_list))
