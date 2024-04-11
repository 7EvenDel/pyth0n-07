import pandas as pd

df = pd.read_csv("GoogleApps.csv", index_col="App")

first_app = df.index[0]


last_app = df.index[-1]
last_category = df.loc[last_app, "Category"]


number_of_columns = df.shape[1]


average_size = df["Size"].mean()
median_size = df["Size"].median()


app_with_max_reviews = df["Reviews"].idxmax()
category_with_max_reviews = df.loc[app_with_max_reviews, "Category"]


expensive_apps = df[df["Price"] > 20]
popular_apps = expensive_apps.query("Installs > 10000")
average_rating = popular_apps["Rating"].mean()


print("First app:", first_app)
print("Category of the last app:", last_category)
print("Number of columns:", number_of_columns)
print("Average size:", average_size)
print("Median size:", median_size)
print("Category with the most reviews:", category_with_max_reviews)
print("Average rating of popular paid apps:", average_rating)
