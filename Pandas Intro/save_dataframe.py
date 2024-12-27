import pandas 


mydataset = {
    'languages': ["Python", "Java", "C++"],
    'popularity': [100, 99, 98]

}

myvar = pandas.DataFrame(mydataset)

print(myvar)



import pandas as pd

mydataset = {   
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)