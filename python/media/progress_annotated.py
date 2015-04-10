#!/bin/env python3
'''A module to produce a pie chart showing the progress of data processing based
on the number of files in a directory.
'''

import os

def setup_example(all_run_numbers=None):
    '''Creates a tempdir and populates it with empty files
    simulating raw data files and processed data files.

    Takes an optional list of integers to use as example
    data file (run) numbers.
    '''
    if all_run_numbers is None:
        all_run_numbers = [i for i in range(2113, 2452)]

    import tempfile
    data_dir = tempfile.mkdtemp()
    print('Writing data to', data_dir)

    # Touch some random files to simulate processed data.
    from random import randrange, randint
    max_faked_runs = randrange(0, len(all_run_numbers))
    faked_runs = sorted(
        {randint(all_run_numbers[0], all_run_numbers[-1])
         for _ in range(max_faked_runs)})

    print('Faking data files for all runs.')
    print('   Faking runs', faked_runs)

    for run in all_run_numbers:
        if run in faked_runs:
            files_to_make = ('Raw', 'Run')
        else:
            files_to_make = ('Raw',)
        for basename in files_to_make:
            file_path = os.path.join(
                data_dir, '{}{}.data'.format(basename, run))
            with open(file_path, 'w+'):
                pass

    # Return the path to the faked data.
    return data_dir

def cleanup_example(directory):
    '''Clean up after running a example progress check.

    WARNING: This function deletes all files in directory and then
    removes the directory.
    '''
    filenames = os.listdir(directory)
    for file in filenames:
        os.remove(os.path.join(directory, file))
    os.rmdir(directory)

# Just for fun, we'll extract the run number from the filename just to show we
# can with a specially crafted function.
def extract_run_number(fname, prefix='Run', suffix='.data'):
    '''Return an int NNNN from a file name in the form 'prefixNNNNsuffix'.
    '''
    return int(fname.strip(prefix).strip(suffix))

# Here's the real code. This does the heavy lifting. If this weren't an example,
# this is the only function that would be defined.
def check_progress(data_dir, unprocessed_tag='Raw', processed_tag='Run'):
    '''Generates a pie chart showing the progress of processing data in a
    directory.

    check_progress finds all files in data_dir and computes the ratio of the
    number of files with 'Run' in their filename to those without.
    '''
    # Get the directory contents.
    filenames = os.listdir(data_dir)

    number_of_data_files = len([i for i in filenames if unprocessed_tag in i])
    if number_of_data_files == 0:
        print('No data files found in {}'.format(data_dir))
        return

    # Just for fun, we can extract specific run numbers from the files
    # found in the dir, even though we don't need this info to make
    # the progress pie chart.
    processed_runs = tuple(
        extract_run_number(i) for i in filenames if processed_tag in i)
    print('Processed runs', sorted(processed_runs))

    # Compute the progress percentages.
    percent_completed = len(processed_runs) / number_of_data_files
    percent_remaining = 1 - percent_completed

    # Make a pie chart.
    import matplotlib
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({'font.size': 16})
    plt.figure(1, figsize=(6, 6))
    plt.axis('equal')
    plot_properties = {
        'labels':['Remaining', 'Completed'],
        'autopct':'%.1f%%',
        'startangle':90,
        'colors':('lightcoral', 'yellowgreen'),
    }
    plt.pie((percent_remaining, percent_completed), **plot_properties)
    plt.title("Processed Data")
    plt.draw()
    plt.show()

def _run_example():
    '''Run the progress check as an example on fake data in a safe temporary
    directory.
    '''
    print('Running an example with fake data.')
    data_dir = setup_example()
    check_progress(data_dir)
    cleanup_example(data_dir)

def _in_ipython():
    '''Return a boolean indicating if the interpereter is running in an iPython
    instance.
    '''
    try:
        if __IPYTHON__:
            in_ipython = True
    except NameError:
        in_ipython = False
    return in_ipython


# Run check_progress if called from the command line. When a python source file
# is executed by itself (as opposed to being imported to another source file),
# the interpereter gives the file an internal name __name__ = '__main__'.

# Using this fact, we can have the following block run as a script when this
# file is executed by itself by either
#    `$./progress.py`
# or
#    `$python progress.py`
# The first form assumes the file has executable permissions. The second will
# work for any python source file regardless if the file has executable
# permissions.
#
# Furthermore, if we wish to reuse the functions defined in this file in another
# source file, we can import them without having the code below run.
if __name__ == '__main__':
    # We don't want to run this code if we are in an iPython instance.
    if not _in_ipython():
        # We can catch command line arguments using the 'argparse' package.
        # This package also adds help output to the function when called
        # from the command line. Try it with '$./progress.py -h'.
        from argparse import ArgumentParser
        PARSER = ArgumentParser(
            description='''Check data processing progress.''')
        PARSER.add_argument(
            'directory', metavar='DIR', type=str, nargs='?',
            help='directory to check progress in.')
        PARSER.add_argument(
            '-p', '--processed-tag', metavar='PTAG', type=str, default='Run',
            help='Files containing substring PTAG\
                are assumed to be processed.')
        PARSER.add_argument(
            '-u', '--unprocessed-tag', metavar='UTAG', type=str, default='Raw',
            help='Files containing substring UTAG\
                are assumed to be unprocessed.')
        ARGS = PARSER.parse_args()
        if ARGS.directory is None:
            _run_example()
        else:
            check_progress(
                ARGS.directory,
                ARGS.unprocessed_tag,
                ARGS.processed_tag)
