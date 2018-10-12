'''
Created on 12-Oct-2018

@author: 10086
'''
sports = 'cricket-vollyball-baseball-golf-basketball -badminton'
sports = (sports.split('-'))
sports.sort()
sports = '-'.join(sports)
print(sports) 
