# # Create vectors (data)
# name <- c('Dinesh', 'Suresh', 'Rahul', 'Ravi', 'Manoj', 
#           'Hari', 'Yatharth', 'Saurabh', 'Kapil', 'Salini')

# score <- c(12.5, 9, 16.5, NA, 9, 20, 14.5, NA, 8, 19)

# attempts <- c(1, 3, 2, 3, 2, 3, 1, 1, 2, 1)

# qualify <- c('yes', 'no', 'yes', 'no', 'no', 
#              'yes', 'yes', 'no', 'no', 'yes')

# labels <- c('a', 'b', 'c', 'd', 'e', 'f', 
#             'g', 'h', 'i', 'j')

# # Create DataFrame
# exam_data <- data.frame(name, score, attempts, qualify, row.names = labels)

# # Display DataFrame
# print(exam_data)


#--------------------------------------------------------------------------------------

import pandas as pd
import numpy as np

# Create dictionary data
exam_data = {
    'name': ['Dinesh', 'Suresh', 'Rahul', 'Ravi', 'Manoj',
             'Hari', 'Yatharth', 'Saurabh', 'Kapil', 'Salini'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no',
                'yes', 'yes', 'no', 'no', 'yes']
}

# Index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create DataFrame
df = pd.DataFrame(exam_data, index=labels)

# Display DataFrame
print(df)