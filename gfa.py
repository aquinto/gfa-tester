# Created by Alexander Quinto
import pandas as pd
import time

def generate_pub_tests(total, points_per_tests, string):
    columns = {}
    for i in range(1, total+1):
        columns.update({string+str(i) : points_per_tests})
    return columns


def check_gfa(ID, r, assignment, points_to_pass, comment_pass, comment_fail):
    if r >= points_to_pass:
        return {'login':ID, 'assignment':assignment, 'score': 1, 'comment': comment_pass}
    else:
        return {'login':ID, 'assignment':assignment, 'score': 0, 'comment': comment_fail}


def main(input_file_name, output_file_name, requirements, points_needed_to_pass_gfa, comment_pass, comment_fail, assignment):
    start = time.time()
    print("Generating GFA results for " + assignment+"....")
    df = pd.read_csv(input_file_name, header=[1])
    column_names = ['DirectoryID'] + list(requirements.keys())
    filtered_df = df[column_names]
    filtered_df.set_index('DirectoryID', inplace=True)
    filtered_df = filtered_df.sum(axis=1).to_frame()
    filtered_df.reset_index(inplace= True)
    filtered_df = filtered_df.rename(columns={0:'Total'})
    generate_final_df = filtered_df.apply(lambda x: check_gfa(x.DirectoryID, x.Total, assignment, points_needed_to_pass_gfa, comment_pass, comment_fail), axis =1, result_type = 'expand')
    generate_final_df.to_csv(output_file_name, index = False)
    end = time.time()
    print("Done! This took: " + str(end-start) + " seconds")


# CHANGE THE VALUES BELOW AS YOU CHECK GFA FOR OTHER PROJECTS

#original csv file downloaded from grades server
input_file_name = 'grades-gfa.csv'

#gfa requirements for given assignment, key value should be the requirement title as listed in the grades server
#value should be the points necessary to pass the GFA requirement
#If it is an autograder projet with pub tests do this below
number_of_pub_tests = 6
points_per_pub_test = 1
number_of_pub_tests_needed_to_pass = 6
header_name = 'GFA'
columns = generate_pub_tests(number_of_pub_tests, points_per_pub_test, header_name)
points_total = number_of_pub_tests*points_per_pub_test

# if it is not an autograded project such as a Processing project, change the 'autograded' variable to False
# you will have to manually fill out the dictionary below since it is manually graded
manual_columns = {'MB' : 10, 'BT' : 15, 'PC' : 15, 'SG' : 5}
points_total_2 = sum(manual_columns.values())

#requirements will be used to filter columns from the original dataframe
#points_needed to pass gfa is the sum of the total of points a student needs to pass a GFA for a given project
autograded = True
requirements = columns if autograded else manual_columns
points_needed_to_pass_gfa = points_total if autograded else points_total_2

#assignment name for the GFA that is listed in the grades server. (Spring 2022 is GFA1,2,3,4 etc)
assignment = 'GFA'
comment_pass = 'all GFAs Passed'
comment_fail = 'some GFAs Failed'

#output file name for csv
output_file_name = 'GFAFinal_Results.csv'

#call main
main(input_file_name, output_file_name, requirements, points_needed_to_pass_gfa, comment_pass, comment_fail, assignment)
 
