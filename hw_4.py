# Date: 02/25/2020
# Author : Sunil Shah
# Description: This is HW4 for CSCI 6221

# Implemention of Queue class with pushElement, popElement and count methods.
class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0
    def pushElement(self,element):
        self.queue = self.queue + [element]
        self.size += 1
        print("Element added to queue: ",element)
    def popElement(self):
        if self.size == 0:
            return False
        else:
            print("Head element removed from queue:", self.queue[0])
            self.queue = self.queue[1:]
            self.size -= 1
            return True
    def count(self):
        print("Number of elements in the queue: ", self.size)
    

# Main Screen
def main_menu():
    while True:
        print("#############################################")
        print("Enter the type of queue you want to create:")
        print("a. Integer")
        print("b. String")
        print("#############################################")

        # Sub Screen
        print()
        option = input("Enter your choice:")
        if option == 'a':
            print()
            print("We are creating Integer Queue.")
            
            q_integer = Queue()
            
            while True:
                print()
                print("----------------------------------")
                print("Choose among these 4 choices:")
                print("a. Push element into queue.")
                print("b. Pop element from queue.")
                print("c. Count number of elements in the queue.")
                print("d. Terminate the program.")
                print("----------------------------------")

                print()
                choice = input("Enter your choice:")
                if choice == 'a':
                    try:
                        element = int(input("Enter the element to push into queue:"))
                        q_integer.pushElement(element)
                        continue
                    except ValueError:
                        print("The wrong data type is entered.")
                        break

                elif choice == 'b':
                    if not q_integer.popElement():
                        print("There is no element in the queue.")
                        break

                elif choice == 'c':
                    q_integer.count()
                elif choice == 'd':
                    return
                else:
                    print("Invalid choice. Please choose from the given options.")
                    continue
        elif option == 'b':
            print()
            print("We are creating String Queue.")
            
            q_integer = Queue()
            
            while True:
                print()
                print("----------------------------------")

                print("Choose among these 4 choices:")
                print("a. Push element into queue.")
                print("b. Pop element from queue.")
                print("c. Count number of elements in the queue.")
                print("d. Terminate the program.")
                print("----------------------------------")

                print()
                choice = input("Enter your choice:")
                if choice == 'a':
                    element = input("Enter the element to push into queue:")
                    if element.isdigit():
                        print("The wrong data type is entered.")
                        break
                    q_integer.pushElement(element)
                elif choice == 'b':
                    if not q_integer.popElement():
                        print("There is no element in the queue.")
                        break
                elif choice == 'c':
                    q_integer.count()
                elif choice == 'd':
                    return
                else:
                    print("Invalid choice. Please choose from the given options.")
                    continue

main_menu()