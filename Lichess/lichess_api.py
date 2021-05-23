import lichess.api

user = lichess.api.user('LabBrat')
print(user.get('perfs', {}).get('blitz', {}).get('rating'))

games = lichess.api.user_games('LabBrat', max=50, perfType='blitz')
print(next(games)['moves'])
