#todo
#add error handling 

import json


def d3Format1(title, xlabel, ylabel, datasets, x_range=False, y_range=False):
	data = {}
	data['meta'] = {}
	data['sets'] = []
	x_range_calc = [0,0]
	y_range_calc = [0,0]
	for s in datasets:
		data['sets'].append({"name": s['label'],"values": [{'x': x,'y' :y} for x,y in zip(s['x'],s['y'])]})
		if x_range == False:
			if min(s['x']) < x_range_calc[0]:
				x_range_calc[0] = min(s['x'])
			if max(s['x']) > x_range_calc[1]:
				x_range_calc[1] = max(s['x'])
		if y_range == False:
			if min(s['y']) < y_range_calc[0]:
				y_range_calc[0] = min(s['y'])
			if max(s['y']) > y_range_calc[1]:
				y_range_calc[1] = max(s['y'])
	data['meta']['title'] = title
	data['meta']['xlabel'] = xlabel
	data['meta']['ylabel'] = ylabel
	if x_range:
		data['meta']['xrange'] = x_range
	else:
		data['meta']['xrange'] = x_range_calc
	if y_range:
		data['meta']['yrange'] = y_range
	else:
		data['meta']['yrange'] = y_range_calc

	return data


def d3JSON(name,data):   
    with open(name+'.js', 'w+') as outfile:
        outfile.write("var " + name + " = ")
        json.dump(data, outfile, indent=4)


plot_title = 'Normalized Metric versus Other Metric'
y_axis = 'Normalized Metric'
x_axis = 'Other Metric'
#record1a = {'label':'first data set','data': [{'x':0.1,'y':1.2},{'x':0.2,'y':5},{'x':0.4,'y':0}]}
#record2a = {'label':'second data set','data': [{'x':0.2,'y':1.2},{'x':0.6,'y':8.77},{'x':-10,'y':20}]}
#record3a = {'label':'third data set','data': [{'x':0.3,'y':1.2},{'x':-0.2,'y':9.2},{'x':0.3,'y':0.1}]}
record1 = {'label':'first data set','x':[0.1,0.2,0.4],'y':[1.2,5,0]}
record2 = {'label':'second data set','x':[0.2,0.6,0.8],'y':[12,12,12]}  
record3 = {'label':'third data set','x':[0.3,0.7,0.9],'y':[8,5,0]}
record3 = {'label':'t22','x':[0.3,0.7,0.9],'y':[8,2,0]}
record4 = {'label':'thir2ata set','x':[0.2,0.7,0.9],'y':[8,5,0]}
record5 = {'label':'third2a set','x':[0.3,0.7,0.2],'y':[8,5,0]}
records = [record1,record2,record3,record4,record5]

ram_data = d3Format1(plot_title, x_axis, y_axis, records)
d3JSON('test_data2', ram_data)