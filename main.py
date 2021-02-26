import pandas as pd
import matplotlib

# path = 'C:/Users/blue/Downloads/HalteEinAus.att'
path = 'C:/Users/blue/Downloads/fpf_roh.att'


def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=37, sep=';')
    # print(attfile)
    return ret_att

def removeDoubleTimetable(timeDF):
    find_doubles = timeDF.duplicated(subset=['DEP','LINENAME','DIRECTIONCODE'], keep='first')
    timeDF['CM_DELETE'] = find_doubles.astype(int)
    return timeDF

work_thing = attribut2dataframe(path)

for col in work_thing:
    print(col)

removeDoubleTimetable(work_thing).to_csv(path_or_buf='C:/Users/blue/Downloads/fpf_witthDEL.att', sep=';',index=False)

# ax = work_thing.nlargest(20, 'PASSBOARD_TSYS(ICE,AP)').plot.bar(x='NAME', y='PASSBOARD_TSYS(ICE,AP)', rot=70)
# matplotlib.pyplot.savefig('out.png')