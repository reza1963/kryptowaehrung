from src.util.pandaz import Pandaz

pandaz = Pandaz("data/")
m, p, s = pandaz.dataframes()

print(" ***** mcap ***")
print(m)

print(" ***** price ***")
print(p)

print(" ***** supply ***")
print(s)

pandaz.box_plot(s, "supply", 2020)
pandaz.box_plot(m, "mcap", 2020)
pandaz.box_plot(p, "price", 2020)

p = pandaz.group_by_cur(p)
merged_df = pandaz.merge(p, m)

print(" ***** merged ***")
print(merged_df)
