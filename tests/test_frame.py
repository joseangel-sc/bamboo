from bamboo.frame import DataFrame


def test_df_working():
    data = [
        {'name': 'John', 'age': 23},
        {'name': 'Jane', 'age': 25},
        {'name': 'Joe', 'age': 21},
    ]
    df = DataFrame(data)