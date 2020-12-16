class Garden:
    student_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    plant_type = {'V': "Violets", 'C': "Clover", 'R': "Radishes", 'G': "Grass"}

    def __init__(self, diagram, students=student_list):
        self.diagram = [list(line) for line in diagram.split()] # "AA\nBB" -> [['A','A'],['B','B']]
        self.student_list = students
        self.student_list.sort()    # sort ascending

    def plants(self, students):
        student_num = self.student_list.index(students) # get student number for indexing pot location in diagram
        ## think more pythonic...
        pots = []
        for line in self.diagram:
            # line[2 * student_num:2 * (student_num + 1)]
            pots.append(Garden.plant_type.get(line[2*student_num]))
            pots.append(Garden.plant_type.get(line[2*student_num+1]))
        return pots