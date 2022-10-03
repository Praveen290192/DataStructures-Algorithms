
import os
def helper_func(suffix, path, output):
    # Getting the list of folders/directories
    listFolder = os.listdir(path)
    # Looping over each folders/directories
    for f in listFolder:
        # Creating path for current directory
        FilePath = os.path.join(path,f)
        # Checking if its a Directory
        if os.path.isdir(FilePath):
            # navigating to that directory 
            helper_func(suffix,FilePath,output)
        # Checking for suffix
        elif f.endswith(suffix):
            # Appending the path
            output.append(FilePath)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = []
    try:
        os.listdir(path)
    except:
        return "Invalid path", path
    helper_func(suffix, path, output)
    return output

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(find_files(".c",".")) #['.\\testdir\\subdir1\\a.c', '.\\testdir\\subdir3\\subsubdir1\\b.c', '.\\testdir\\subdir5\\a.c', '.\\testdir\\t1.c']
# Test Case 2
print(find_files(".h",".")) #['.\\testdir\\subdir1\\a.h', '.\\testdir\\subdir3\\subsubdir1\\b.h', '.\\testdir\\subdir5\\a.h', '.\\testdir\\t1.h']
# Test Case 3
print(find_files(".h",".rs")) #('Invalid path', '.rs')




