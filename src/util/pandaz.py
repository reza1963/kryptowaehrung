import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pds
from src.util.constant import Constant


class Pandaz:
    csv_files = dict({"mcap": "Top100_MCap.csv", "price": "Top100_Prices.csv", "supply": "Top100_Supply.csv"})
    path = "../data/"

    def __init__(self, path):
        self.path = path

    def dataframes(self):
        mcap = pds.read_csv(self.path + self.csv_files["mcap"])
        prices = pds.read_csv(self.path + self.csv_files["price"])
        supply = pds.read_csv(self.path + self.csv_files["supply"])

        prices = pds.melt(prices, id_vars=[Constant.DATE_COL], value_vars=prices.columns[1:], var_name="cur", value_name="price")
        supply = pds.melt(supply, id_vars=[Constant.DATE_COL], value_vars=supply.columns[1:], var_name="cur", value_name="supply")
        mcap = pds.melt(mcap, id_vars=[Constant.DATE_COL], value_vars=mcap.columns[1:], var_name="cur", value_name="mcap")

        mcap, prices, supply = self.create_and_set_index(mcap, prices, supply)

        return mcap, prices, supply

    def create_and_set_index(self, mcap, prices, supply):
        mcap[Constant.DATE_INDEX] = pds.to_datetime(mcap[Constant.DATE_COL])
        mcap = mcap.set_index(pds.DatetimeIndex(mcap[Constant.DATE_INDEX]))

        prices[Constant.DATE_INDEX] = pds.to_datetime(prices[Constant.DATE_COL])
        prices = prices.set_index(pds.DatetimeIndex(prices[Constant.DATE_INDEX]))

        supply[Constant.DATE_INDEX] = pds.to_datetime(supply[Constant.DATE_COL])
        supply = supply.set_index(pds.DatetimeIndex(supply[Constant.DATE_INDEX]))

        return mcap, prices, supply

    def box_plot(self, df, col):
        sns.set(rc={'figure.figsize': (15, 5)})
        df[Constant.DATE_INDEX] = df.index.month_name()
        sns.boxplot(data=df, x=Constant.DATE_INDEX, y=col)

        plt.show()

    def group_by_cur(self, df):
        # TODO: Why shift ?
        df[Constant.PRICEY_COL] = df.groupby(Constant.CURRENC_COL)[Constant.PRICE_COL].shift(periods=1)
        df[Constant.RETUTN_COL] = (df[Constant.PRICE_COL] / df[Constant.PRICEY_COL]) - 1

        return df

    def merge(self, df1, df2):
        df = pds.merge(df1, df2, how="left", on=[Constant.DATE_COL, Constant.CURRENC_COL])
        df.drop('date_idx_y',  axis='columns', inplace=True)
        # TODO: test
        df = df[~pds.isna(df[Constant.RETUTN_COL])]
        df[Constant.MCAP_AGG_COL] = df.groupby(Constant.DATE_COL)[Constant.MCAP_COL].transform("sum")
        # Calc weight for each currency's daily return by its mcap normalized by market mcap
        df[Constant.WEIGHT_RETURN_COL] = df[Constant.RETUTN_COL] * df[Constant.MCAP_COL] / df[Constant.MCAP_AGG_COL]
        # Collapse it at the day level
        df[Constant.WEIGHT_RETURN_AGG_COL] = df.groupby(Constant.DATE_COL)[Constant.WEIGHT_RETURN_COL].transform("sum")

        return df[[Constant.DATE_COL, Constant.WEIGHT_RETURN_AGG_COL]].drop_duplicates()