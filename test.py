
try:
    logweek = 2104

    report = "testing text"

    #fileName = 'WCC (KT Report) - LW{0}.txt'.format(str(logweek))
    #with open(fileName, 'w') as f:
    #with open('C:\Users\MohamadYusuf\Desktop\Haikal\Personal Projects\cerberus-check\WCC (KT Report) - LW{0}.txt'.format(str(logweek)), 'w') as f:
    #import os
    #fileName = os.getcwd() + '\\' + fileName
    #with open(os.getcwd + 'WCC (KT Report) - LW%s.txt' % (str(logweek),), 'w') as f:

    with open('C:\\Users\\MohamadYusuf\\Desktop\\Haikal\\Personal Projects\\cerberus-check\\WCC (KT Report) - LW%s.txt' % (str(logweek),), 'w') as f:    
        f.write(report)

except Exception as e:
    print(e)
    print("Error caught")
