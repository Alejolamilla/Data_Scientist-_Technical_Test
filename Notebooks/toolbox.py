# This file contains useful functions used in the notebooks

import seaborn as sns
import matplotlib.pyplot as plt

def null_data_proportion(df):
    # seeing the null values proportion
    fg = df.isnull().melt().pipe(
        lambda df: (
            sns.displot(
                data=df,
                y="variable",
                hue="value",
                aspect=2,
                multiple = "fill"
            )
        )
    )

    for ax in fg.axes.ravel():
        # add annotations
        for c in ax.containers:
            # custom label calculates value and adds an empty string so 0 value bars don't have a number
            labels = [f'{w:.2f}' if (w := (v.get_width())*100) > 0 else '' for v in c]
            ax.bar_label(c, labels=labels, label_type='center', fontsize=8, rotation=0, padding=2)
        ax.margins(x=0.2)

    plt.show()
