# Panda makes use of Numpy and Mattplotlib
import panda as pd

file = 'file.extension'
# This is where the data is extracted 
df = pd_read_csv(file, arguments)
## Arguments
arguments = [sep=',', header='infer', index_col=None, usecols=None,
            squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None,
            converters=None, true_values=None, false_values=None, skipinitialspace=False,
            skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True,
            na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False,
            infer_datetime_format=False, keep_date_col=False, date_parser=None,
            dayfirst=False, cache_dates=True, iterator=False, chunksize=None,
            compression='infer', thousands=None, decimal='.', lineterminator=None,
            quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None,
            encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True,
            delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None]
## Retrieves rows and collumns description
df.shape
## Self explanatory
df.head(Number)
df.tail(Number)
df.info()
# Create data frame
pd.DataFrame(YourData)
## Summary of the data
df.describe()
## Retrieve ammount of not None values
df.count()
# Create and overwrite to file
df.to_csv('file.extension', arguments)
## Arguments
arguments = [sep=',', na_rep='', float_format=None, columns=None, 
             header=True, index=True, index_label=None, mode='w', encoding=None, 
             compression='infer', quoting=None, quotechar='"', line_terminator=None, 
             chunksize=None, date_format=None, doublequote=True, escapechar=None, 
             decimal='.', errors='strict']