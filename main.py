import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# path = 'C:/Users/blue/Downloads/HalteEinAus.att'
# path = 'C:/Users/blue/Downloads/fpf_roh.att'
path = 'C:/Users/chris/proj-lvm_files/EinsteigerVSySDiff.att'

def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=findFirstLine(attfile), sep=';', encoding='ansi', index_col=0)#'$STOP:NO')
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
    return np.sqrt( ( 2 * np.power((model-measure), 2) ) / (model + measure) )

print('GEH: ', GEH(1,1))

print(np.power((2+2), 2,))

df = attribut2dataframe(path)
print(df)

df = df[df['B_BAYERN']==1]



df.rename(columns={'NEU_EINST_N14': 'Calibration Count',
                   'PASSBOARD_TSYS(B,AP)': 'Bus',
                   'PASSBOARD_TSYS(F,AP)': 'Walk/Bike',
                   'PASSBOARD_TSYS(ICE,AP)': 'ICE',
                   'PASSBOARD_TSYS(RB,AP)': 'Regional Train',
                   'PASSBOARD_TSYS(S,AP)': 'S-Bahn',
                   'PASSBOARD_TSYS(SCHIFF,AP)': 'Boat',
                   'PASSBOARD_TSYS(T,AP)': 'Tram',
                   'PASSBOARD_TSYS(U,AP)': 'Metro'
                   }, inplace=True)
print(df)
df['SPNV'] = df['Regional Train'] + df['S-Bahn']

# todo: GEH value
df['Deviation'] = df['SPNV'] - df['Calibration Count']
df['GEH'] = GEH(df['SPNV'], df['Calibration Count'])

for col in df.columns:
    print(col, type(col))

# select specific row and relevant columns for bar plot

top_stations = np.array(df['PASSBOARD(AP)'].nlargest(10).index).tolist()

to_bar_group1 = df.loc[top_stations]



print('---begin to bar---')
print(to_bar_group1)



print('---end to bar---')


#fig = plt.figure()

#ax2 = fig.add_subplot(111)

fig, ax2 = plt.subplots()

# see: https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
colormap = plt.cm.get_cmap('tab20', 8)
# viridis = ['red', 'green', 'blue']
# print(colormap.colors, type(colormap.colors))

# see: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
ax2.set_facecolor('whitesmoke')

# pal1 = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71", "#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]
to_bar_group1.plot.bar(y=['S-Bahn', 'Regional Train', 'ICE', 'Tram', 'Metro', 'Bus', 'Walk/Bike', 'Boat'],
                       ax=ax2, width=0.45, position=0, color=colormap.colors, stacked=True)

to_bar_group1.plot.bar(x='NAME', y='Calibration Count', ax=ax2, width=0.45, position=1, color='gray')




# activate for frame SPNV
# to_bar_group1.plot.bar(x='NAME', y='SPNV', ax=ax2, width=0.1, position=0, edgecolor = "black", linewidth=2.5, fc="none")

ax2.grid(b=True, which='major', color='#666666', linestyle=':', alpha=0.2)
plt.title('Boardings per Mode of Transport at Different Stops')
plt.ylabel('Passengers [n]')
plt.xlabel('Station Name')
plt.xticks(fontsize=8)
fig.autofmt_xdate()

ax2.legend(loc='upper left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()

fig = ax2.get_figure()
fig.savefig('Barplot_Boardings.png')#, bbox_inches='tight')
plt.clf()

fig2, ax3 = plt.subplots()
df['GEH'].hist(bins=50, ax=ax3)
fig2 = ax3.get_figure()
plt.title('Counted and Modelled Passengers at Stops')
plt.ylabel('Frequency')
plt.xlabel('GEH value')
fig2.savefig('histogram_GEH.png')
plt.clf()

fig2, ax3 = plt.subplots()
df['GEH'].hist(bins=50, ax=ax3, label=r'$\sqrt{\frac{2(model-count)^2}{model+count}}$')
fig2 = ax3.get_figure()
plt.title('Deviation of Counted and Modelled Passengers at Stops')
plt.ylabel('Frequency')
plt.xlabel('GEH-weighted Deviation')
ax3.legend(loc='upper right')
fig2.savefig('histogram_GEH.png')
plt.clf()


abs_limit = max(df["Deviation"].max(), abs(df["Deviation"].min()))
fig2, ax3 = plt.subplots()
df['Deviation'].hist(bins=50, ax=ax3, range=(-abs_limit,abs_limit), label='model - count')

ax3.legend(loc='upper right')
fig2 = ax3.get_figure()

# ax3.legend('hello')

plt.title('Deviation of Counted and Modelled Passengers at Stops')
plt.ylabel('Frequency')
plt.xlabel('Absolute Deviation')
fig2.savefig('histogram_abs_deviation.png')
plt.clf()

fig2, ax3 = plt.subplots()
df['Calibration Count'].hist(bins=50, ax=ax3)
fig2 = ax3.get_figure()
plt.title('Empirical Data')
plt.ylabel('Frequency')
plt.xlabel('SPNV Counts')
fig2.savefig('histogram_SPNV_counts.png')
plt.clf()

print(df.nlargest(10,'GEH'))
print(df.nlargest(10,'Calibration Count')[['NAME', 'Calibration Count']])
print(df.nsmallest(10,'Calibration Count')[['NAME', 'Calibration Count']])



#newest version 2.1
