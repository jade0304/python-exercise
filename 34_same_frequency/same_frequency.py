def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
# my own result:
    count = {}
    count2 = {}

 
    for num in list(num1):
        count[num] = count.get(ltr, 0) + 1
        max_key = max(count.values()):
        for (key, val) in count.items():
            if val == max_key:
                num1_key = key

    for num2 in list(num2):
        count2[num2] = count2.get(ltr, 0) + 1
        max_key = max(count2.values()):
        for (key, val) in count2.items():
            if val == max_key:
                num2_key = key
    
    return if num1_key == num2_key



#create a func freq_counter()
# def freq_counter(coll):
#     """Returns frequency counter mapping of coll."""

#     counts = {}

#     for x in coll:
#         counts[x] = counts.get(x, 0) + 1

#     return counts

# def same_frequency(num1, num2):
#     return freq_counter(str(num1)) == freq_counter(str(num2))