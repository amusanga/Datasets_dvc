import os
import uuid
import numpy as np 
import pandas as pd 
from tqdm import tqdm

DATA_PATH ="/home/aime/TrustStamp/Datasets_dvc/ttiff_images_dataset/data/tiff_images"
OUT_DIR = 'ttiff_images_dataset/data'

def list_files_with_extensions(datadir, file_extensions):

    if file_extensions is None:
        file_extensions = [".jpeg", ".jpg", ".png"]
    # Scan png files that are not mask
    filelist = []
    for root, dirs, files in os.walk(datadir):

        for file in files:
            test_ = [file.lower().endswith(x) for x in file_extensions]
            if any(test_):
                filelist.append(os.path.join(root, file))
    return filelist

if __name__ == "__main__":
        # Prepare the output csv filename

    data_paths = list_files_with_extensions(DATA_PATH, file_extensions=[".tif", ".dcm"] )

    if not os.path.exists(OUT_DIR):
        os.makedirs(OUT_DIR)

    CSV_OUT = os.path.join(OUT_DIR,'metadata.csv')
    
    # Initialize the dataframe
    df = pd.read_csv(CSV_OUT) if os.path.exists(CSV_OUT) else pd.DataFrame()

    with tqdm(total=len(data_paths)) as pbar:
        for data_path in data_paths:
            # Check if this file was already processed or not
            if "data_path" in df and (df["data_path"].eq(str(data_path))).any():
                pbar.update(1)
                continue
            
            data_frame_index = str(uuid.uuid4())
                # Add the name and subject id
            df.loc[str(data_frame_index), "data_path"] = str(data_path)
            df.to_csv(CSV_OUT, index=False)
            pbar.update(1)
