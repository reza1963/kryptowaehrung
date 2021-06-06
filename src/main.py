from src.util.pandaz import Pandaz

import warnings
warnings.filterwarnings("ignore")

pandaz = Pandaz("data/", 2020)
m, p, s = pandaz.dataframes()

p = pandaz.group_by_cur(p)
merged_df = pandaz.merge(p, m)
print(merged_df)

WEEK_OF_YEAR = 1
pandaz.weekly_mean(s, WEEK_OF_YEAR, "supply")
pandaz.weekly_mean(m, WEEK_OF_YEAR, "mcap")
pandaz.weekly_mean(p, WEEK_OF_YEAR, "price")


#pandaz.box_plot(s, "supply")
#pandaz.box_plot(m, "mcap")
#pandaz.box_plot(p, "price")
