import webvtt
import os

# Paths for your folders
watch_folder = '../watch'
shorts_folder = '../shorts'

# Paths for merged result files
merge_results_folder = 'merge'
watch_merge_path = os.path.join(merge_results_folder, 'watch_merge.vtt')
shorts_merge_path = os.path.join(merge_results_folder, 'shorts_merge.vtt')
all_merge_path = os.path.join(merge_results_folder, 'all_merge.vtt')

# Function to merge .vtt files in a folder
def merge_vtt_files(folder):
    merged_captions = []
    
    # Iterate over all .vtt files in the folder
    for filename in os.listdir(folder):
        if filename.endswith('.vtt'):
            file_path = os.path.join(folder, filename)
            # Read the .vtt file
            for caption in webvtt.read(file_path):
                merged_captions.append(caption)
    
    return merged_captions

# Merge captions for "watch" folder
watch_captions = merge_vtt_files(watch_folder)
# Merge captions for "shorts" folder
shorts_captions = merge_vtt_files(shorts_folder)

# Make sure the output directory exists
if not os.path.exists(merge_results_folder):
    os.makedirs(merge_results_folder)

# Write the merged captions into their respective files
def write_merged_captions(captions, output_path):
    with open(output_path, 'w') as f:
        for caption in captions:
            f.write(str(caption) + '\n')

# Write the merged files for watch and shorts
write_merged_captions(watch_captions, watch_merge_path)
write_merged_captions(shorts_captions, shorts_merge_path)

# Merge all captions from both folders and write to 'all_merge.vtt'
all_captions = watch_captions + shorts_captions
write_merged_captions(all_captions, all_merge_path)

print("Merging completed. Merged files are saved in 'merge/' folder.")
