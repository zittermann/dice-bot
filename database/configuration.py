import yaml

def load():

	stream = open('config.yml', 'r')
	dict = yaml.full_load(stream)

	return dict
