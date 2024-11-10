import pickle
import os

def write_pkl(write_data, pkl_path):  # 写入pkl
    pickle.dump(write_data, open(pkl_path, 'wb'))


def read_pkl(pkl_file):  # 读取pkl
    my_data = pickle.load(open(pkl_file, 'rb'))
    return my_data


# 读取pkl文件
# pkl_path = 'example_material/example_object_path.pkl'
# read_pkl_content = read_pkl(pkl_path)
# print(read_pkl_content)


#! 测试个别文件
# pkl_path = 'behaviour_1k/usd_object_path.pkl'
# behaviour_objects_path = '/home/wdx/research/omnigibson_data/data/og_dataset/objects/'
# model_path = [
#     os.path.join(behaviour_objects_path, 'armchair/axcwcm/usd/axcwcm.usd'),
#     os.path.join(behaviour_objects_path, 'car/gewjwh/usd/gewjwh.usd'),
#     os.path.join(behaviour_objects_path, 'gift_box/mfalrc/usd/mfalrc.usd'),
# ]
# write_pkl(model_path, pkl_path)


#! 写入完整Behaviour数据集的物体模型路径
pkl_path = 'behaviour_1k/usd_object_path.pkl'
behaviour_objects_path = '/home/wdx/research/omnigibson_data/data/og_dataset/objects/'

model_path = []
categorys = os.listdir(behaviour_objects_path)
for cate in categorys:
    cate_path = os.path.join(behaviour_objects_path, cate)
    uids = os.listdir(cate_path)
    for uid in uids:
        usd_path = os.path.join(cate_path, uid, 'usd', f'{uid}.usd')
        if os.path.exists(usd_path):
            model_path.append(usd_path)
        else:
            print('not exist:', usd_path)

print('='*100)
print('load model count:', len(model_path))
print('first 5:', model_path[:5])
print('='*100)

write_pkl(model_path, pkl_path)




"""
渲染命令：
./blender-3.4.1-linux-x64/blender -b -P render_script.py -- --object_path_pkl './behaviour_1k/usd_object_path.pkl' --parent_dir './behaviour_1k'
"""