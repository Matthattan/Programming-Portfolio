from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)

item1 = Item("MyItem", 750)

# set an attribute
item1.name = "OtherItem"

# get attribute
print(item1.name)
