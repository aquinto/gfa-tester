# GFA Tester

The following script was written to calculate which students have met the GFA requirements for a given project. This was created during the Spring 2022 semester when I was TAing for CMSC131.

## Usage

The script was written to account for both manually graded and autograded projects. Manually graded projects such as Processing projects will contain different names for the requirements needed to pass a GFA for that given project, whereas, for autograded projects students only need to pass X amount of public tests to meet a GFA requirement.

### Usage: Handling Manually Graded Projects

I will be giving a usage case for manual projects below.  First, we need to determine the column names for each of the requirements needed to pass the GFA. 

1. In the **'View & Enter Scores'** section, you'll have all the assignments listed in the first row of the table presented.
    - Select the correct project listed in the grades server.
2. Once you selected the correct project, you will see the sub-columns for that given project along with the total possible points for those sub-columns.
    - Those sub-columns represent the requirements listed in the project description. 

    Below is an example of what a project's sub-columns could look like:

    <p align="center">
        <img src="img/columns.png" />
    </p>

3. Download the scores for the given project as a CSV file, be sure to check off 'Shown' for **Sub-scores for assignments** 
