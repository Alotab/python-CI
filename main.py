import click


@click.group
def mycommands():
    """Main entry point for the CLI application.
    This function groups all the commands together, so they can be executed under the same command-line interface.
    """
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def help(name):
    """Prints a personalized greeting to the user.
    This command asks for the user's name and prints a greeting message with the name provided.
    Arguments:
        name (str): The name of the user to greet.
    """
    click.echo(f"Hello, {name}")


PRIORITIES = {
    "o": "Optional", 
    "l": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("--name", "n", prompt="Enter the todo name", help="The name of the todo item")
@click.option("--desc", "d", prompt="Describe the todo", help="The description of the todo item")
def add_todo(n, d, priority, todofile):
    """Adds a new to-do item to the to-do list.
    This command allows the user to add a to-do item with a name, description, and priority to a specified file.
    If no file is specified, it will default to using 'mytodos.txt'. The priority of the to-do can be set to one of
    the predefined values: Optional, Low, Medium, High, or Crucial.
    """
    filename = todofile if todofile else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{n}: {d} [Priority: {PRIORITIES[priority]}]\n")




@click.command()
@click.argument("idx", type=int, required=1)
def delete_todo(idx):
    """Deletes a to-do item by its index in the list.
    This command allows the user to delete a to-do item from the to-do list file based on the index position.
    After the deletion, the remaining to-do items are saved back to the file.
    """
    with open("mytodos.txt", "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(idx)
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True), required=0)
def list_todos(priority, todofile):
    """Lists all to-do items or filters them by priority.
    This command lists the to-do items from a specified file, or defaults to 'mytodos.txt'. The user can optionally
    filter the list by priority. If no priority is specified, all to-do items will be listed.
    """
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for idx, todo in enumerate(todo_list):
            print(f"({idx}) - {todo}")
    else:
        for idx, todo in enumerate(todo_list):
            if f"[Priority: {PRIORITIES[priority]}]" in todo:
                print(f"({idx}) - {todo}")



# Add commands to the main command group
mycommands.add_command(help)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__ == "__main__":
    mycommands()
