
--Emergent Design--
Start with a single class, and then extract out new classes when it seems like it is doing too much.

--Planned Design--
Design a multi-class system and then build it, updating your design as you learn where you were wrong at first.

# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────────────────────────────┐
│ Diary                                              │
│                                                    │
│ - __init__() ==> {}                                │
│                                                    │
│ - add(title,content) ==> {title: content}          │
│                                                    │
│ - read(title       ) ==> return {title1: content1} │
│               =None  ==> return {title1: content1} │
│                                 {title2: content2} │
│                                 {title3: content3} │
│                                        ...         │
│                                                    │
│ - find_best_entry_for_reading_time(wpm, minutes)   │
│                      ==> <previous code>           │
│                                                    │
│ - todo() ==> return ToDoList.incomplete()          │
│                                                    │
│ - list_mobiles() ==> return [<mobile number>       │
│                              <mobile number>       │
│                                    ...      ]      │
└────────────────────────────────────────────────────┘
                          ▲                           
                          │                           
                          │                           
┌─────────────────────────┴──────────────────────────┐
│ ToDoList                                           │
│                                                    │
│ - __init__() ==> []                                │
│                                                    │
│ - add(task)  ==> [].append({task: False})          │
│                                                    │
│ - mark_done(task) ==> {task: True}                 │
│                                                    │
│ - incomplete() ==> return [incomplete]             │
│ - complete()   ==> return [complete]               │
│                                                    │
│ - give_up() ==> {<all tasks>: True}                │
│                                                    │
└────────────────────────────────────────────────────┘

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
