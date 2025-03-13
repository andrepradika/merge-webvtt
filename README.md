# VTT Merging Script

This Python script merges `.vtt` subtitle files from two folders (`watch` and `shorts`) and combines them into merged `.vtt` files. It outputs three merged subtitle files:
- One for captions from the `watch` folder.
- One for captions from the `shorts` folder.
- One combining all captions from both folders.

## Requirements

- Python 3.x
- `webvtt-py` library for reading `.vtt` files. You can install it using pip:

```bash
pip install webvtt-py
```

## File Structure

Ensure the following folder structure:

```
your_project_folder/
├── watch/                # Folder containing VTT files for "watch"
├── shorts/               # Folder containing VTT files for "shorts"
├── merge/                # Folder where merged VTT files will be saved
├── merge_vtt.py          # Python script (this script)
```

- **`watch/`**: Place `.vtt` files related to "watch" content here.
- **`shorts/`**: Place `.vtt` files related to "shorts" content here.
- **`merge/`**: The merged `.vtt` files will be saved in this folder.

## Usage

1. Place your `.vtt` subtitle files into the `watch/` and `shorts/` folders.
2. Run the script:

```bash
python merge_vtt.py
```

3. The script will generate the following merged files in the `merge/` folder:
    - `watch_merge.vtt`: Merged captions from the `watch` folder.
    - `shorts_merge.vtt`: Merged captions from the `shorts` folder.
    - `all_merge.vtt`: Merged captions from both the `watch` and `shorts` folders.

## How It Works

- The script reads all `.vtt` files in the `watch/` and `shorts/` folders.
- It merges the captions from these files and stores the result in a new file.
- Three merged `.vtt` files are generated:
  - **`watch_merge.vtt`**: Contains merged captions from the `watch` folder.
  - **`shorts_merge.vtt`**: Contains merged captions from the `shorts` folder.
  - **`all_merge.vtt`**: Contains merged captions from both `watch` and `shorts` folders.

## Folder and File Paths

The following paths are used in the script:
- **`watch_folder`**: Path to the folder containing the `watch` `.vtt` files (`../watch`).
- **`shorts_folder`**: Path to the folder containing the `shorts` `.vtt` files (`../shorts`).
- **`merge_results_folder`**: Path to the folder where the merged `.vtt` files will be saved (`merge/`).

## Example

### Folder Structure:

```
your_project/
├── watch/
│   ├── video1.vtt
│   ├── video2.vtt
├── shorts/
│   ├── short1.vtt
│   ├── short2.vtt
├── merge/
│   ├── watch_merge.vtt
│   ├── shorts_merge.vtt
│   ├── all_merge.vtt
```

### Output Example:

After running the script, the `merge/` folder will contain:

```
merge/
├── watch_merge.vtt
├── shorts_merge.vtt
├── all_merge.vtt
```

## License

MIT License (or your preferred license)

## Author
andrepradika

sh```
yt-dlp --write-auto-subs --skip-download --sleep-requests 1.25 --min-sleep-interval 60 --max-sleep-interval 90 -o "%(uploader)s/%(title)s.%(ext)s" "https://www.youtube.com/@MyFirstMillionPod"
```
