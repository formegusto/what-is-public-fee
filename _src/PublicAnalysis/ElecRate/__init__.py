import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class ElecRate:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def get_kwh(self, start_mean_kwh=0, end_mean_kwh=250, mean_inc=1):
        matplotlib.rc('font', family='AppleGothic')
        plt.rcParams['axes.unicode_minus'] = False

        calc = self.analyzer.calc
        household_count = calc.household_count
        household_kwh = calc.household_kwh

        start_kwh = start_mean_kwh
        end_kwh = household_count * end_mean_kwh
        inc = household_count * mean_inc

        public_mean_range = range(start_mean_kwh, end_mean_kwh, mean_inc)
        public_range = range(start_kwh, end_kwh, inc)

        result = None
        for public_kwh in public_range:
            apt = household_kwh + public_kwh
            self.analyzer.set_calc(kwh=apt)
            bill_table = self.analyzer.bill_table.get

            elec_rates = bill_table[['전력량요금']].to_numpy()[:3]
            if result is None:
                result = elec_rates
            else:
                result = np.append(result, elec_rates, axis=1)

        plt.figure(figsize=(16, 8))
        indexes = ['APT 전력량요금', '세대부 전력량요금', '공용부 전력량요금']
        palette = plt.cm.get_cmap("Set1", result[:, 0].size)
        for idx, index_name in enumerate(indexes):
            plt.plot(public_mean_range, result[idx], c=palette(
                idx), label=index_name, alpha=1)

        plt.title("공용부 사용량 증가에 따른 전력량요금 변화")
        plt.ylabel("요금")
        plt.xlabel("공용부 kWh")
        plt.legend(loc='upper left')
        plt.show()
        return pd.DataFrame(result, columns=["{}kWh".format(_) for _ in public_mean_range], index=indexes)
