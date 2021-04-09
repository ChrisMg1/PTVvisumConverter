import pandas as pd
import numpy as np
from matplotlib import cm



def attribut2dataframe(attfile, myindex):
    ret_att = pd.read_csv(attfile, skiprows=findFirstLine(attfile), sep=';', 
                          encoding='ansi', index_col=myindex)
    # print(attfile)
    return ret_att


def removeDoubleTimetable(timeDF):
    find_doubles = timeDF.duplicated(subset=['DEP','LINENAME','DIRECTIONCODE'], keep='first')
    timeDF['CM_DELETE'] = find_doubles.astype(int)
    return timeDF


def findFirstLine(arrfile):
    dollar_count = 0
    line_count = 0
    with open(arrfile, 'r') as file1:
        line = file1.readline()
        while dollar_count < 2:
            line_count = line_count + 1
            line = file1.readline()
            # print(line)
            if line[:1] == "$":
                dollar_count = dollar_count + 1
                # print("found dollar")
                # print(dollar_count)
        # print(line)
        return line_count


def GEH(model, measure):
    return np.sqrt( ( 2 * np.power((model - measure), 2) ) / (model + measure) )

cmap1 = cm.get_cmap('coolwarm') # Colour map (there are many others)

# Dictionary to replace german terms
VSYS_aliases = {
  'Bus': 'Bus',
  'Fernbus': 'Long Distance Bus',
  'ÖVFuss': 'Foot',
  'ICE/IC': 'ICE/IC',
  'RB/RE': 'Regional Train',
  'S-Bahn': 'Commuter Train',
  'Seilbahn 30kmh': 'Cable Car',
  'Schiff': 'Boat',
  'Tram': 'Tram',
  'U-Bahn': 'Metro',
  'Urban Air Mobility 200kmh': 'UAM'
}

idx_aliases = {
  'B': 'Bus',
  'F': 'Long Distance Bus',
  'Fuss': 'Foot',
  'ICE': 'ICE/IC',
  'RB': 'Regional Train',
  'S': 'Commuter Train',
  'SB30': 'Cable Car',
  'Schiff': 'Boat',
  'T': 'Tram',
  'U': 'Metro',
  'UAM200': 'UAM'
}


