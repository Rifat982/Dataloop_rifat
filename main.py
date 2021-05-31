###Section 1
import datetime

import dtlpy as d1
if d1.token_expired():
    d1.login()
# project = d1.projects.create(project_name='rifat2')
project = d1.projects.get(project_name='rifat2')
# project.print()


###Section 2

##Upload 2 Images
#project.datasets.create(dataset_name='rifat_dataset')
dataset = project.datasets.get(dataset_name='rifat_dataset')
url_path = 'https://walksf.org/wp-content/uploads/2018/10/6th-street.jpg'
url_path2 = 'https://www.centreforcities.org/wp-content/uploads/2019/04/Sheffield_city_centre_x1650-1630x796.jpg'
link1 = d1.UrlLink(ref=url_path, mimetype='image', name='6th-street.jpg')
link2 = d1.UrlLink(ref=url_path2, mimetype='image', name='Sheffield_city_centre_x1650-1630x796.jpg')
dataset.items.upload(local_path=link1)
dataset.items.upload(local_path=link2)

##Classification
item = dataset.items.get(filepath='/Sheffield_city_centre_x1650-1630x796.jpg_link.json')
builder = item.annotations.builder()
annotations_definition = d1.Classification(label="manual")
builder.add(annotations_definition)
item.annotations.upload(builder)

###Section 4
item = dataset.items.get(filepath='/6th-street.jpg_link.json')
builder = item.annotations.builder()
annotations_definition = d1.Classification(label="auto")
builder.add(annotations_definition)
item.annotations.upload(builder)

###Section 5-6

##Add version to metadata
#version = 0
#item = dataset.items.get(filepath='/Sheffield_city_centre_x1650-1630x796.jpg_link.json')
#item.metadata['user'] = dict()
#item.metadata['user']['Vesrion'] = str(version)
#item = item.update()

##Increment version
item = dataset.items.get(filepath='/Sheffield_city_centre_x1650-1630x796.jpg_link.json')
item.metadata['user'] = dict()
vers = int(item.metadata.get['user']['Vesrion'])
vers+=1
item.metadata['user']['Vesrion'] = str(vers)
item = item.update()

###Section 7

##Upload 3rd image
url_path3 = 'https://rookstudio.files.wordpress.com/2015/05/dsc6762.jpg'
link3 = d1.UrlLink(ref=url_path3, mimetype='image', name='sfmta-170524_brannan_26-2500x750.jpg')
dataset.items.upload(local_path=link3)

##Add time metadata
dt = datetime.datetime.now()
item = dataset.items.get(filepath='/sfmta-170524_brannan_26-2500x750.jpg_link.json')
item.metadata['user'] = dict()
item.metadata['user']['CollectionTime'] = str(dt)
item = item.update()

