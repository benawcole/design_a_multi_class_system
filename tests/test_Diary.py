from lib.Diary import *
from lib.ToDoList import *

def test_init_and_add_Diary():
    diary1 = Diary()
    assert diary1.entries == {}
    diary1.add("Monday", "You can fall apart")
    diary1.add("Tuesday", "Break my heart")
    assert diary1.entries ==   {
                                "Monday": "You can fall apart",
                                "Tuesday": "Break my heart"
                                }
    diary1.add("Thursday", "I don't care about you")
    diary1.add("Friday", "I'm in love")
    assert diary1.read("Thursday") ==   { 
                                        "Thursday": 
                                        "I don't care about you"
                                        }
    assert diary1.read() ==     {
                                "Monday": "You can fall apart",
                                "Tuesday": "Break my heart",
                                "Thursday": "I don't care about you",
                                "Friday": "I'm in love"
                                }

def test_lengths_and_best_entry():
    diary2 = Diary()
    diary2.add("Oct 1", "Went to Makers and worked hard")
    diary2.add("Oct 2", "Went to Makers, worked, and then ate a sandwich")
    diary2.add("Oct 3", "Went to Makers, worked, ate a sandwich, and completed a complex class")
    assert diary2.lengths ==   {"Oct 1": 6,
                                "Oct 2": 9,
                                "Oct 3": 12}
    assert diary2.find_best_entry_for_reading_time(3, 2) == {"Oct 1": "Went to Makers and worked hard"}
    assert diary2.find_best_entry_for_reading_time(2, 5) == {"Oct 2": "Went to Makers, worked, and then ate a sandwich"}
    assert diary2.find_best_entry_for_reading_time(3, 5) == {"Oct 3": "Went to Makers, worked, ate a sandwich, and completed a complex class"}

def test_todo():
    diary3 = Diary()
    list1 = ToDoList()
    list1.add("Feed the cat")
    list1.add("Pay the bills")
    list1.add("Clean your room")
    assert diary3.todo(list1) == ["Feed the cat", "Pay the bills", "Clean your room"]
    list1.mark_done("Feed the cat")
    assert diary3.todo(list1) == ["Pay the bills", "Clean your room"]