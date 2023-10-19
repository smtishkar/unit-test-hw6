class NumsLists:
    def __init__(self, num_list1, num_list2):
        self.num_list1 = num_list1
        self.num_list2 = num_list2    


    def get_lists_averages(self,num_list):
        if len(num_list) > 0:
            avg_list = sum(num_list) / len(num_list)
            return avg_list
        else:
            return 0

    def compare_averages(self) -> None:
        avg1 = self.get_lists_averages(self.num_list1)
        avg2 = self.get_lists_averages(self.num_list2)
        if avg1 > avg2:
            return 'Первый список имеет большее среднее значение'
        elif avg1 < avg2:
            return 'Второй список имеет большее среднее значение'
        else:
            return 'Средние значения равны'


if __name__ == '__main__':
    lists = NumsLists([1,2,3,4,5],[2,3,4,5,6])
    avg1 = lists.get_lists_averages(lists.num_list1)
    avg2 = lists.get_lists_averages(lists.num_list2)
    
    print(f'{avg1} ------- {avg2}')
    lists.compare_averages()




    # lists = NumsLists([1,2,3,4,5],[2,3,4,5,6])
    # print(lists.get_lists_averages())