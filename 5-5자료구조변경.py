# coffee shop
menu = {"coffee", "milk", "juice"}
print(menu, type(menu)) # {'juice', 'milk', 'coffee'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['juice', 'milk', 'coffee'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('milk', 'coffee', 'juice') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'juice', 'milk', 'coffee'} <class 'set'>