# A Brief Overview of Python

Python is a multi-paradigm general purpose scripting language which is used for writing small scripts to run without the need of compiling. Due it's ease of use, almost natural-language-like syntax, Python attracts programmers & beginners alike from various backgrounds from software developers to scientific experiments in CERN. But primarily, Python is used for the following reasons:

1. The [PEP 20 -- _Zen of Python_](https://www.python.org/dev/peps/pep-0020/#id2), states the focus of writing Python code should be for easier interpretability & less [cognitive load](https://en.wikipedia.org/wiki/Cognitive_load). Accordingly, the Python syntax should be very familiar to individuals who has never written a line of code before, as it has a English natural-language-like syntax.

2. Python's simple synatx increases developer productivity by requiring them to write less code which also runs immediately without compiling. Thus, the language has become very popular among individuals in the field of Data Analytics or scientic programming where visualizations are important. Using Python these individuals can expect to see results of their work almost as immediately as the writing the code. In other words, Python is more of a "[_What You See Is What You Get (WYSIWYG)_](https://en.wikipedia.org/wiki/WYSIWYG)" programming language in my opinion.

3. As of writing this book, Python is one of the most popular programming language out there among 57000+ respondents on Stack Overflow making it the [4th most popular language](https://insights.stackoverflow.com/survey/2020#technology-programming-scripting-and-markup-languages)! What does it mean for you & me? Community support. Python already boasts a humongous [Standard Library](https://docs.python.org/3/library/) & together with its extensive third party library support hosted at [PyPI -- The Python Package Index](https://pypi.org/), there's no reason why an interested individual should refrain from learning Python.

4. Being the most popular programming language also comes with certain advantages. The most obvious one is perhaps, availability of employment opportunities. Besides, most of the jobs available for a Python developer appears to be well paid too! As per Glassdoor reports, a Python Developer can expect a salary from anything between [$56K-$107K](https://www.glassdoor.com/Salaries/python-developer-salary-SRCH_KO0,16.htm?countryRedirect=true&countryRedirect=true). But of course considering the popularity of Python among individuals working in the field of Data Science and/or Machine Learning, one can expect an even heftier paycheck.

## What Can You Do With Python

- As mentioned earlier, writing Python code is super simple. It's as easy as writing simple one-liners in English as showcased in a video -- [Complexity of Hello World & What Comes After](https://www.youtube.com/watch?v=dRhLRvOZEXA&t=367s) for writing the `Hello world!` code in various programming languages. Hence, due to the simple syntax & decreased development time requirements, its often used for system programming. The versatile built-in [OS module](https://docs.python.org/3/library/os.html) abstracts a ton of low-level Operating System work with just the call of a simple function. Thus without a doubt, Python is extensibly used to do anything from manipulating system paths, to downloading files over Internet into distinct directories and/or automatically setting up a development environments by manipulating [dotfiles](https://dotfiles.github.io/). The sky is the limit in what's possible with the OS module.

- Python isn't really the most favoured language to develop GUI applications but it does have a decent support of the community to develop GUI applications using [Tkinter (_pronounced as "tee-keentar"_)](https://docs.python.org/3/library/tkinter.html) which is part of the Standard Library as well! It's perfect for beginners to get into programming as Python being an interpreted language enables the user to see his/her creations right away without compiling or creating binaries. Beside Tkinter, other production capable frameworks like [PyQT5](https://pypi.org/project/PyQt5/) are used extensibly by enterprises to desktop applications.

- Perhaps, building desktop applications or simple scripting isn't your thing & you want to learn a skill with a wider employment prospect like web development. Luckily this is where Python shines the most for its general purposeness. Its frequently used to power the backend systems of popular websites like Pinterest, Quora, etc. You can build [RESTful APIs](https://en.wikipedia.org/wiki/Representational_state_transfer) using web frameworks like [Flask](https://flask.palletsprojects.com), [Django](https://www.djangoproject.com/), [FastAPI](https://fastapi.tiangolo.com/). Unsurprisingly, Flask & Django are also perhaps two of the most popular frameworks to build web apps with beside the likes of Javascript frameworks like [Node.js](https://nodejs.org).

- Python is also often used as a glue language in certain instances for embedded technologies. Due to the decreased development time, prototypes are built using Python which are then ported to C/C++ for the increased execution speed. Also note it, C libraries can be written using [Cython](https://cython.org/) wherein it can be tested & launched onsite without the need for recompliling.

- Boasting Python's huge Standard Library would be a disappointment if it didn't come with built-in support for Database manipulations. Thus, it supports database manipulation using the [SQLite](https://docs.python.org/3/library/sqlite3.html) interface. It performs on-file manipulations using the SQL database engine which is perfect for quick prototyping & testing. Beside the on-file SQL system, on the non-SQL side, Python's standard [pickle](https://docs.python.org/3/library/pickle.html) module provides a simple object persistence system, enabling entire Python objects to be written into file & file-like objects. Hence, it's widely used in the field of Machine Learning(ML) for saving entire models onto a persistent file-system.

- A major reason for Python's rise in popularity is due to the advancements made in the field of ML & AI. As of writing this book, it's literally considered the de facto go-to programming language for those interested in ML. Coupled with execellent ML frameworks & libraries like [TensorFlow](https://www.tensorflow.org/)/[PyTorch](https://pytorch.org/) & [Scikit-Learn](https://scikit-learn.org/stable/), the ML community is yet to embrace any other language whole-heartedly.

- Python has almost completely replaced older popular languages like Fortran/C++ for numerical programming. Its scientific computing library, [NumPy](https://numpy.org/) is a high-performance numeric programming library for Python. Due to its performance speed, Numpy is used extensibly from Astronomy to complex Mathematical Analytics. So if you're a researcher at CERN or you might as well work as a Quant, then you should definitely check it out. 

- "_Python IS an general-purpose language_" is a statement you'll hear from literally every Pythonista (A developer who codes in Python)! But nowhere else is it more apparent then generic use cases like Data Mining, Robotics, Automation & similar work.

====EDITED TILL HERE====

## Why Use Python

- As Python is a multi-paradigm language, you as a developer, is left free to choose whichever paradigmn to write a script in. You could write a whole script using OOP aspects making full use of its class model systems.

- Python is completely free, will always be & is also allowed to package it up for redistribution. It's source code is available for anyone to take a peek into which means, if you're so inclined & want to make a different typen of the Python programming itself for yourself, you're free to do so.

- As of writing the book Python isn't only available on all major platforms but is available on hand-held devices as well like your iPhone! On the other hand, Python comes preinstalled with all the major Unix-based systems. So if you own a Mac or a Debian-based system, all that you've to do is call Python using the `Python` command on the Command-Line Interface(CLI).

- The Python toolbox is extremely versatile & its only becoming better by each passing day.Besides, all the reasons mentioned earlier, Python allows for dynamic typing which means, you won't have to specific mention the type of the object, although this behaviour can be changed somewhat using type hints. It also has a myriad variety of commonly used object-types, tools to manipulate the object-types & libraries all built-in! If the built-in stuff isn't enough for your use case, then Python also supports an inexhaustive list of third-party utlities hosted at PyPi which can be downloaded using `pip` - The Python Package Installer.

- Ease of Learning & Using -- I've already mentioned countless time previously but due to Python natural-language like syntax, its relatively easier for even someone who hasn't written a single line of code earlier.

## Python vs Arbitrary Language: Which Is Better

For most beginner programmers it's obvious which language would be best to start learning with. And of course without a single doubt in mind, Python is perhaps the best choice for someone who has never written a line of code ever. Primary reasons being, the almost natural English language-like syntax & the huge community support. But it's not like other programming languages doesn't enjoy the liberty of a thriving community. Javascript, Rust, C++, Java to name a few has already seen immense acceptance in a wide variety of applications. Hence, I often refrain from comparing Python with other programming languages in context to finding out which is better. At the end of the day it comes down to personal preference & mainly the specific type of job to be completed.



## How To Run Python Programmes

- The simplest way to run Python code is through the interactive command line or commonly known as CLI. Although most Unix-based systems come with Python preinstalled, Windows user has to install by downloading the installer from the official Python website. Thereafter, just typing `python` in the Terminal or Command Prompt for Debin/Mac users & Windows users respectively.

- The interactive pompt is great for quick testing small scripts but a drawback is persistent execution of the lines of code. This makes it extremely difficult to write code & permanently store them for later use. Hence, Python scripts are written in files with the `.py` extension which can then be executed through the Terminal by calling the `python <filename.py>` command.

- In certain use cases like executing a Python script remotely on a server, its convenient to give the file executable privileges in an Unix-like environment. Fortunately, doing so is as easy as typing the `#!/usr/local/bin/python` shebang line at the top of the file & making it a executable using `chmod`.

- **Note:  `proof-read this section`** Clicking File Icons(On Windows) -- But contrary to the Unix-like system making a executable file out of a Python script for Windows isn't always a easy task. Although the shebang use case does work most of the time, libraries like wsPython are useful.

- If it's not obvious by now, Python scripts are saved using the `.py` file extension. So basically every other Python module is a script with the `.py` file extension. So in a few later sections of the book, whenever an `import` statement is used assume a Python script is being imported from somewhere.

- Using an Editor -- Typing a line of code on the interactive prompt each time a need arises can be exhaustive, inefficient & not so developer-friendly. Hence, its recommended to use some kind of Text Editors or Interactive Development Environemt(IDE) to write your code. Sublime Text, Atom & my personal favorite, Visual Studio Code are some of the popular Text Editors created specifically for coding & development.
