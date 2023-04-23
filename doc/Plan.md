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


## Phase 2: Implementation (tag name `implemented`)
*(15% of your effort)*

**Finally, you can write code!**

Deliver:

*   [ ] More or less working code.
*   [ ] Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan.
*   [ ] **Tag** the last commit in this phase `implemented` and push it to GitLab.


## Phase 3: Testing and Debugging (tag name `tested`)
*(30% of your effort)*

Deliver:

*   [ ] A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
    *   Write your test cases in plain language such that a non-coder could run them and replicate your experience.
*   [ ] **Tag** the last commit in this phase `tested` and push it to GitLab.


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
