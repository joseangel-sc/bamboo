from bamboo.series import Series


class DataFrame:
    def __init__(self, data: list):
        self.data = data
        self.df = self.make_df()

    def make_df(self) -> dict:
        column_names = self.data[0].keys()
        records = [[] for _ in range(len(column_names))]
        for record in self.data:
            if column_names != record.keys():
                raise Exception("Column names need to be the same for all the records")

            for i, value in enumerate(record.values()):
                records[i].append(value)

        df = dict()
        column_names = list(column_names)
        for i, column_record in enumerate(records):
            df[column_names[i]] = Series(column_record)

        return df

if __name__ == '__main__':
    data = [
        {'name': 'John', 'age': 23},
        {'name': 'Jane', 'age': 25},
        {'name': 'Joe', 'age': 21},
    ]
    df = DataFrame(data)
    print(df)
