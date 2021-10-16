def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    rreturn [val for val in lst if val]


    #my other result: 
    # 
    #  new_lst = []
    # 
    # for list in lst:
    #     if list == True:
    #         new_lst.append(list)
    # 
    #     return new_lst        

