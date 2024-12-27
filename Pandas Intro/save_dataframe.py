import pandas 


mydataset = {
    'languages': ["Python", "Java", "C++"],
    'popularity': [100, 99, 98]

}

myvar = pandas.DataFrame(mydataset)

print(myvar)