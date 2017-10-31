import pandas as pd
import matplotlib.pyplot as plt

df_cpuo = pd.read_csv('cpuo.csv')

'''
Build and save two graphs.
'''
# These lines do the work.
plot_cpuo_1 = df_cpuo.plot()
plot_cpuo_2 = df_cpuo.plot(title='hello plot', kind='bar')

plt.ylabel('Iron Man')
plt.xlabel('Ant Man')

plot_cpuo_3 = df_cpuo.plot(title='Third Charm', kind='line')

# pass in [xmin, xmax, ymin, ymax]
plot_cpuo_3.axis([0,5,0,20])

# Give the x axis and y axis labels
plt.ylabel('Avengers')
plt.xlabel('X-Men')


# These lines save the files.
fig_cpuo_1 = plot_cpuo_1.get_figure()
fig_cpuo_1.savefig('cpuo-default.png')

fig_cpuo_2 = plot_cpuo_2.get_figure()
fig_cpuo_2.savefig('cpuo-bar.png')

fig_cpuo_3 = plot_cpuo_3.get_figure()
fig_cpuo_3.savefig('cpuo-line.png')


