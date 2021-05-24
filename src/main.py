from src.util.pandaz import Pandaz

pandaz = Pandaz("data/")
m, p, s = pandaz.dataframes()

#pandaz.box_plot(s, "supply")
#pandaz.box_plot(m, "mcap")
#pandaz.box_plot(p, "price")

p = pandaz.group_by_cur(p)

merged_df = pandaz.merge(p, m)
print(merged_df)
