# python-CI

This is custome professional command line python application using `click` lib in python

#List all the commands:

`python main.py --help`

How to add a new -- todoList:

`python main.py add-todo`

`python main.py add-todo --name "Repaire Phone"`

`python main.py add-todo --name "Sell Ipad" --desc "Have to sell my iPad for a new one"`

`python main.py add-todo --name "Hospital" --desc "Going to see the doctor for my surgery" h` -- h for high priority.

List all the todoList commands:

`python main.py list-todos` -- List all todolist

`python main.py list-todos -p m` -- medium priority todolist

`python main.py list-todos -p h` -- high priority todolist

`python main.py list-todos -p c` -- crucial priority todolist

Delete todo

`python main.py delete_todo 3` -- delete todo with an index 3
