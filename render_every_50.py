import os
import pickle
import time

object_path_pkl = './behaviour_1k/usd_object_path.pkl'
uid_paths = pickle.load(open(object_path_pkl, 'rb'))

every_num = 50
for i in range(len(uid_paths)):
    if i % every_num == 0:
        start_id = i
        end_id = start_id + every_num
        os.system(f"./blender-3.4.1-linux-x64/blender -b -P render_script.py -- --object_path_pkl {object_path_pkl} --start_id {start_id} --end_id {end_id} --parent_dir './behaviour_1k'")
        print('done:', start_id, '--', end_id)
        time.sleep(3)