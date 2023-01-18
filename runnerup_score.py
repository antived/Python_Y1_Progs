# AdAstra 2022-23 problem-2
# program to find 2nd highest score of runner's up in javelin throw, given an array of scores
# - vedant dutta

def RunnerUp(scoreArr):
    # Remove duplicate from scoreArr to get array with unique values
    uniqScoreArr = list(set(scoreArr))
    
    # Sort the array of unique scores in descending order such that
    # 0th item will be highest, 1st item will be 2nd highest
    uniqScoreArr.sort(reverse=True)
    
    # Return the 2nd highest score
    return uniqScoreArr[1]

# main()

# take a sample array of score, which has duplicate highest scores
sampleScoreArray = [56, 73, 73, 65, 69, 62]

# get the RunnerUp() score
scoreOfRunnerUp = RunnerUp(sampleScoreArray)

# print the score
print(scoreOfRunnerUp)

