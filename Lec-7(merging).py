import pandas as pd

frame1 = pd.DataFrame({'key': range(5), 'frame1': ['a', 'b', 'c', 'd', 'e']})
frame2 = pd.DataFrame({'key': range(2, 7), 'frame2': ['t', 'u', 'v', 'w', 'x']})
frame1
frame2

pd.merge(frame1, frame2)
pd.merge(frame1, frame2, on='key')  # note that on='key' is not effected but was in the tut
pd.merge(frame1, frame2, on='key', how='right')  # frame2 is superior
pd.merge(frame1, frame2, on='key', how='left')  # frame1 is superior
pd.merge(frame1, frame2, on='key', how='outer')  # u get everythin
pd.merge(frame1, frame2, on='key', how='inner')  # the default
pd.concat([frame1, frame2])  # act as a repetetion one above the other
pd.concat([frame1, frame2], axis=1)  # act as a repetetion one beside the other
