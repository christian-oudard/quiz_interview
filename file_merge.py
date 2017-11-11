"""
You have a list of log files from several web servers, and you would like to
merge them into a single log file. Each log file line starts with a timestamp.

These files might be very large, so you can't read them all into memory
at once.

The unittests use StringIO fake files, but your code should operate equally
well on real files.

>>> from StringIO import StringIO
>>> file1 = StringIO('''\\
... 1366201359 stuff happened
... 1366201450 more stuff happened
... 1366202101 different stuff
... ''')
>>> file2 = StringIO('''\\
... 1366200237 blah
... 1366201763 blah blah
... ''')
>>> file3 = StringIO('''\\
... 1366193610 red
... 1366200562 green
... 1366202304 blue
... 1366202312 orange
... 1366203094 yellow
... ''')

>>> outfile = StringIO()
>>> merge_files([file1, file2, file3], outfile)
>>> outfile.seek(0)
>>> print outfile.read(),
1366193610 red
1366200237 blah
1366200562 green
1366201359 stuff happened
1366201450 more stuff happened
1366201763 blah blah
1366202101 different stuff
1366202304 blue
1366202312 orange
1366203094 yellow
"""


def get_timestamp(line):
    try:
        timestamp_string = line.split()[0]
    except IndexError:
        return None
    try:
        return int(timestamp_string)
    except ValueError:
        return None


def index_min_timestamp(lines):
    # Return the index of the line with the minimum timestamp.
    min_ts = None
    min_index = None
    for i, line in enumerate(lines):
        ts = get_timestamp(line)
        if ts is None:
            continue
        if min_ts is None or ts < min_ts:
            min_ts = ts
            min_index = i
    return min_index


def merge_files(infiles, outfile):
    first_lines = [f.readline() for f in infiles]
    while True:
        i = index_min_timestamp(first_lines)
        if i is None:
            break
        outfile.write(first_lines[i])
        first_lines[i] = infiles[i].readline()
