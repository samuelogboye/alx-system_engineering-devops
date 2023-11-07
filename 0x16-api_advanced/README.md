# Reddit API Advanced Tasks

This repository contains solutions to advanced tasks related to the Reddit API. The tasks are designed to help you become proficient in working with APIs, parsing JSON data, and implementing recursive functions. The project covers the following objectives:

    Reading API documentation to find the desired endpoints.
    Using APIs with pagination to retrieve data from multiple pages.
    Parsing JSON results from an API response.
    Making recursive API calls to retrieve all relevant data.
    Sorting a dictionary by value.

Project Structure

The repository is organized into the following files, each corresponding to a specific task:

    0-subs.py: This file contains the solution for the task "How many subs?" It provides a Python function to query the Reddit API and return the number of subscribers for a given subreddit.

    1-top_ten.py: This file contains the solution for the task "Top Ten." It includes a Python function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    2-recurse.py: This file contains the solution for the task "Recurse it!" It includes a recursive Python function that queries the Reddit API and returns a list of titles for all hot articles in a given subreddit.

    100-count.py: This file contains the solution for the task "Count it!" It includes a recursive Python function that queries the Reddit API, parses article titles, and prints a sorted count of given keywords.

Usage

You can run each of the tasks using the provided main scripts, such as 0-main.py, 1-main.py, 2-main.py, and 100-main.py. These scripts demonstrate how to use the respective functions with sample input.

To execute the main scripts, use the following format:

```bash
python3 <main_script.py> <subreddit> <additional_arguments>
```

    <subreddit>: Replace this with the name of the subreddit you want to query.

    <additional_arguments>: These arguments may vary depending on the task and can include keyword lists for task 3 or other relevant parameters.

Please note that if you provide an invalid subreddit, the functions will handle it gracefully and return appropriate responses.
Requirements

    Python 3.4.3 or later.
    The requests module for making HTTP requests to the Reddit API.
    The PEP 8 coding style should be followed for code consistency.
    All files should have proper documentation, and the first line should be #!/usr/bin/python3.

Disclaimer

Keep in mind that the number of results may not be accurate as Reddit's hot articles are constantly changing. The tasks focus on the functionality of the code rather than the specific number of occurrences.

Please ensure that you do not use loops and instead implement recursive functions, as the tasks emphasize this approach.

Happy coding and enjoy working with the Reddit API!
