class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append({task: False})
    
    def mark_done(self, task):
        for dict in self.tasks:
            if list(dict.keys())[0] == task:
                dict[task] = True

    def incomplete(self):
        return [list(x.keys())[0] for x in self.tasks if not list(x.values())[0]]

    def complete(self):
        return [list(x.keys())[0] for x in self.tasks if list(x.values())[0]]

    def give_up(self):
        for dict in self.tasks:
            for task in dict:
                dict[task] = True