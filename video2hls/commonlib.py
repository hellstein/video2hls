import sys

def get_meta_from_filename(fname):
    from os import path
    meta = {}
    if path.exists(fname) and path.isfile(fname):
        meta["file"] = fname
        meta["dir"] = path.dirname(fname)
        meta["name"], meta["ext"] = path.splitext(path.basename(fname))
    return meta

def encoding_meta_to_filename(meta):
    import hashlib
    m = hashlib.sha256()
    m.update(meta["name"].encode())
    # m.update(key)
    return m.hexdigest()



if __name__ == "__main__":
    fname = sys.argv[1] 
    meta = get_meta_from_filename(fname)
    print(meta)
