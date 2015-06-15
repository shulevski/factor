import os
from lofarpipe.support.data_map import DataMap
from lofarpipe.support.data_map import DataProduct


def plugin_main(args, **kwargs):
    """
    Trims a string from filenames in a mapfile

    Note that everything from the matching string to the end is trimmed.

    Parameters
    ----------
    mapfile_in : str
        Filename of datamap to trim
    trim_str : str
        String to remove
    mapfile_dir : str
        Directory for output mapfile
    filename: str
        Name of output mapfile

    Returns
    -------
    result : dict
        New datamap filename

    """
    mapfile_in = kwargs['mapfile_in']
    trim_str = kwargs['trim']
    mapfile_dir = kwargs['mapfile_dir']
    filename = kwargs['filename']

    map_out = DataMap([])
    map_in = DataMap.load(mapfile_in)

    for i, item in enumerate(map_in):
        map_out.data.append(DataProduct(item.host, item.file[:item.file.index(trim_str)],
            item.skip))

    fileid = os.path.join(mapfile_dir, filename)
    map_out.save(fileid)
    result = {'mapfile': fileid}

    return result
