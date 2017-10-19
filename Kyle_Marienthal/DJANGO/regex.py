import re
def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
        "11234566",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)
    return results


# my_expression = r"(\w)\1"
# returns ['baseball', 'issue', 'mattress', 'obsessive', 'rabble', 'volleyball', '11234566']

# my_expression = r"ss"
# returns ['issue', 'mattress', 'obsessive']

# my_expression = r"b.b"
# returns ['baby']

# my_expression = r"b.+b"
# returns =  ['baby', 'baseball']

# my_expression = r"a.*e.*i.*o.*u"
# returns ['facetious']

# my_expression = r"[aeiou]{2}$"
# returns ['issue', 'paranoia']

# my_expression = r"^[regularexpressions]*$"
# starts with and ends with 0 or more of any of those letters in the list.
# returns ['issue', 'paranoia', 'union']

# my_expression = r"^[^regex]*$"
# returns ['baby', 'union', '11234566']


# my_expression = r"b.*b"
# returns ['baby', 'baseball', 'rabble']

# my_expression = r"b.?b"
# returns ['baby', 'rabble']

# my_expression = r"io"
# returns ['facetious', 'union']

# my_expression = r"e$"
# returns ['issue', 'obsessive', 'rabble']

my_expression = r"(\w\1).*(\w\2)"


print get_matching_words(my_expression)
