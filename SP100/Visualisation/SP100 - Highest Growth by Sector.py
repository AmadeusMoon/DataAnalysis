import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

dfGrowth = pd.read_csv('SP100/Tables/Economy.csv')

revenueSector = dfGrowth.groupby(
    'Sector')['Mean Revenue Growth per Industry'].sum() / dfGrowth.groupby('Sector')['Industry'].count()
meanGrowth = revenueSector.mean()

plt.figure(figsize=(10, 6))
ax = revenueSector.plot(kind='bar', color=['skyblue', 'orange', 'green'])
plt.axhline(y=meanGrowth, color='black',
            linestyle='--')

plt.title('Mean Revenue Growth by Sector')

plt.xlabel('Sector')

plt.ylabel('Mean Revenue Growth')

plt.xticks(rotation=45)

# Format y-axis labels to plain numbers
fmt = '{x:,.2f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

sector_labels = [f'{sector}: {value:,.2f}' for sector,
                 value in revenueSector.items()]
overall_label = f'Overall Mean: {meanGrowth:,.2f}'
plt.legend([*ax.patches, ax.lines[0]], sector_labels + [overall_label])

plt.savefig('SP100 - Mean Revenue Growth by Sector.png', bbox_inches='tight')
