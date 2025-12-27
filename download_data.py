import kagglehub
import shutil

# Download to default location
path = kagglehub.dataset_download("mrbaloglu/rotten-tomatoes-reviews-dataset")
print("Downloaded to:", path)

# Move it here
target_dir = "./data/"
shutil.move(path, target_dir)
print("Moved to:", target_dir)

