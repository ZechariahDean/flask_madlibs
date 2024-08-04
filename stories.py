"""Madlibs Stories."""
class Stories:
    """class to contain a list of stories"""
    def __init__(self):
        self.stories = []

stories = Stories()

class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""

        self.title = title
        self.prompts = words
        self.template = text
        stories.stories.append(self)

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started
Story(
    "fairytale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",

)
# madlib taken from 
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.readbrightly.com%2Fmad-libs-printables-activities%2F&psig=AOvVaw0bYUXtMhf8_wYJtdmpqbky&ust=1722873094112000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIjbt8jY24cDFQAAAAAdAAAAABAE
Story(
    "If I were president",
    ["1person_in_room", "1number", "1adjective", "color", "1noun", 
     "type_of_food_plural", "2noun", 'verb_ending_in_ing', 
     "article_of_clothing", "2adjective","celebrity", "2number", 
     "2person_in_room", "3noun", "3person_in_room", "occupation"],
     """My name is {1person_in_room} and I am {1number} years old. If I were president, 
     I'd do a whole bunch of {1adjective} things:  1.  I would drive the biggest {color} 
     car in the country. And that car would go faster than any other {1noun} in the world!
       2.  Everyone would eat pepperoni {type_of_food_plural} for dinner.  3.  I would 
     live in the Statue of {2noun} and build a {verb_ending_in_ing} pool at her feet.  4.
     I would wear a/an {article_of_clothing} on my head, and everyone would say I look 
     {2adjective} like {celebrity}.  5.  School would be open only {2number} days a year.
       6.  I would give my friends the best jobs. I would nominate {2person_in_room} to 
     be secretary of (the) {3noun}, and {3person_in_room} could be vice {occupation}!"""
)