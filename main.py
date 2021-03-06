import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# path = 'C:/Users/blue/Downloads/HalteEinAus.att'
# path = 'C:/Users/blue/Downloads/fpf_roh.att'
path = 'C:/Users/blue/Downloads/EinsteigerVSySDiff.att'

def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=findFirstLine(attfile), sep=';', encoding='ansi', index_col='$STOP:NO')
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


df = attribut2dataframe(path)

for col in df.columns:
    print(col, type(col))

# select specific row and relevant columns for bar plot

to_bar_group1 = df.loc[[1877, 2513]]

print('---begin to bar---')
print(to_bar_group1)

to_bar_group1['SPNV'] = to_bar_group1['PASSBOARD_TSYS(RB,AP)'] + to_bar_group1['PASSBOARD_TSYS(S,AP)']
print('---end to bar---')


#fig = plt.figure()

#ax2 = fig.add_subplot(111)

fig, ax2 = plt.subplots()

to_bar_group1.plot.bar(y=['PASSBOARD_TSYS(RB,AP)', 'PASSBOARD_TSYS(S,AP)', 'PASSBOARD_TSYS(B,AP)', 'PASSBOARD_TSYS(F,AP)', 'PASSBOARD_TSYS(ICE,AP)', 'PASSBOARD_TSYS(SCHIFF,AP)', 'PASSBOARD_TSYS(T,AP)', 'PASSBOARD_TSYS(U,AP)'],
                       ax=ax2, width=0.1, position=0, stacked=True)

to_bar_group1.plot.bar(x='NAME', y='NEU_EINST_N14', ax=ax2, width=0.1, position=1)

to_bar_group1.plot.bar(x='NAME', y='SPNV', ax=ax2, width=0.1, position=0, edgecolor = "black", linewidth=2.5, fc="none")
ax2.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)
plt.title('Boardings per Mode of Transport at Different Stops')
plt.ylabel('Passengers [n]')
plt.xlabel('Station Name')
fig.autofmt_xdate()

ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()

fig = ax2.get_figure()
fig.savefig('figure.png')#, bbox_inches='tight')

