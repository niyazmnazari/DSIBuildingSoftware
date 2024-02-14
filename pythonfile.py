# This an example of calling this Python file: python pythonfile.py -f red -e k -o buildingscore.png
import pandas as pd 
import matplotlib.pyplot as plt 
import argparse
import yaml

#Parser Argument
parser = argparse.ArgumentParser(description='Building Score upon Building Year')
parser.add_argument('--fcolor', '-f' , type=str, help='Plot Fore Color')
parser.add_argument('--ecolor', '-e' , type=str, help='Plot Edge Color')
parser.add_argument('--outputfile', '-o', type=str, help='Output plot filename')
args = parser.parse_args()

#Load 
config_files = ['userconfig.yml']
config = {}

with open('userconfig.yml', 'r') as yamlfile:
    config = yaml.safe_load(yamlfile)
        

dr = pd.read_csv(config['dataset'])

fig , ax = plt.subplots()
ax.set_title(config['plot_config']['title'])
ax.set_xlabel(config['plot_config']['xlabel'])
ax.set_ylabel(config['plot_config']['ylabel'])
ax.set_axisbelow(True)           
ax.grid(alpha = 0.7 )

plt.scatter(dr['YEAR BUILT'] , dr['CURRENT BUILDING EVAL SCORE'] , marker='s' , facecolor=args.fcolor , edgecolors=args.ecolor)

plt.savefig(args.outputfile)