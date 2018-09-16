import unittest
from src.divis_by_2_Solution import divis_by_2_solution
from tmpl.divis_by_2 import divis_by_2

class LearningCase(unittest.TestCase):

    def test1(self):
        list_1 = [1,2,3,4,5,6]
        list_2 = [2,4,6,8]
        list_3 = [1,3,5,7]
        self.assertEqual(divis_by_2_solution(list_1), divis_by_2(list_1))
        self.assertEqual(divis_by_2_solution(list_2), divis_by_2(list_2))
        self.assertEqual(divis_by_2_solution(list_3), divis_by_2(list_3))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
