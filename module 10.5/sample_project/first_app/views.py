from django.shortcuts import render
from datetime import datetime

def index(request):
    d = {
        # 'add' filter: The number to be incremented.
        "number_to_add": 4,  # For add

        # 'addslashes' filter: The string with quotes to be escaped.
        "string_with_quotes": "I’m Jai",  # For addslashes

        # 'capfirst' filter: The string to capitalize the first character.
        "lowercase_string": "jai",  # For capfirst

        # 'center' filter: The string to be centered.
        "short_name": "Jai",  # For center

        # 'cut' filter: The string to remove spaces.
        "string_with_spaces": "String with spaces",  # For cut

        # 'date' filter: The current datetime to be formatted.
        "current_datetime": datetime.now(),  # For date and time

        # 'default' filter: An empty string to provide a default value.
        "empty_value": "",  # For default

        # 'dictsort' filter: List of dictionaries to be sorted by name.
        "dictionary_list": [  # For dictsort
            {"name": "zed", "age": 19},
            {"name": "amy", "age": 22},
            {"name": "joe", "age": 31},
        ],

        # 'divisibleby' filter: The number to check divisibility.
        "divisible_number": 21,  # For divisibleby

        # 'escape' filter: The HTML string to be escaped.
        "html_string": '<h1>Title</h1>',  # For escape

        # 'filesizeformat' filter: The file size in bytes to be formatted.
        "file_size_bytes": 123456789,  # For filesizeformat

        # 'first' filter: A list to get the first item.
        "string_list": ["a", "b", "c"],  # For first

        # 'join' filter: A list to join items with a string separator.
        "string_list_to_join": ["a", "b", "c"],  # For join

        # 'last' filter: A list to get the last item.
        "longer_list": ["a", "b", "c", "d"],  # For last

        # 'length' filter: A list to get its length.
        "longer_list_length": ["a", "b", "c", "d"],  # For length

        # 'linenumbers' filter: A multi-line text to display with line numbers.
        "multi_line_text": "one\ntwo\nthree",  # For linenumbers

        # 'lower' filter: The string to be converted to lowercase.
        "mixed_case_string": "My Name is Jai",  # For lower

        # 'make_list' filter: A string to be converted into a list.
        "name_string": "Naveen",  # For make_list

        # 'random' filter: A list from which a random item will be picked.
        "random_items_list": ["a", "b", "c", "d"],  # For random

        # 'slice' filter: A list to be sliced.
        "short_list_for_slice": ["a", "b", "c"],  # For slice

        # 'slugify' filter: A string to be slugified.
        "string_to_slugify": "Jai is a slug",  # For slugify
    }
    return render(request, "first_app/index.html", d)
