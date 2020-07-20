# A Brief Overview of Python

Python is a multi-paradigm general purpose scripting language. It's often used for writing small scripts to run without the need of compiling. Besides it's ease of use is what made Python so attractive to programmers from various backgrounds. Primarily, Python is used for the following reasons:

1. As stated in the _Zen of Python_, the focus of Python is to be easier to understand.

2. Python increases developer productivity by requiring them to write less code which will also run immediately without compiling.

3. There're over a million developers using Python at the time of writing this book. Thus apart from the very useful standard library Python also supports a wide range of third party libraries available via PyPi.

4. Python is also the world's second most popular language as of writing this book. It practically means, developers with Python skills has a higher chance of being hired.

## What Can You Do With Python

- Considering Python's simple syntax & decreased development, its often used for system programming. The built-in OS module abstracts a lot of low-level Operating System stuff with just a call of a simple function. Hence, Python is incredibly popular to work with in environments where manipulating the system is to be expected.

- Although Python isn't a very popular language to develop GUI applications with but due to frameworks like Tkinter & PyQT, it's popular among beginner Python enthusiasts/developers. If you're starting out programming for the first time ever, a GUI app with Tkinter should be a great starting point.

- Programming with Python isn't just limited to the simple scripting or GUI applications. It is also frequently used to power the backend systems of popular websites like Pinterest, Quora, etc. Web frameworks like Flask. Django are perhaps some of the most popular frameworks to develop web apps.

- Python can also be used a glue language in certain instances in embedded technology. C libraries can be enabled wherein it can be tested & launched onsite without the need for recompliling.

- Python also comes with in-built support for Database manipulation. The `SQLite` library comes packaged in the standard library & performs as a on-file SQL database engine which is perfect for quick prototyping & testing. Besides, on the non-SQL side, Python's standard `pickle` module provides a simple object persistence system, enabling entire Python objects to file & file-like objects. Hence, it's widely used in the field of Machine Learning(ML) for saving entire models onto a persistent file-system.

- If it's not obvious by now, but Python is perfect for rapid prototyping for later migrating into other lowel-level languages like C/C++. This ease of portability is more obvious in the field of ML where the models are expected to work in a low-level environment.

- Perhaps a major reason why Python is so popular because of the advancements made in the field of ML/AI. As of writing this book, it's literally considered the de facto go-to book if you want to dive into ML. Coupled with execellent  ML frameworks & libraries like TensorFlow/PyTorch & Scikit-Learn, the ML community is yet to embrace some other language whole-heartedly.

- Python has almost completely replaced older popular languages which were used for numerical programming. Some of those older languages are FORTRAN/C++. Combined with NumPy which is a high-performance numeric programming extension for Python, the community has made very meaningful use of it in the field of ML & others.

- Generic Use Cases Like Data Mining & Such -- As mentioned earlier, Python is a general-purpose programming language & it's general-purposeness is more apparent through the fact that its used in varying other fields like data mining, robotics, gaming, natural language processing, etc.

## Why Use Python

- As Python is a multi-paradigm language, you as a developer, is left free to choose whichever paradigmn to write a script in. You could write a whole script using OOP aspects making full use of its class model systems.

- Python is completely free, will always be & is also allowed to package it up for redistribution. It's source code is available for anyone to take a peek into which means, if you're so inclined & want to make a different typen of the Python programming itself for yourself, you're free to do so.

- As of writing the book Python isn't only available on all major platforms but is available on hand-held devices as well like your iPhone! On the other hand, Python comes preinstalled with all the major Unix-based systems. So if you own a Mac or a Debian-based system, all that you've to do is call Python using the `Python` command on the Command-Line Interface(CLI).

- The Python toolbox is extremely versatile & its only becoming better by each passing day.Besides, all the reasons mentioned earlier, Python allows for dynamic typing which means, you won't have to specific mention the type of the object, although this behaviour can be changed somewhat using type hints. It also has a myriad variety of commonly used object-types, tools to manipulate the object-types & libraries all built-in! If the built-in stuff isn't enough for your use case, then Python also supports an inexhaustive list of third-party utlities hosted at PyPi which can be downloaded using `pip` - The Python Package Installer.

- Ease of Learning & Using -- I've already mentioned countless time previously but due to Python natural-language like syntax, its relatively easier for even someone who hasn't written a single line of code earlier.

## Python vs Arbitrary Language: Which Is Better

For most beginner programmers it's obvious which language would be best to start learning with. And of course without a single doubt in mind, Python is perhaps the best choice for someone who has never written a line of code ever. Primary reasons being, the almost natural English language-like syntax & the huge community support. But it's not like other programming languages doesn't enjoy the liberty of a thriving community. Javascript, Rust, C++, Java to name a few has already seen immense acceptance in a wide variety of applications. Hence, I often refrain from comparing Python with other programming languages in context to finding out which is better. At the end of the day it comes down to personal preference & mainly the specific type of job to be completed.

Regardless, for the sake of understanding, let me describe some differences between Python & other languages. But remember, no one language fars better than another. Each language will have it's drawbacks & advantages which is why some individuals end up learning more than one language.

*Work-In-Progress* -- **More Content to Write.**

## How To Run Python Programmes

- The simplest way to run Python code is through the interactive command line or commonly known as CLI. Although most Unix-based systems come with Python preinstalled, Windows user has to install by downloading the installer from the official Python website. Thereafter, just typing `python` in the Terminal or Command Prompt for Debin/Mac users & Windows users respectively.

- The interactive pompt is great for quick testing small scripts but a drawback is persistent execution of the lines of code. This makes it extremely difficult to write code & permanently store them for later use. Hence, Python scripts are written in files with the `.py` extension which can then be executed through the Terminal by calling the `python <filename.py>` command.

- In certain use cases like executing a Python script remotely on a server, its convenient to give the file executable privileges in an Unix-like environment. Fortunately, doing so is as easy as typing the `#!/usr/local/bin/python` shebang line at the top of the file & making it a executable using `chmod`.

- **Note:  `proof-read this section`** Clicking File Icons(On Windows) -- But contrary to the Unix-like system making a executable file out of a Python script for Windows isn't always a easy task. Although the shebang use case does work most of the time, libraries like wsPython are useful.

- If it's not obvious by now, Python scripts are saved using the `.py` file extension. So basically every other Python module is a script with the `.py` file extension. So in a few later sections of the book, whenever an `import` statement is used assume a Python script is being imported from somewhere.

- Using an Editor -- Typing a line of code on the interactive prompt each time a need arises can be exhaustive, inefficient & not so developer-friendly. Hence, its recommended to use some kind of Text Editors or Interactive Development Environemt(IDE) to write your code. Sublime Text, Atom & my personal favorite, Visual Studio Code are some of the popular Text Editors created specifically for coding & development.
