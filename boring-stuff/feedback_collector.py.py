"""
14/7/2022. this program validates
user inputs by using string methods.

"""

from logging import exception


def main():
    print("welcome to ffedback generator")
    list_item = inputs()
    outputs(list_item)

def inputs():

    print("please enter multiple feedback phrases each ending with a !")
    list_items = input("Enter as many as you like. you don't have to capitalize: ")#Collects user inputs.
    list_item = list_items.split('!')#converts user inputs into a list
    list_item.pop()#removes the extra empty space at the end
    return list_item

    

def outputs(list_item):
    index =0
    for i in list_item:
        index+= 1
        print(f'{index}: {str(i).strip()}!')
print("Thanks for helping us buld our library.")

main()