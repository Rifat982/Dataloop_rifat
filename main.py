import dtlpy as d1
if d1.token_expired():
    d1.login()
# project = d1.projects.create(project_name='rifat2')
project = d1.projects.get(project_name='rifat2')
project.print()