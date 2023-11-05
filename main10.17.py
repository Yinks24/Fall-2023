# Solomon Falode 2154980
class ItemToPurchase:
    # the constructor 
    # 3 attributes 
    def __init__(self):
        # initialize the attributes 
        self.item_name="none"
        self.item_price=0
        self.item_quantity=0
        
    # the method print_item_cost() 
    # prints the cost 
    def print_item_cost(self):
        # print the output in the format 
        print(self.item_name,self.item_quantity,'@ $',end='')
        print(self.item_price,'= $',end='')
        
        # calculate the cost of the item 
        cost=self.item_price*self.item_quantity
        print(cost)
 
# main() 
# driver code 
if __name__=="__main__":
    # two objects are created         
    item1=ItemToPurchase()
    item2=ItemToPurchase()
    # take the input from the user 
    print('Item 1')
    item1.item_name=input('Enter the item name:\n')
    item1.item_price=int(input('Enter the item price:\n'))
    item1.item_quantity=int(input('Enter the item quantity:\n'))
    
    # for item 2 
    print('\nItem 2')
    item2.item_name=input('Enter the item name:\n')
    item2.item_price=int(input('Enter the item price:\n'))
    item2.item_quantity=int(input('Enter the item quantity:\n'))
    
    # print the costs 
    print('\nTOTAL COST')
    # call the method and print the cost 
    item1.print_item_cost()
    item2.print_item_cost()
    
    # print the total cost 
    print('\nTotal: $',end='')
    # for item1 and item2 
    total_cost=item1.item_price*item1.item_quantity+item2.item_price*item2.item_quantity
    print(total_cost)