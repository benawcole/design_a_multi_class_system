class Diary:
    def __init__(self):
        self.entries = {}
        self.lengths = {}
    
    def add(self, title, content):
        self.entries[title] = content
        self.lengths[title] = len(content.split())

    def read(self, title=None):
        if title == None:
            return self.entries
        return {title: self.entries[title]}
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        # if wpm*minutes is longer than all entries, return longest entry
        if wpm*minutes > list(self.lengths.values())[-1]:
            return {list(self.lengths.keys())[-1]: self.entries[list(self.lengths.keys())[-1]]}
        # if wpm*minutes is longer than entries[i] and shorter than entries[i+1], return entries[i] 
        i = 0
        while i < len(self.lengths.values()):
            if wpm*minutes == list(self.lengths.values())[i] or wpm*minutes > list(self.lengths.values())[i] and wpm*minutes < list(self.lengths.values())[i+1]:
                return {list(self.lengths.keys())[i]: self.entries[list(self.lengths.keys())[i]]}
            i += 1

    def todo(self, lst):
        return lst.incomplete()
    
    def list_mobiles(self, title=None):
        pass