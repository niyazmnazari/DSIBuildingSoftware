# This an example of calling this Python file: python pythonfile.py -f red -e k -o buildingscore.png
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import yaml
import logging

#Refactoring 
def LoadData(filepath):
    try:
        return pd.read_csv(filepath)
        logging.info(f'Successfully loaded {filepath}')
    except Exception as e:
        logging.error('Error loading dataset', exc_info=e)
        raise e.add_note('Please enter a valid dataset path.')
    
#Parser Argument
parser = argparse.ArgumentParser(description='Building Score upon Building Year')
parser.add_argument('--fcolor', '-f' , type=str, help='Plot Fore Color' ,default='red')
parser.add_argument('--ecolor', '-e' , type=str, help='Plot Edge Color',default='k')
parser.add_argument('--outputfile', '-o', type=str, help='Output plot filename',default='plot.png')
parser.add_argument('--verbose', '-v', action='store_true',default='')
args = parser.parse_args()

#Define lo file to keep errors and warnings
if args.verbose:
    logging_level = logging.INFO
else:
    logging_level = logging.WARNING

logging.basicConfig(
    handlers=(logging.StreamHandler(), logging.FileHandler('my_python_analysis.log')), 
    level=logging.INFO,
    )


#Load Configuration File
config_files = ['userconfig.yml']
config = {}

with open('userconfig.yml', 'r') as yamlfile:
    config = yaml.safe_load(yamlfile)
        

dataset_url = config['dataset']
dr = LoadData(dataset_url)


fig , ax = plt.subplots()
ax.set_title(config['plot_config']['title'])
ax.set_xlabel(config['plot_config']['xlabel'])
ax.set_ylabel(config['plot_config']['ylabel'])
ax.set_axisbelow(True)           
ax.grid(alpha = 0.7 )

plt.scatter(dr['YEAR BUILT'] , dr['CURRENT BUILDING EVAL SCORE'] , marker='s' , facecolor='red' , edgecolors='k')

plt.savefig(args.outputfile)