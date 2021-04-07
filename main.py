import pandas as pd
import numpy as np


# todo: ersten 3 spalten als index; export KM ändern
def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=findFirstLine(attfile), sep=';', encoding='ansi', index_col=0)#[0, 1, 2])#'$STOP:NO')
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




