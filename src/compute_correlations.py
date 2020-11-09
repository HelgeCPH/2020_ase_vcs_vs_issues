import sys
import pandas as pd
import matplotlib.pyplot as plt


def main(fname):
    df = pd.read_csv(fname)
    cols = list(df.columns)
    cols.remove("system")
    cols.remove("version")
    systems = df.system.unique()

    for system in systems:
        df_mini = df[df.system == system][cols]

        plt.matshow(df.corr("spearman"))
        plt.savefig(f"../output/{system}_corr_mat.png")


if __name__ == "__main__":
    # I expect that the versions are sorted increasingly
    fname = sys.argv[1]  # "data/test_correlations.csv"
    main(fname)
