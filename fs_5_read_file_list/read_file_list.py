def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    with open('/Users/stefaniedinhnguyen/Desktop/springboard/Software Engineer course/python3/Data Structures/python-ds-practice/fs_5_read_file_list') as f:
    for line in f: 
    line = line.strip()
        lines.append(line) 
    return f"- {line}"    

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!