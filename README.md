


# Clean Code in Python

<a href="https://www.packtpub.com/application-development/clean-code-python?utm_source=github&utm_medium=repository&utm_campaign=9781788835831 "><img src="https://static.packt-cdn.com/products/9781800560215/cover/smaller" alt="Clean Code in Python" height="256px" align="right"></a>

This is the code repository for [Clean Code in Python](https://www.packtpub.com/application-development/clean-code-python?utm_source=github&utm_medium=repository&utm_campaign=9781788835831 ), published by Packt.

**Refactor your legacy code base**

## What is this book about?
Python is currently used in many different areas such as software construction, systems administration, and data processing. In all of these areas, experienced professionals can find examples of inefficiency, problems, and other perils, as a result of bad code. After reading this book, readers will understand these problems, and more importantly, how to correct them.

This book covers the following exciting features:
Set up tools to effectively work in a development environment 
Explore how the magic methods of Python can help us write better code 
Examine the traits of Python to create advanced object-oriented design 
Understand removal of duplicated code using decorators and descriptors 
Effectively refactor code with the help of unit tests 
Learn to implement the SOLID principles in Python 

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1788835832) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations

**Setup**

Create a virtual environment, and once activated run:

    make setup

This will install the common dependencies. Besides this, each chapter might
have additional ones, for which another ``make setup`` will have to be run
inside that particular directory.

Each chapter has its corresponding directory given by its number.

Inside each chapter directory, tests can be run by:

    make test

This requires the ``make`` application installed (in Unix environments).
In environments without access to the ``make`` command, the same code can be
tested by running the commands on the ``Makefile``:

    python -m doctest *.py
    python -m unittest *.py

All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
```

## Errata
* In Chapter 2, page 41: Add the following import in the code: ```from datetime import date```

**Following is what you need for this book:**
This book will appeal to team leads, software architects and senior software engineers who would like to work on their legacy systems to save cost and improve efficiency. A strong understanding of Programming is assumed.

With the following software and hardware list you can run all code files present in the book (Chapter 1-10).
### Software and Hardware List
| Chapter | Software required | Hardware required |
| -------- | ------------------------------------ | ----------------------------------- |
|1, 2, 3, 4, 5, 6, 7, 8, 9, 10  |Python 3.7  |System with 4GB RAM  |
|10  |Docker  |System with 4GB RAM  |

### Related products
* Secret Recipes of the Python Ninja [[Packt]](https://www.packtpub.com/application-development/secret-recipes-python-ninja?utm_source=github&utm_medium=repository&utm_campaign=9781788294874 ) [[Amazon]](https://www.amazon.com/dp/1788294874)

* Python Programming Blueprints [[Packt]](https://www.packtpub.com/application-development/python-programming-blueprints?utm_source=github&utm_medium=repository&utm_campaign=9781786468161 ) [[Amazon]](https://www.amazon.com/dp/1786468166)

## Get to Know the Author
**Mariano Anaya**
is a software engineer who spends most of his time creating software with Python and mentoring fellow programmers. Mariano's main areas of interests besides Python are software architecture, functional programming, distributed systems, and speaking at conferences.

He was a speaker at Euro Python 2016 and 2017. To know more about him, you can refer to his GitHub account with the username rmariano.

His speakerdeck username is rmariano.


### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781788835831">https://packt.link/free-ebook/9781788835831 </a> </p>
