from lib.ToDoList import *

def test_init_and_add_ToDo():
    list1 = ToDoList()
    assert list1.tasks == []
    list1.add("Wash the car")
    assert list1.tasks == [{"Wash the car": False}]
    list1.add("Clean your room")
    assert list1.tasks == [{"Wash the car": False}, {"Clean your room": False}]

def test_mark_done_and_complete():
    list2 = ToDoList()
    list2.add("Feed the cat")
    list2.add("Pay the bills")
    assert list2.incomplete() == ["Feed the cat", "Pay the bills"]
    list2.mark_done("Feed the cat")
    assert list2.complete() == ["Feed the cat"]
    assert list2.incomplete() == ["Pay the bills"]

def test_give_up():
    list3 = ToDoList()
    list3.add("Feed the cat")
    list3.add("Pay the bills")
    list3.add("Clean your room")
    list3.give_up()
    assert list3.incomplete() == []
    assert list3.complete() == ["Feed the cat", "Pay the bills", "Clean your room"]