import requests
import pygal

from operator import itemgetter
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#Make an API call and store the response.
url= 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Status code: ', r.status_code)

#Process information for each submissions.
submission_ids = r.json()
types, submission_dicts = [], []
for submission_id in submission_ids[:30]:

    #Make a separate API call for each submission.
    url= f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    #print(submission_r.status_code)
    response_dict = submission_r.json()
    types.append(response_dict.get('type', ''))

    submission_dict ={
        'value': response_dict.get('descendants', 0),
        'label': response_dict['title'],
        'xlink': f'http://news.ycombinator.com/item?id={submission_id}',

    }

    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,  key=itemgetter('value'), reverse=True)

'''for submission_dict in submission_dicts:
    print('\nTitle: ', submission_dict['label'])
    print('Discussion Link: ', submission_dict['xlink'])
    print('Comments: ', submission_dict['value'])'''

#Make Visualization.
my_style =LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart =pygal.Bar(my_config, style = my_style)
chart.title = 'Most-Active Discussions on Hacker News'
chart.x_labels = types

chart.add('', submission_dicts)
chart.render_to_file('Hacker_News_Discussions.svg')

