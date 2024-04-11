# ValueError: Length mismatch: Expected axis has X elements, new values have Y elements

import pandas as pd


df = pd.DataFrame(
    {
        'id': [112, 113, 114, 115],
        'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    }
)

df.columns = ['id', 'first_name']

#     id first_name
# 0  112      Alice
# 1  113      Bobby
# 2  114       Carl
# 3  115        Dan
print(df)