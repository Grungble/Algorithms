from priq import Kpq

if __name__ == '__main__':
    my_values = [8,1,3,2,4,10,6]

    my_pq = Kpq()
    for value in my_values:
        my_pq.insert(value)

    print(my_pq)
    print(my_pq.peek())
    my_pq.delete(10)
    print(my_pq)
    print(my_pq.peek())

    print('----- doing dequeues')
    print(my_pq.sorter())
    for i in range(len(my_pq)):
        print(my_pq.dequeue())
        print(my_pq)