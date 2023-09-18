overs = int(input("enter overs bowled by bowler"))

runs_given = int(input("enter the runs given by bowler"))


def economy(runs_given,overs):
    
    
    
    globals()['eco'] =  runs_given / overs
    
    return True


if economy(runs_given,overs):
    print(f"bowlers economy is {eco}")
else:
    print('enter proper details')