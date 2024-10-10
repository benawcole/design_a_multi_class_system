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
    
    def list_mobiles(self, title):
        # Phone number format: 00000 000 000 OR 00000 000000 OR 00000000000
        # iterate through every char
        # CONTENT = SELF.ENTRIES[TITLE]
        i = 0
        while i < len(self.entries[title]):
            if "".join(self.entries[title].split())[i:i+11].isdigit():
                return "".join(self.entries[title].split())[i:i+5] + " " + "".join(self.entries[title].split())[i+5:i+11]
            i += 1
        return "No numbers found"