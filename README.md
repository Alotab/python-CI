# TodoList CLI Application

This is a custom, professional command-line To-Do List application built with Python using the `click` library. The application allows users to manage their to-dos through a set of simple commands, all of which interact with a `todolist.txt` file for data storage.

## Features

- Add a new to-do with a name, description, and priority.
- List all to-dos with different priority filters (high, medium, crucial).
- Delete a to-do by its index in the list.
- Built using the powerful and easy-to-use `click` Python library for CLI interfaces.

## Installation

1. Clone or download the repository.
2. Install the required dependencies via pip:
   `pip install click`

# Usage

## List All Commands

`python main.py --help`

## Add a New To-Do:

To add a new to-do, use the add-todo command. You can optionally specify a description and priority

`python main.py add-todo`

`python main.py add-todo --name "Repaire Phone"`

`python main.py add-todo --name "Sell Ipad" --desc "Have to sell my iPad for a new one"`

`python main.py add-todo --name "Hospital" --desc "Going to see the doctor for my surgery" h` -- h for high priority.

## List All To-Dos:

To list all to-dos, use the `list-todos` command. You can filter the list based on priority:

List all to-dos --

`python main.py list-todos`

List medium priority to-dos --

`python main.py list-todos -p m`

List high priority to-dos --

`python main.py list-todos -p h`

List crucial priority to-dos --

`python main.py list-todos -p c`

## Delete a To-Do

To delete a to-do, use the delete-todo command, followed by the index of the to-do you want to delete:

Delete the to-do at index 3 --

```

python main.py delete_todo 3

```

## Command Summary

| Command               | Description                             |
| --------------------- | --------------------------------------- |
| `add-todo`            | Add a new to-do to the list             |
| `list-todos`          | List all to-dos or filter by priority   |
| `delete-todo [index]` | Delete the to-do at the specified index |
| `--help`              | Show help information for any command   |

## Dependencies

This application uses the following Python library:

1. love
