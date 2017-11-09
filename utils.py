import os



def get_files_by_file_size(dirname, reverse=True):
    """ Return list of file paths in directory sorted by file size """

    # Get list of files
    onlyfiles = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]

    # Re-populate list with filename, size tuples
    for i in xrange(len(onlyfiles)):
        onlyfiles[i] = (os.path.join(dirname,onlyfiles[i]), os.path.getsize(os.path.join(dirname,onlyfiles[i])))
    # Sort list by file size
    # If reverse=True sort from largest to smallest
    # If reverse=False sort from smallest to largest
    onlyfiles.sort(key=lambda filename: filename[1], reverse=reverse)

    # Re-populate list with just filenames
    for i in xrange(len(onlyfiles)):
        onlyfiles[i] = onlyfiles[i][0]

    return onlyfiles
    
    
if __name__ == "__main__":
    print 'This is not a standalone script'