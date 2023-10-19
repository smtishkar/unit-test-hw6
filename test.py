import unittest
from task1 import NumsLists


class TestNumLists(unittest.TestCase):

    def test_lists_compartision_second_list(self):
        lists = NumsLists([1,2,3,4,5],[2,3,4,5,6])
        self.assertEqual(lists.compare_averages(),'Второй список имеет большее среднее значение')

    def test_lists_compartision_first_list(self):
        lists = NumsLists([1,2,3,4,5, 20],[2,3,4,5,6])
        self.assertEqual(lists.compare_averages(),'Первый список имеет большее среднее значение')

    def test_lists_compartision_equal(self):
        lists = NumsLists([1,2,3,4,5],[1,2,3,4,5])
        self.assertEqual(lists.compare_averages(),'Средние значения равны')

    def test_average_calculation_list1(self):
        lists = NumsLists([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
        self.assertEqual(lists.get_lists_averages(lists.num_list1),3)

    def test_average_calculation_list2(self):
        lists = NumsLists([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
        self.assertEqual(lists.get_lists_averages(lists.num_list2),4)

    def test_average_calculation_list2_zero(self):
        lists = NumsLists([1, 2, 3, 4, 5], [])
        self.assertEqual(lists.get_lists_averages(lists.num_list2),0)

    def test_init(self):
        lists = NumsLists([1, 2, 3, 4, 5], [2, 3, 4, 5, 6])
        assert lists.num_list1 == [1, 2, 3, 4, 5]
        assert lists.num_list2 == [2, 3, 4, 5, 6]



if __name__ == "__main__":
    unittest.main(verbosity=2)