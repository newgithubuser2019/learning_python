import requests
# import pprint
# import pygal
# from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# --------------------------------------------------------------------------------------------------------------------------------------------
# Make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:javascript&sort=stars"
r = requests.get(url)
print("------------------------------------------------------------------------------------------------------------")
print("\nStatus code:", r.status_code)  # A status code of 200 indicates a successful response
r.raise_for_status()

# Store API response in a variable
response_dict = r.json()
# print("\n")

# Process results
# print(response_dict.keys())
print("\nTotal repositories:", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
# pprint.pprint(repo_dicts)
print("\nRepositories returned:", len(repo_dicts))

# Examine the first repository
"""
repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
    # print(key)
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Number of forks:', repo_dict['forks_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
"""

# Examine repositories
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\n-------------------------------------------------------------------")
    print('\nName:', repo_dict['name'])
    # print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Number of forks:', repo_dict['forks_count'])
    print('Repository:', repo_dict['html_url'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])

# names, stars = [], []
names, plot_dicts = [], []
plot_dict = {}
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    description = repo_dict['description']
    if not description:
        description = 'No description provided'
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
# print(plot_dicts)

# --------------------------------------------------------------------------------------------------------------------------------------------
# Creating a visualization
"""
my_style = LS('# 333366', base_style=LCS)
#
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
#
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
# chart.add("", stars)
chart.add("", plot_dicts)
chart.render_to_file('requests_github_visualisation.svg')
exit()
"""
