# Software Development Plan

## Phase 0: Requirements Analysis (tag name `analyzed`)
*(20% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Re-write the instructions in your own words.
    *   If you don't do this, you won't know what you're supposed to do!
    *   Don't leave out details!
*   [ ] Explain the problem this program aims to solve.
    *   Describe what a *good* solution looks like.
    *   List what you already know how to do.
    *   Point out any challenges that you can foresee.
*   [ ] List all of the data that is used by the program, making note of where it comes from.
    *   Explain what form the output will take.
*   [ ] List the algorithms that will be used (but don't write them yet).
*   [ ] **Tag** the last commit in this phase `analyzed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*
The instructions for this assignment is pretty well outlined in the source code todo 
lines. The crawl function is written recursviely, although it will have a loop inside of 
the function. The parameters for crawl will have to be modified to allow depths and 
urls, maxdepth, and a set of visited urls. The base cases will be if the depth is more 
than the maxdepth, or if the given url has already been visited, or if the url is 
invalid. If all these cases are untrue, then the url will be printed with the spaces 
relative to the depth of recursion, mark the url as visited, use requests libraries to 
get the url. It will use exception handling to print any exceptions and return crawl(). 
Scan the html for anchor tags(other urls), and check for href attributes. If no 
attribues, continue to next iterations. If attributes, discard fragment portion, make 
into absolute url, and call crawl again with the correct parameters. The program will be 
able to take command line arguments, and if none are given, usage message will be 
provided. If 1 is given, the argument is the starting url. The second command line 
argument, if given, is the maximum depth of recursion. The output of the program will 
have a message of the starting url and max crawl depth, and it will print out the urls 
visited with correct levels of indentation(tied to the recursion level). Bfore program 
exits, print report including time, number of links. If program is quit on keyboard 
interrupt, the report is still printed out. IF there is any errors in the libraries, the 
program does not quit and instead prints an error message and continues on with the 
pograms. 
The program aims to solve the problem of a recursive web crawler. A good solution 
outputs the correct output, without crashes or bugs. I believe that I know how to solve 
all of the problems in the program, and will just need to figure out how to use the 
libraries well. The demo program is very good though, and should help me solve 
evertyhing I need to do. I can see a little bit of challenges in figuring out some of 
these libraries. 
The data used by the program comes from the internet and the command line. The output 
consists of the recursive return strings, and the report.
There will be recursive algorithms used in this program. 

## Phase 1: Design (tag name `designed`)
*(30% of your effort)*

**Important - do not change the code in this phase**

Deliver:

*   [ ] Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain its purpose and types of inputs and outputs.
*   [ ] Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
*   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occur to you, and use them later when testing.
*   [ ] **Tag** the last commit in this phase `designed` and push it to GitLab.
    *   *Grace Points: if this tag is pushed by midnight on the Sunday before the due date, you will receive up to 5 points back*
crawler psueodcode:
	define crawl(URL, current depth, maxdepth, visited(set))
		#Base cases
		if the current depth is greater than the maxdepth, return
		if the supplied url is in the visited set, return
		Print 4 " " times the depth, plus the URL
		Add the URL to set visited
		Visit the URL using requests.get()
		If requests.get throws error, 
			print exceptions raised, return
		Scan the html given by requests.get for anchor tags <a>(representing 
		new links) with BeautifulSoup
		For each of the anchor tags:
		check for href attribute(URL link). If no href, continue.
		create variable new_url, set equal to string in href attribute
		discard fragments in new_url, if relative URL, make it absolute
		recursively call crawl(new_url, depth +1, maxdepth, visited(set)
if crawler is loaded as main module:
	if no arguments given:
		print usage message telling user to input absolute url and optionally 
		depth
	else:
		make variable url, set equal to the first command line argument
	use urlparse() on url, check if there is netloc and scheme.
	if no netloc and scheme:
		print error message, print message telling user to provide absolute url
	create variable maxdepth, set equal to 3
	create variable plural, set equal to s if maxdepth is not one, else
        its a space.
	if second command line argument is provided:
		set maxdepth to second command line argument.
	print crawling from url provided, to maxdepth(plural)
	take time.
	try:
		crawl(url, depth = 0, maxdepth = maxdepth, visited = empty set)
	except KeyBoard Interupt error:
		take time
		print system report with time and contents of visited
		exit program
	print system report with time and contents of visited
	exit program
In the face of good input, the program will run as expected, printing out reports and 
urls of websites visited, and error messages when websites are faulty. Program will 
print out end report and exit the program.
In the face of no command line arguments, usage message will be printed out. If user 
supplied relative or invalid url, and error and a usage message will be printed out. If 
user supplied 2 arguments, and the second is negative or not an integer, the program 
will default to a max recursion depth of 3, and procede as normal. If more than 2 
command line arguments are given the program will ignore extra arguments. 



 ## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.
My code followed the pseuocode that I wrote very well. Everything went pretty closly to my plan.
I did have a little issue that would cause my program to quit after printing one url, but I fixed 
it by converting the url to a string, and passing in the text of the response object into beautiful soup.
The only other issues that I had were sytanx questions about the new libraries, but the demo programs
helped me pretty well. My code works very well, and should only have a few bugs.

## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.
First, I tested the command line arguments. I ran the program with no arguments, 
and it exited with an error message. I ran the program with one URL, and the 
program defaulted to maxDepth of 3. I ran the program with an invalid url, and a 
usage message was printed. Next, I inputted a negative number into the second 
command argument field. I forgot to check if the 2nd argument was a whole digit 
greater than or equal to 0, so I added code that checked to make sure the maxdepth 
was valid. I tried a character, string, negative number, and a float value in the 
command line as the second argument, and in every case the program defaulted to a 
maxdepth of 3. Lastly, I tried putting extra arguments into the program, and they 
had no effect.
After testing the command line, I moved onto testing the crawl function. I ran all 
of the test cases that were given to us as examples from the test server, and my 
program gave the correct output for every one. I specified 0 links, and the program 
just outputted the one link. I added a plural clause into the report so it would 
print 'page', instead of '1 unique pages'. I tested my program on cs.usu.edu, and 
checked the output for error messages. My program was not swallowing the error 
messages, and instead was printing them out while not crashing. When I tried to 
input a large number into the maxdepth while using the testing server when I 
specified a large number into the breadth field, my program would crash with an 
error stating max retries exceeded with url, which I assume is not at the fault of 
my program. It worked when I specified a breadth of 20 with a depth of 30, with no 
errors.
My program quits immediatly when I input control c, and also prints out the report. 
My program was printing out the 'control C' keys onto the terminal, so I went on 
stackOverflow and found a simple piece of code that wrote the message into the 
error file, and it fixed my problem.
My program formats the output with no issues, and shows the correct level of 
indentation for each level of recursion. it prints out the reports and usage 
messages with no typos or spacing issues.  

## Phase 4: Deployment (tag name `deployed`)
*(5% of your effort)*

Deliver:

*   [ ] **Tag** the last commit in this phase `deployed` and push it to GitLab.
*   [ ] Your repository is pushed to GitLab.
*   [ ] **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Look for all of the tags in the **Tags** tab.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   [ ] **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 5: Maintenance

Spend a few minutes writing thoughtful answers to these questions.  They are meant to make you think about the long-term consequences of choices you made in this project.

Deliver:

*   [ ] Write brief and honest answers to these questions:
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   [ ] Make one final commit and push your **completed** Software Development Plan to GitLab.
*   [ ] Respond to the **Assignment Reflection Survey** on Canvas.
My program is pretty well written and easy to understand. Some of the 3rd party library sytanx may 
be a little hard to understand at first, but that can easily be fixed with a Google Search. Some of the 
error checking for the command line arguments may be a little long and sloppy, but it is still only 
a few lines. I am sure and confident on every part of the program, and I understand how everything
works very well. If a bug is reported, it shouldn't be too hard to find the source because it is 
such a short program.
My documentation should make sense to anyone, because it does not use too many technical terms. It 
will make sense to me in 6 months time. 
Adding a new feature to this program should't be too hard, because new functions or modules could be added.
The main crawler function works well, so that function could be built off of to make the program more complex
There could be potential issues if python or my systems hardware was updated, because of the 3rd party libraries 
used. These libraries would have to stay up to date with the current version of python, or the program could be 
inoperable or be left with bugs. The program should continue to work well after upgrading my systems hardware. 
