import pandas as pd
import matplotlib.pyplot as plt

# path = 'C:/Users/blue/Downloads/HalteEinAus.att'
# path = 'C:/Users/blue/Downloads/fpf_roh.att'
path = 'C:/Users/blue/Downloads/EinsteigerVSySDiff.att'

def attribut2dataframe(attfile):
    ret_att = pd.read_csv(attfile, skiprows=findFirstLine(attfile), sep=';', encoding='ansi')
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

# ax = df.plot.bar(x='lab', y='val', rot=0)


print(df.head())
for col in df.columns:
    print(col)


# select specific row and relevant columns for bar plot

to_bar_group1 = df.loc[df['$STOP:NO'] == 1877].iloc[:, range(2, 12)]

print(to_bar_group1, type(to_bar_group1))


# plot all stuff as stacks

plt.style.use('ggplot')

fig, ax = plt.subplots()
# df[['a', 'c']].plot.bar(stacked=True, width=0.1, position=1.5, colormap="bwr", ax=ax, alpha=0.7)
to_bar_group1.iloc[:, range(0, 3)].plot.bar(stacked=True, width=0.1, position=1.5, colormap="bwr", ax=ax, alpha=0.7)
# df[['b', 'd']].plot.bar(stacked=True, width=0.1, position=-0.5, colormap="RdGy", ax=ax, alpha=0.7)
to_bar_group1.iloc[:, range(4, 6)].plot.bar(stacked=True, width=0.1, position=-0.5, colormap="RdGy", ax=ax, alpha=0.7)
# df[['a', 'd']].plot.bar(stacked=True, width=0.1, position=0.5, colormap="BrBG", ax=ax, alpha=0.7)
to_bar_group1.iloc[:, range(7, 8)].plot.bar(stacked=True, width=0.1, position=0.5, colormap="BrBG", ax=ax, alpha=0.7)
plt.legend(loc="upper center")
# plt.show()

# ax = to_bar_group1.plot.bar(stacked=True)
# ax.plot()
fig = ax.get_figure()
fig.savefig('figure.png')