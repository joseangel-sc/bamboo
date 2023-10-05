class Series:
    def __init__(self, data):
        self.values = []
        self.dtype = None
        self.generate_values(data)

    def generate_values(self, data):
        data_types = set()
        for value in data:
            if value is None:
                self.values.append(value)
            else:
                data_types.add(type(value))
                if len(data_types) > 1:
                    raise Exception(f"Only one type (and None) is allowed in a Series got {data_types}")
                else:
                    self.values.append(value)

        self.dtype = data_types.pop()

    def __str__(self):
        values = []
        for i, value in enumerate(self.values):
            values.append(f"{i}    {str(value)}")

        return "\n".join(values) + f"\ndtype: {self.dtype}"

    def __repr__(self):
        return self.__str__()
