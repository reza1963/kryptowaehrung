from src.util.pandaz import Pandaz

pandaz = Pandaz("data/")
m, p, s = pandaz.dataframes()

print(" ***** mcap ***")
print(m)

print(" ***** price ***")
print(p)

print(" ***** supply ***")
print(s)

#pandaz.box_plot(s, "supply")
#pandaz.box_plot(m, "mcap")
#pandaz.box_plot(p, "price")

p = pandaz.group_by_cur(p)
merged_df = pandaz.merge(p, m)

print(" ***** merged ***")
print(merged_df)
