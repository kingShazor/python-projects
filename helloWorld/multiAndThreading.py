import threading
import multiprocessing

def print_list(list):
    for item in list:
        print(item)

# Thread - Test
print("Thread:")
list1 = [1,2,3,4]
list2 = [7,8,9]

thread1 = threading.Thread(target=print_list,args=(list1,))
thread2 = threading.Thread(target=print_list,args=(list2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Multiprocessing
print("Multiprocessing:")
if __name__ == "__main__":
    process1 = multiprocessing.Process(target=print_list,args=(list1,))
    process2 = multiprocessing.Process(target=print_list,args=(list2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
