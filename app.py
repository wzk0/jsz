import json
import os
import sys
import datetime

def read_from_data():
	with open('data.json','r')as f:
		return json.loads(f.read())

def write_in_data(data):
	with open('data.json','w')as f:
		f.write(json.dumps(data,ensure_ascii=False))

def new(thing):
	old_data=read_from_data()
	old_data.append({'point':thing,'time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
	write_in_data(old_data)

def new_input():
	os.system('micro temp')
	with open('temp','r')as f:
		data=f.read()
		os.system('rm temp')
		return '\n'.join(data.split('\n')[:-1])

def make_readme():
	data=read_from_data()
	os.system('rm README.md')
	with open('README.md','a')as f:
		f.write('## 便当的驾考知识点\n\n')
		for d in data:
			f.write('**%s**\n> 记录时间: %s\n\n'%(d['point'],d['time']))

def main():
	while True:
		user=new_input()
		if user=='q':
			sys.exit()
		else:
			new(user)

make_readme()