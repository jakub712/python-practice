input =  ['hey', 'yo', 'cheerio']
# Output: {'hey': 3, 'yo': 2, 'cheerio': 7}

result = {}

for i in input:
    result[i] = len(i)
print(result)