import statistics

class Grades:
    grades_list: list[float]
    grades_average: float
    grades_std_dev: float
    highest_grade: float
    lowest_grade: float

    def __init__(self, grades_list: list[float]) -> None:
        self.grades_list = grades_list.copy()

    def get_grades_average(self):
        self.grades_average = sum(self.grades_list) / len(self.grades_list)
        return self.grades_average
    
    def get_grades_std_dev(self):
        self.grades_std_dev = statistics.stdev(self.grades_list)
        return self.grades_std_dev
    
    def get_highest_grade(self):
        self.highest_grade = max(self.grades_list)
        return self.highest_grade

    def get_lowest_grade(self):
        self.lowest_grade = min(self.grades_list)
        return self.lowest_grade
        
