#Let’s do a small loop to fill a dictionary — this is what you’ve been struggling with:
my_dict = {'car':'ford', 'job' : 'softwear_dev' , 'income' : '100k'}
new_dict= {}

my_dict['car'] = 'Aston Martin'

for key, value in my_dict.items():
    new_dict[key] = value
print(new_dict)