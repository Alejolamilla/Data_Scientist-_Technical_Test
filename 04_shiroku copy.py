from os import getenv
import shimoku_api_python as Shimoku

access_token = getenv('20e10bd5-f628-466b-a9fc-ec1ca395e9dd')
universe_id: str = getenv('c2edae80-3e21-4f15-8c51-c394b34475cf')
workspace_id: str = getenv('e96f1077-ae84-4068-9333-457b5d65ec37')

s = Shimoku.Client(
    local_port=8080,
    async_execution=True,
    verbosity='INFO', 
)
# Necessary for compatibility with cloud execution
s.set_workspace() 

# Set the group of the menu
s.set_board('Custom Board')

# Set the menu path 'catalog' with the sub-path 'bar-example'
s.set_menu_path('catalog', 'bar-example')

language_expressiveness = [
    {'Language': 'C', 'Statements ratio': 1.0, 'Lines ratio': 1.0},
    {'Language': 'C++', 'Statements ratio': 2.5, 'Lines ratio': 1.0},
    {'Language': 'Fortran', 'Statements ratio': 2.0, 'Lines ratio': 0.8},
    {'Language': 'Java', 'Statements ratio': 2.5, 'Lines ratio': 1.5},
    {'Language': 'Perl', 'Statements ratio': 6.0, 'Lines ratio': 6.0},
    {'Language': 'Smalltalk', 'Statements ratio': 6.0, 'Lines ratio': 6.25},
    {'Language': 'Python', 'Statements ratio': 6.0, 'Lines ratio': 6.5},
]

s.plt.bar(
    order=0, title='Language expressiveness',
    data=language_expressiveness, x='Language',
    y=['Statements ratio', 'Lines ratio'],
)

# Necessary for notifying the front-end even if not using async execution
s.run()

# Close the server in the port 8080
#s.terminate_local_server()