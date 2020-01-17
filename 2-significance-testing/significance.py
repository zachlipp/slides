import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from scipy import stats


def report_significant_results(
    data: DataFrame, group_field: str, value_field: str, max_subgroups: int
) -> None:
    """
    Given dataframe and the names of a continuous value series and a discrete
    grouping series, find if subgroups within that groups have significant
    differences between the rest of the data using one-way ANOVA
    """
    # Get the top N most populated subgroups
    most_popular_subgroups = (
        data[group_field].value_counts()[:max_subgroups].index.tolist()
    )

    significant = 0
    for subgroup in most_popular_subgroups:
        subgroup_index = data[group_field] == subgroup

        subgroup_data = data.loc[subgroup_index, value_field].values
        non_subgroup_data = data.loc[~subgroup_index, value_field].values

        # One way ANOVA test
        anova = stats.f_oneway(subgroup_data, non_subgroup_data)

        if anova.pvalue <= 0.05:
            print(f"Significant result! {subgroup} (p={anova.pvalue})")
            significant += 1

    percent_significant = np.round(
        significant / len(most_popular_subgroups) * 100, 2
    )

    print("\n", "-" * 50, "\n")

    print(
        f"In total, {percent_significant}% of results are statistically "
        "significantly different.\n"
        f"If there were no differences between groups, we'd expect 5% "
        "of results to differ at this level by chance alone."
    )


if __name__ == "__main__":
    np.random.seed(1337)
    df = pd.read_csv(
        "https://data.cityofchicago.org/api/views/xzkq-xp2w/rows.csv?accessType=DOWNLOAD"
    )

    salaried = df[df["Salary or Hourly"] == "Salary"]
    print(salaried.head())
    print(salaried.shape)

    salaried["last_name"] = salaried["Name"].str.replace(r",[\s\S]+", "")

    report_significant_results(salaried, "Department", "Annual Salary", 100)

    report_significant_results(salaried, "last_name", "Annual Salary", 100)

    salaried.loc[:, "random"] = np.random.normal(size=salaried.shape[0])
    report_significant_results(salaried, "last_name", "random", 500)
