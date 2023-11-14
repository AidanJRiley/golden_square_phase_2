# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

We need a function that takes a string as an argument.
The function needs to return True or False, depending on 
if the string contains '#TODO'.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def todo_checker(word):
    """Checks if an argument contains #TODO in a string, returns True if it does, False if not.

    Parameters: words (a string containing words)

    Returns: Boolean (depending on a conditional)

    Side effects: No side effects
    """
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given a non-string (e.g. None, Integer, float, list, dictionary)
"""

todo_checker(None) => "Not a string!"

"""
Given a string containing #TODO
"""

todo_checker("#TODO Water the plants") => True

"""
Given a string not containing #TODO
"""

todo_checker('Wash the dishes') => False

"""
Given a string containing TODO (not #TODO)
"""
todo_checker('TODO Wash the dog') => False

"""
Given a string containing #TODO, at the end
"""
todo_checker('Feed the dog #TODO') => True

"""
Given a string containing #todo
"""
todo_checker('#todo get my capslock key fixed') => True

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

see test_todo_checker.py

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->