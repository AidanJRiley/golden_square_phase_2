# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._
'''
The name of the class.
The design of its initializer, the parameters it takes, and their data types
The design of any properties the user will need to read or write, and their data types
The design of its public methods, including:
Their names and purposes
What parameters they take and the data types
What they return and that data type
Any other side effects they might have
'''

```python
# EXAMPLE

class ToDo:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def show_todo_tasks(self):
        # Returns:
        #   A list of all current todo tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def remove_completed_tasks(self,task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Moves task to completed list
        #   Throws an exception if task is not in todo list
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given no tasks
#show_todo_list raises an exception
"""
todo = ToDo()
todo.show_todo_list() #raises an error with the message "ToDo list is empty"

"""
Given a task that isn't a string
#add_task raises an exception
"""
todo = ToDo()
todo.add_task() #raises an error with the message "Task must be a valid string"


"""
Given a task
#show_todo_list returns a list of one
"""
todo = ToDo()
todo.add_task("Bake a cake")
todo.show_todo_list() => ['Bake a cake']

"""
Given multiple tasks
#show_todo_list returns a list of all tasks
"""
todo = ToDo()
todo.add_task("Bake a cake")
todo.add_task("Water plants")
todo.add_task("Eat chocolate")
todo.show_todo_list() => ['Bake a cake','Water plants','Eat chocolate']



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
