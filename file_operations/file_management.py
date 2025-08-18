import os

def file_exists(filename):
    return os.path.exists(filename)

print(f" 'sample.txt' exists: {file_exists('sample.txt')}")
print(f" 'nonexistent.txt' exists: {file_exists('nonexistent.txt')}")