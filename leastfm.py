def get_elements(lst):
  if  not lst:
    return "List is empty"
  first=lst[0]
  last=lst[-1]
  middle=lst[len(lst)//2]
  return first,middle,last
my_list=[10,20,30,40,50]
first,middle,last=get_elements(my_list)
print(f"first element:{first}")
print(f"middle element:{middle}")
print(f"last element:{last}")
