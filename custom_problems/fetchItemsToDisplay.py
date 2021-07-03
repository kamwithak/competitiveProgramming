def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
  starts = itemsPerPage*(pageNumber)
  ends = starts + itemsPerPage
  if(ends > len(items)):
    ends = len(items)
  
  pageitems = []

  for i in range(starts, ends):
    result = None ; ctr = 0
    for key in items.keys():
        if (i == ctr):
            result = key
        ctr += 1
    pageitems.append(result)
  
  return pageitems

print(fetchItemsToDisplay({"i1": [1, 2],"i2": [2, 1]},0,0,1,0))

# If u got the answer, please upvote. If you want to know anything please mention in the comment section