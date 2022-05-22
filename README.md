# GFA Tester

The following script was written to calculate which students have met the GFA requirements for a given project. This was created during the Spring 2022 semester when I was TAing for CMSC131.

## Usage

The script was written to account for both manually graded and autograded projects. Manually graded projects such as Processing projects will contain different names for the requirements needed to pass a GFA for that given project, whereas, for autograded projects students only need to pass X amount of public tests to meet a GFA requirement.

You will need to change the values of the variables depending on the type of project you are handling. But generally, there are some variables value you will need to change no matter what. We will start with those below. 

### General Variable Changes

Whether you are handling a manually graded project or autograded project, you will have to change the value of the following variables below no matter what.

```python
    assignment = ''
    comment_pass = ''
    comment_fail = ''
    input_file_name = ''
    output_file_name = ''
```

- The **'assignment'** variable defines the assignment column we will fill in the grades server.
- The **'comment_pass'** variable defines the comment a student will see if they passed the GFA
- The **'comment_fail'** variable defines the comment a student will see if they failed the GFA
- The **'input_file_name'** variable defines the CSV file name for the file downloaded from the grades server. **Make sure** that the file is present within the same directory as the python file or else you will encounter an error where the file cannot be found.
- The **'output_file_name'** variable defines the CSV file name for the output file the script will generate.

An example of variable values is shown below:

```python
    assignment = 'GFA1'
    comment_pass = 'GFA passed'
    comment_fail = 'GFA failed'
    input_file_name = 'grades-p1.csv'
    output_file_name = 'p1-gfa-results.csv'
```
Once these changes are made, we can move on to changes **only** certain variables. These variables will depend on whether we are handling a manually graded project or autograded project. 

### Usage: Handling Manually Graded Projects

I will be giving a usage case for manual projects below. First, let us download the student's scores for that given project.

1. Download the given project, make sure to check off 'Shown' for **Sub-scores for assignments**

Secondly, we need to determine the column names for each of the requirements needed to pass the GFA. 

2. In the **'View & Enter Scores'** section, you'll have all the assignments listed in the first row of the table presented.
    - Select the correct project listed in the grades server.
3. Once you selected the correct project, you will see the sub-columns for that given project along with the total possible points for those sub-columns.
    - Those sub-columns represent the requirements listed in the project description. 

    Below is an example of what a project's sub-columns could look like:

    <p align="center">
        <img src="img/columns.png" />
    </p>

    Given these columns, let us assume that the students need to pass the first four requirements in order to meet the GFA. They **must** receive full points for each requirements.

    We are now going to modify some of the code inside **gfa.py** or **gfa.ipynb** depending on your choice.

    Inside our code we have this variable name:

    ```python
        manual_columns = {}
    ```

    This dictionary is going to store the column name and their total possible points. The key is going to be the column name as a str and the value is the total points as an int. Going back to our example, lets say that our requirements are the first four columns shown the image above, our **'manual_columns'** dictionary will look like this.

    ```python
        manual_columns = {'MB' : 10, 'BP' : 10, 'BT' : 15, 'PC' : 15}
    ```

    These columns name will be present in the CSV file you have downloaded from the grades server. The script will use these column to filter out any unecessary columns to generate our final table showing which students have passed or failed the GFA.

    Since we are handling a manually graded project, it is **very** important to change the value of the **autograded** variable from 
    ```python
        autograded = True
    ```
    to 
    ```python
        autograded = False
    ```

    Once you have changed all the necessary variables, you can run the script.


### Usage: Handling Autograded Projects

I will be giving a usage case for autograded projects below. First, let us download the student's scores for that given project.

1. Download the given project, make sure to check off 'Shown' for **Sub-scores for assignments**

Secondly, we need to determine the column names for each of the requirements needed to pass the GFA. Since we are handling an autograded project, we only need to worry about the number of public tests a student needs to pass. This makes everything much easier as each public test is worth the same amount of points but we still need to change the values of variables.

These are the variables you will need to change in the **gfa.py** or **gfa.ipynb** file.
```python
    number_of_pub_tests = 0
    points_per_pub_test = 0
    number_of_pub_tests_needed_to_pass = 0
    header_name = ''
```

- The **'number_of_pub_tests'** variable defines the total number of public tests.
- The **'points_per_pub_test'** variable defines the amount of points each public test is worth.
- The **'number_of_pub_tests_needed_to_pass'** variable defines the number of public test the student needs to pass in order to meet GFA requirement.
- The **'header_name'** variable defines the name of the sub-column for autograded projects.

Here is an example of what the variables could look like:

```python
    number_of_pub_tests = 15
    points_per_pub_test = 2
    number_of_pub_tests_needed_to_pass = 8
    header_name = 'T'
```

Since we are handling an autograded project, it is **very** important to change the value of the **autograded** variable from 
```python
    autograded = False
```
to 
```python
    autograded = True
```

Once you have changed all the necessary variables, you can run the script.


## Uploading Results to Grades Server

Once you have ran the script above, you will have a CSV file that was generated displaying the results. You can use this file to upload the results to the grades server.

1. Select the **'Up-load Scores'** section on the left side of the grades server

2. We are going to use the **'Load scores from a text file'** section. 
    - For the **'Assignment'** drop down selection, select **Assignment In File (no sub-parts)**
    - For the **'Scores File'**, locate the CSV file that was generated by the script on your local computer

3. Hit the **'Upload Scores'** button.