# Exercises
minTime and findSubstring problem solving

minTime --> Given a file, input, and number of cores; find the minimum time required to process all the files. 

Process time is the time interval that a single processor processes the lines in a file, which can be considered as serial processing. In order to decrease the processing time, if the length of the lines in a file can be divided into a number of cores, then this file can be processed parallelly. 
In this case, total process time will be a summation of each file process time, either serial or parallel. 
However when there is a limit to parallelize the number of the files, then a file that minimizes the total process time should be chosen.

For example when there is n = 5 (number of the files) with length of lines [4, 1, 3, 2, 8], number of cores numCores = 4 and there is a limit = 1, the optimum process time should be totalTime = 4 + 1 + 3 + 2 + (8/4) = 12. Since only one file can be parallelized and the minimum process time can be reached when the fifth file is paralyzed, the total process time can be calculated as 12.


findSubstring --> Given a string and a length for substring, find a substring that has the highest amount of vowels. If there is no vowel in the given string, the message of "No Output!" must be printed. If there is more than one substring that fits the definition, then return the first substring as index-wise. 

For example, a word given as 'caberqiitefg' and length for the substring k = 5 is given, then the program should return the substring 'erqii'. If another word 'sdgnmb' and k = 3 is given, then the program should return 'Not found!'
