# Issue #117: Essential Tools for Web Application Testing

**Repository:** esysflow  
**Status:** Open  
**Created:** 2025-02-14  
**Updated:** 2025-02-14  
**Author:** @Muralipandiyan  
**Assignees:** @Muralipandiyan  
**Labels:** `Issue`  

[View on GitHub](https://github.com/Simtestlab/esysflow/issues/117)

## Description

DOD : As a tester, I'm mentioning which framework and language are used to automate eSysFlow.
The Cypress framework and JavaScript language are used to automate eSysFlow.

# Cypress Introduction:
- Cypress is primarily a front-end web automation testing tool.
- It is specifically developed for modern web applications, such as those built with React JS and Angular JS. These types of frameworks are commonly used in web application development, and applications built with them are typically referred to as modern web applications.
- Using Cypress, we can automate any application that runs in a browser.
- Cypress uses JavaScript to write automation tests, but it doesn't use any Selenium libraries because it is entirely different from Selenium.
- Cypress is open source, but it has two main components: Cypress Runner and Cypress Dashboard. In Cypress Runner, we can design the framework and write our automation test scripts, as it is open source. However, Cypress Dashboard is a paid version.
- Cypress works on top of the Node.js environment, is built on Node.js, and comes with the Node Package Manager (NPM).
- For example, when working with a Java Maven project, it uses a global Maven repository. Whenever we need dependencies, we simply add them to the **pom.xml** file, and all the required dependencies are fetched from the Maven repository. 
- Similarly, in the Node.js environment, we have something called NPM (Node Package Manager). We can use it to get any libraries required for the Cypress automation tool.

# Who can use Cypress?  
- Both developers and testers can use Cypress.  
- Developers use Cypress to perform integration and unit testing, as well as for automation.  
- Testers prefer to use Cypress to automate end-to-end test cases and perform API testing.

# Comparison between Selenium and Cypress:

![Image](https://github.com/user-attachments/assets/f741517e-3f2a-4ef0-8c0d-971d4cb56f14)

# Features:
- TimeTravel : Cypress takes snapshots of your application every time an action is performed, such as clicking a button or entering text.
- Debuggability : It makes debugging easier and faster by showing exactly what happened at each stage.
- Automatic waits or Built-in waits : In Cypress, there is a default waiting time for everything. It automatically waits for elements and page loads. Whenever you perform an action on an element, Cypress automatically waits for that element before performing the action. This feature is built into Cypress.
- Consistence result : You will always get consistent results with Cypress. You can run the same test case any number of times and get the same results. This is because Cypress runs inside the browser, which is one of its major advantages.
- Screenshots and videos are automatically captured whenever you run a test case, regardless of whether it passes or fails.
- Cross browser testing : We can run our test cases on multiple browsers, both locally and remotely, using Jenkins or other CI/CD tools.

# Limitation :
- It can't automate Windows-based or mobile applications.  
- It has limited browser support, including Chrome, Edge, and Firefox.  
- It supports JavaScript and TypeScript languages.  

@aeroramesh @sajimotrax 
I have knowledge of the Selenium framework and Java programming language, but the Cypress framework uses JavaScript. I'm stuck here.