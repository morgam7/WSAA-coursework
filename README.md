# Weekly Assignments

![Panda Eating Computer](panda_eating_laptop.png)

This is the repository containing all the weekly assignments for the Web Services and Applications module of the [Higher Diploma in Science in Data Analytics given by ATU Galway-Mayo](https://www.gmit.ie/higher-diploma-in-science-in-computing-in-data-analytics). My lecturer is [Andrew Beatty](https://github.com/andrewbeattycourseware?tab=overview&from=2022-12-01&to=2022-12-31). The focus of the assignments is on interacting with APIs, handling JSON data, automating file changes, and using GitHub as part of a development workflow.

To create this repository, I installed Python using [Anaconda](https://www.anaconda.com/download), and I used [Visual Studio Code](https://code.visualstudio.com/) as a text editor and terminal. The image of the panda eating a computer was generated using OpenAI's DALL·E.

## Getting Started

To get started with this repository, you’ll need:  
1. **Python**: Install Python (I recommend using [Anaconda](https://www.anaconda.com/), which includes all the necessary tools and libraries).  
2. **A Notebook Editor**: I used Visual Studio Code, but you can also use [Jupyter Notebook](https://jupyter.org/) or [Google Colab](https://colab.research.google.com/).  

## Libraries Used

- Python
- Jupyter Notebook
- REST APIs
- JSON
- Git and GitHub

### Weekly Assignments

- `assignment2-carddraw.py`  
  Python program that uses the Deck of Cards API to shuffle a deck, draw five cards, print the value and suit of each card, and check the hand for combinations such as a pair, triple, straight, or flush.

- `assignment03-cso.ipynb`  
  Python notebook that retrieves the CSO dataset **Exchequer Account (Historical Series)** and saves it locally as `cso.json`.

- `assignment04-github.py`  
  Python program that reads a file from a GitHub repository, replaces every instance of the text `"Andrew"` with my name, and then commits and pushes the change back to the repository.

## Highlights and Challenges

### carddraw

This assignment involved using the Deck of Cards API to shuffle a deck, draw five cards, and extract the value and suit from the JSON response. The main challenge was understanding the structure of the returned data and working with lists of card values and suits in Python. The program also checks the hand for combinations such as a pair, triple, or flush, which helped reinforce the use of loops, counting repeated values, and conditional statements. Overall, the task improved my understanding of API responses and Python data handling.

### assignment03-cso
This assignment was short, but the main challenge was making sure I was getting the actual dataset rather than the html for the public webpage describing it. I needed the JSON dataset itself. The dataset page lists the real machine-readable resource separately under Data Resources, and on the JSON-STAT landing page is the ws.cso.ie API URL. Once I used the correct CSO API link, the program was able to request the dataset successfully and save it to cso.json


### assignment04
This assignment involved several practical issues while working with the GitHub API. The main challenges were learning to use the correct API URL instead of the normal GitHub webpage link, understanding that authentication tokens allow access to the repository through the API, and handling the Base64 encoding GitHub uses for file contents. I also had to fix debugging problems such as missing imports, inconsistent variable names, and incorrectly structured update requests, including a 422 error caused by not sending the required JSON fields properly. Another issue arose when applying multiple replacements, as only the last change was being saved until I updated the loop logic. Finally, because the file was changed remotely through the API, I had to refresh the local copy without disturbing other uncommitted work. Overall, the assignment helped me understand how to read, modify, and update repository files programmatically using Python and the GitHub API.



## References

I used the module lecture notes and class materials as a guide when completing these assignments, along with the code in the course repository available [here](https://github.com/andrewbeattycourseware/wsaa-courseware). I also used ChatGPT as an AI support tool for debugging and figuring out why my code wasn't working.

Deck of Cards API. Available at: https://deckofcardsapi.com\
Central Statistics Office (CSO) Ireland, Exchequer Account (Historical Series), dataset FIQ02. Available via the CSO / PxWeb API.
GitHub REST API documentation. Available at: https://docs.github.com/en/rest\
Requests: https://realpython.com/python-requests/\
https://www.geeksforgeeks.org/python/python-replace-multiple-characters-at-once/\
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens\
https://docs.python.org/3/library/base64.html\
https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10\
https://www.geeksforgeeks.org/python/counters-in-python-set-1/\






