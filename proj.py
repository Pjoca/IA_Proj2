import pandas

data = pandas.read_csv("dataset.csv")
print(data.head())


age = {
    -0.95197: '18-24',
    -0.07854: '25-34',
    0.49788: '35-44',
    1.09449: '45-54',
    1.82213: '55-64',
    2.59171: '65+'
}

gender = {
            0.48246: 'Female',
            -0.48246: 'Male'
}

country = {
            -0.09765: 'Australia',
            0.24923: 'Canada',
            -0.46841: 'New Zealand',
            -0.28519: 'Other',
            0.21128: 'Republic of Ireland',
            0.96082: 'UK',
            -0.57009: 'USA'
}

ethnicity = {
            -0.50212: 'Asian',
            -1.10702: 'Black',
            1.90725: 'Mixed-Black/Asian',
            0.12600: 'Mixed-White/Asian',
            -0.22166: 'Mixed-White/Black',
            0.11440: 'Other',
            -0.31685: 'White'
}

education = {
            -2.43591: 'Left School Before 16 years',
            -1.73790: 'Left School at 16 years',
            -1.43719: 'Left School at 17 years',
            -1.22751: 'Left School at 18 years',
            -0.61113: 'Some College,No Certificate Or Degree',
            -0.05921: 'Professional Certificate/ Diploma',
            0.45468: 'University Degree',
            1.16365: 'Masters Degree',
            1.98437: 'Doctorate Degree',
}


            
data['Age'] = data['Age'].replace(age)
data['Gender'] = data['Gender'].replace(gender)
data['Country'] = data['Country'].replace(country)
data['Ethnicity'] = data['Ethnicity'].replace(ethnicity)
data['Education'] = data['Education'].replace(education)

updated_dataset = "updated_dataset.csv"
data.to_csv(updated_dataset, index=False)
          
print(data.head())

