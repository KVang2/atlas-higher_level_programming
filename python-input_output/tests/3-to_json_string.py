# Json test

if __name__ == "__main__":
    my_list = [6, 12, 24]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))

# Test 2
    my_dict = {'id': 24, 'name': 'Nick', 'places': ["San Franciso", "Tokyo"],
    'is_active': True,
    'info': {
        'age': 28,
        'average': 88}}

# Test 3
    my_set = { 44, 22 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
