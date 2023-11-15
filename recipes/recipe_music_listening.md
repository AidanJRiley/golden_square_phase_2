# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicListening:
    # User-facing properties:
    #   name: string

    def __init__(self):
        #set a empty data structure
        # e.g. self.track_list = []
        pass # No code here yet

    def add_track(self, name):
        # Parameters:
        #   task: string representing a song name
        # Returns:
        #   Nothing
        # Side-effects
        #   Throw an exception if the name is not a string
        pass # No code here yet

    def show_tracks(self):
        # Returns:
        #   A list containing all the tracks that have been added
        # Side-effects:
        #   Throws an exception if the list is empty
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE
"""
Given a number
#raises an exception
"""
music = MusicListening()
music.add_track(7) => Exception 'This is not a string!'

"""
Given a  track name
#adds the track to the track list
"""
music = MusicListening()
music.add_track('Happy') => return nothing, but add 'Happy' to the tracklist


"""
Given nothing and requests track list
#raise an exception: Exception 'No tracks in list'
"""
music = MusicListening()
music.show_tracks() => Exception 'No tracks in list'

"""
Given three tracks, then requests show_tracks
Returns a list of the three tracks
"""
music = MusicListening()
music.add_track('Happy') => return nothing, but add 'Happy' to the tracklist
music.add_track('Sad') => return nothing, but add 'sad' to the tracklist
music.add_track('Excited') => return nothing, but add 'Excited' to the tracklist
=> ['Happy','Sad','Excited']
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