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


my_expression = r"(\w)\1.*(\w)\2"
print get_matching_words(my_expression)

Answers
python regex.py
['denver', 'obsessive', 'volleyball']

python regex.py
['denver', 'obsessive', 'volleyball']

$ python regex.py
['baseball', 'issue', 'mattress', 'obsessive', 'rabble', 'volleyball', '11234566']

r"ss"
python regex.py
['issue', 'mattress', 'obsessive']

r"^b"
python regex.py
['baby']

r"b.+b"
python regex.py
['baby', 'baseball']

r"a.*e.*i.*o.*u.*"
python regex.py
['facetious']

r"[aeiou][aeiou]$"
python regex.py
['issue', 'paranoia']

r"^[regular expressions]+$"
python regex.py
['issue', 'paranoia', 'union']

r"^[^regex]+$"
python regex.py
['baby', 'union', '11234566']

r"b.*b"
python regex.py
['baby', 'baseball', 'rabble']

r"b.?b"
python regex.py
['baby', 'rabble']

r"io"
python regex.py
['facetious', 'union']

r"e$"
python regex.py
['issue', 'obsessive', 'rabble']

r"(\w)\1.*(\w)\2"
python regex.py
['mattress', 'volleyball', '11234566']

