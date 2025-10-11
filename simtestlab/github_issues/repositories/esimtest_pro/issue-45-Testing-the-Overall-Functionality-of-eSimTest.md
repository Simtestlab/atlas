# Issue #45: Testing the Overall Functionality of eSimTest

**Repository:** esimtest_pro  
**Status:** Closed  
**Created:** 2024-11-29  
**Updated:** 2024-11-29  
**Closed:** 2024-11-29  
**Author:** @Muralipandiyan  
**Assignees:** @Muralipandiyan  

[View on GitHub](https://github.com/Simtestlab/esimtest_pro/issues/45)

## Description

DOD : As a tester, I need to test the following functionalities and validate the software.

Files:
-  Create Testcase.
-  Load Testcase.
-  Load Excel data (under implementation).
-  Save.
-  Save As.

**Create Testcase**

     1. Verify if the folder name and model name are the same.
     2. Select "Create Testcase" and load the model.
     3. Verify whether the verification folder is created and ensure the MATLAB model opens at the same time.
     4. Set Test parameters 
     5. Inport values are provided from the plotting window, and a test case should be written.
     6. Set the expected output on the outports. The actual output will be generated on assessments out.
     7. If the actual output matches the expected output, the test case will pass. If not, the test case will fail.

![Image](https://github.com/user-attachments/assets/a149f75f-1d46-4d3b-9c82-230d901fd69f)

![Image](https://github.com/user-attachments/assets/a97110f5-fb4b-4e67-930a-2159dbcc92a3)

**Load Testcase**
 1. Initially, "Create Testcase" will generate a default test template. From the next time, we will select "Load Testcase" instead of creating a new one, as the test template will remain empty.
 2. Inport values are provided from the plotting window, and a test case should be written.
 3. Set the expected output on the outports. The actual output will be generated on assessments out.
 4. If the actual output matches the expected output, the test case will pass. If not, the test case will fail.

**Save And Save As**
"Save" will store the input and output in the Test Template, while "Save As" allows you to choose the specific location to save the file.



