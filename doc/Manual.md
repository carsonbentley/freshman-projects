# Recursive Web Crawler User Manual

*   This is the **user manual**, not the **programmer's manual**
    *   Keep your instructions at a user-friendly level.
*   Explain how to run the program
    *   What is the name of the main program file?
    *   What command-line arguments are needed?
*   What output does the program produce?
    *   What is shown when the program works correctly?
    *   What is shown when an error is encountered
    *   Provide examples of both!
*   This block of instructions does not belong in the finished product
    *   Delete this before turning it in

To run the program, the libraries must first be installed on the users computer. To do 
this, run 'python -m pip install --user -r requirements.txt'. Navigate into the 
cs1440-assn6 directory. From there, either run 'python3 src/crawler.py', or navigate 
into the src directory and run 'python3 crawler.py'.
The crawler.py program take 2 arguments, an absolute URL and a maximum recursion depth. 
The absolute URL command line argument is REQUIRED. If this is not supplied, the program 
will quit with a usage message. The URL must be absolute, and include a scheme(http, 
https, etc) followed by a :// token, followed by a hostname.
If the second command line argument is not inputted, the program will default to a 
maximum recursion depth of 3. This means that the program follow a link on the webpage 
specified, then follow all the links that were on the new link opened, and follow all of 
the links links. It will repeat this process for every link on the URL specified. If the 
depth is specified, by providing a positive integer as a second command line argument, 
the program will follow each link on the supplied webpage up to 5 links deep. 
When the program runs correctly, a message will be printed out with the starting 
URL, and the level of recursion. URL's will be printed out,starting with the supplied 
URL,  with each level of recursion indicated by 4 additional spaces. If there is a 
faulty link, the program will print an error and keep crawling. After the crawler has 
completed its work, a report will be printed out with the total time, and the number of 
unique webpages printed out. If the user quits the program with 'control + C', the 
crawler will terminate, and the report will still be printed out. 
When the program is run without any command line arguments, the program will terminate 
with a simple usage method. If the program is ran with a URL that is not absolute (such 
as 'duckduckgo.com' or 'cs.usu.edu' instead of 'https://duckduckgo.com' or 
'https://cs.usu.edu'), an Invalid URL error will be raised, with a short usage method. 
The second command line argument, recursion depth, is optional and will default to 3. 
Valid recursion depth would be any positive integer, from 0 on. Depths past 2 or 3 may 
take extremely long for the crawler to complete, this is normal. Depths such as '-1' or 
'0.5' are invalid, and if supplied, the program will still run with the default depth. 
Additional arguments are ignored, and the program will run as usual.
