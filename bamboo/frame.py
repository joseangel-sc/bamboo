from bamboo.series import Series


class DataFrame:
    def __init__(self, data: list):
        self.data = data
        self.df = self.make_df()

    def make_df(self):
        column_names = self.data[0].keys()
        # emtpy array with the same number of empty arrays as there are columns
        list_of_future_series = [[] for _ in range(len(column_names))]
        for i, row in enumerate(self.data):
            if row.keys() != column_names:
                raise ValueError("All rows must have the same keys")
            for j, column_name in enumerate(column_names):
                list_of_future_series[j].append(row[column_name])
        df = {}
        for column_name, series in zip(column_names, list_of_future_series):
            df[column_name] = Series(series, type(series[0]))

        return df

    def __str__(self):
        # Compute column widths for alignment
        col_widths = {
            col: max(len(str(col)), max(len(str(val)) for val in self.df[col].series))
            for col in self.df
        }

        # Header row
        header = " | ".join(str(col).ljust(col_widths[col]) for col in self.df)
        separator = "-+-".join("-" * col_widths[col] for col in self.df)

        # Data rows
        rows = []
        for i in range(len(self.data)):
            row = " | ".join(
                str(self.df[col].series[i]).ljust(col_widths[col]) for col in self.df
            )
            rows.append(row)

        return "\n".join([header, separator] + rows)


if __name__ == '__main__':
    data = [
        {'name': 'John', 'age': 23},
        {'name': 'Jane', 'age': 25},
        {'name': 'Joe', 'age': 21},
    ]
    df = DataFrame(data)
    print(df)

