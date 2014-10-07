# Objective

Create a Python wrapper for a C/C++ such that it could be integrated into a 
larger Python application. You may choose any C/C++ source code you wish, 
including your own work. The aim is to demonstrate key aspects of teamwork at 
DeskGen: integration, testing, documentation, readability, good abstraction, and
 **effective communication** which we feel are just as important 
as brilliant algorithms. The goal should be that the other members of the 
DeskGen team could integrate your work into a larger Python application 
without necessarily knowing all the details of your implementation.


The skeleton follows general Python conventions for this type of package, but is
a suggestion, not a requirement.

Here is the annotated tree:

```
.
├── doc <------------------------------------------ Documentation
│    └── instructions.md
├── lib <------------------------------------------ C/C++ source
│   └── code.c
├── LICENSE.md             ,----- Project toolchain
├── README.md              |
├── scripts <--------------'  ,-- Python packaging entrypoint
├── setup.py <----------------'
├── tests <---------------------- At least one test that the wrapped code is
│   └── test_wrapper.py           callable from Python. You should also
└── wrapup                        describe the other test cases you'd write.
    ├── __init__.py
    └── wrapper.py
```


## Further notes

* Makefile and any other compilation requirements should be placed in `lib`, I
  would like to be able to compile and test the wrapper
* Documentation - sufficient documentation such that someone else at DeskGen
  could effectively setup and run the underlying C/C++ code
* License - Copyright remains yours so please pick a license

## You don't need to include

* setup.py - No need to make this a distributable python module
* granular test coverage of the library, just the more interesting public
  methods as an example is sufficient. You may wish to outline the "future
  work" you'd undertake.
* Extensive cross-platform build details (assume a sane version of Ubuntu)
* Python Packaging (setup.py) is not the focus

You may take as long as you need until you feel you have something that 
showcases your abilities and we can discuss together. As in real-life you can 
use all resources at your disposal, the web, books, friends, but ultimately 
your work should be your own. You can also reach out to the team here at
DeskGen for help if needed.

## Submission

We use the [GitHub workflow](https://guides.github.com/introduction/flow/index.html)
heavily. To submit your work, please follow it; you should fork this repository
and work on the code. When you are finished you should
[make a pull request](https://help.github.com/articles/creating-a-pull-request/)
back to the parent repository.  We'll then review the PR, checkout and run your
code, and provide feedback.


Resources
---------
* CFFI - one way of solving this problem.
 https://cffi.readthedocs.org/en/release-0.8/#an-example-of-calling-a-main-like-thing

* datrie - an example of a python-wrapped C library that we use
https://github.com/kmike/datrie

Getting Started
---------------
Assuming you haven't done any Python work before you might need a boost.
This will install PIP and a Python virtual environment and both are very good
things to know about if you do any Python development.
```
cd /tmp
wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
sudo pip install virtualenvwrapper
cd ~  # or where ever you put your code
. virtualenvwrapper.sh
mkvirtualenv wrapup 
git clone git@github.com:rodoyle/wrapup.git wrapup
cd wrapup
python setup.py develop
```
