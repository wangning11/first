print('2017~2018赛季NBA西部联盟前8名:')
team_dict = {1:'火箭',2:'勇士',3:'开拓者',4:'爵士',5:'鹈鹕',6:'马刺',7:'雷霆',8:'森林狼'}
for i,a in enumerate(team_dict):
    if i%2 == 1:
        print('%s'%team_dict[a],end = '\n')
    else:
        print('%s'%team_dict[a],end ='\t')
print('')

