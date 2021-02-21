import pandas as pd
import matplotlib

path = 'C:/Users/blue/Downloads/HalteEinAus.att'


def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=44, sep=';')
    # print(attfile)
    return ret_att


work_thing = attribut2dataframe(path)

for col in work_thing:
    print(col)


ax = work_thing.nlargest(20, 'PASSBOARD_TSYS(ICE,AP)').plot.bar(x='NAME', y='PASSBOARD_TSYS(ICE,AP)', rot=70)

# df = pd.DataFrame({'lab':['A', 'B', 'C'], 'val':[10, 30, 20]})
# ax = df.plot.bar(x='lab', y='val', rot=0)
# matplotlib.pyplot.show()

matplotlib.pyplot.savefig('out.png')