# algorithm-final-project
An API to work with some algorithms which developed by python and flask.

host => http://mhd78.pythonanywhere.com/

endpoints :
/strassen method=>POSTinput value should be in JSON format //eg "{"A":[[],...,[]] , "B":[[],...,[]]}"
/LCS?seq1=value&seq2=value method=>GET
/jobScheduling/count of jobs(user input)?jobs method=>GET//eg /2?job1=12&job2=22
/backtrackKnapsack method=>POSTinput value should be in JSON format //eg "{"capacity":20 , "weights":[10,5,20] ,"values":[5,7,3] }"
/branchAndBoundKnapsack method=>POSTinput value should be in JSON format //eg "{"capacity":20 , "weights":[10,5,20] ,"values":[5,7,3] }"
/DFS method=>POSTinput value should be in JSON format //eg "{"matrix":[] , "startVertex":2 }"
/bellmanFord method=>POSTinput value should be in JSON format //eg "{"matrix":[] , "vertices":4 , "startVertex":2 }"
