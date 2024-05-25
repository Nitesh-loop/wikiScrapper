# Requirements:

#  Install virtualenv:
pip install virtualenv

--------------------------------------------------------------------------------------------------------
pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-20.26.2-py3-none-any.whl.metadata (4.4 kB)
Collecting distlib<1,>=0.3.7 (from virtualenv)
  Downloading distlib-0.3.8-py2.py3-none-any.whl.metadata (5.1 kB)
Collecting filelock<4,>=3.12.2 (from virtualenv)
  Downloading filelock-3.14.0-py3-none-any.whl.metadata (2.8 kB)
Collecting platformdirs<5,>=3.9.1 (from virtualenv)
  Downloading platformdirs-4.2.2-py3-none-any.whl.metadata (11 kB)
Downloading virtualenv-20.26.2-py3-none-any.whl (3.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.9/3.9 MB 4.8 MB/s eta 0:00:00
Downloading distlib-0.3.8-py2.py3-none-any.whl (468 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 468.9/468.9 kB 9.8 MB/s eta 0:00:00
Downloading filelock-3.14.0-py3-none-any.whl (12 kB)
Downloading platformdirs-4.2.2-py3-none-any.whl (18 kB)
Installing collected packages: distlib, platformdirs, filelock, virtualenv
Successfully installed distlib-0.3.8 filelock-3.14.0 platformdirs-4.2.2 virtualenv-20.26.2
--------------------------------------------------------------------------------------------------------

# Create a Virtual Environment: Navigate to your project directory or the directory where you want to create your virtual environment. Then run:
virtualenv myScrapEnv

# Activate the Virtual Environment on Windows: 
myScrapEnv\Scripts\activate

# Activate the Virtual Environment on Linux/MacOS:
source myScrapEnv/bin/activate

python -m pip install selenium
python -m pip install requests
python -m pip install urllib3

# Requests: It is an efficient HTTP library used for accessing web pages.
# Urlib3: It is used for retrieving data from URLs.
# Selenium: It is an open-source automated testing suite for web applications across different browsers and platforms.

pip install bs4

# BeautifulSoup is a Python library for pulling data out of HTML and XML files.
# It needs an input (document or URL) to create a soup object as it cannot fetch a web page by itself.
# We have other modules such as regular expression, lxml for the same purpose.
# We then process the data in CSV or JSON or MySQL format.



#Three features that make Beautiful Soup so powerful:

# 1. Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, Sand modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn’t take much code to write an application
# 2. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don’t have to think about encodings unless the document doesn’t specify an encoding and Beautiful Soup can’t detect one. Then you just have to specify the original encoding.
# 3. Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility. Then we have to just process our data in a proper format such as CSV or JSON or MySQL.