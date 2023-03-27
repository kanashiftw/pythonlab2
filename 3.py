from pathlib import Path

def fix_names(folder, textfile):
    path = Path(folder)
    mask = '*.mp3'
    names = Path(textfile)
    tracks = {}
    with names.open() as f:
        for line in f:
            s = line.split('[')[0]
            tracks[s.split('.')[1].strip()] = s.strip()
    print(tracks)
    for f in path.glob(mask):
        name = f.name.replace(f.suffix, '')
        try:
            f.rename(str(f).replace(name, tracks.get(name)))
        except TypeError:
            continue


fix_names("music", "names.txt")
