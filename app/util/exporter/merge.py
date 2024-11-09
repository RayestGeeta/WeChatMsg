

import json
import os


data_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")), 'data', 'msg', 'raw')
out_dir = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")), 'data', 'msg', 'merge')
os.makedirs(out_dir, exist_ok=True)

dev_res = []
train_res = []

no_room_train_res = []
no_room_dev_res = []

for filepath, dirnames, filenames in os.walk(data_dir):
    for filename in filenames:
        if filename.endswith('.json'):
            print(filename, filepath)
            filepath_ = os.path.join(filepath, filename)
            with open(filepath_, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if data:
                if filename.endswith('train.json'):
                    train_res += data
                    if not filename.startswith('is_chatroom'):
                        no_room_train_res += data
                else:
                    dev_res += data
                    if not filename.startswith('is_chatroom'):
                        no_room_dev_res += data

with open(os.path.join(out_dir, f"train.json"), 'w', encoding='utf-8') as f:
    json.dump(train_res, f, ensure_ascii=False, indent=4)

with open(os.path.join(out_dir, f"dev.json"), 'w', encoding='utf-8') as f:
    json.dump(dev_res, f, ensure_ascii=False, indent=4)


with open(os.path.join(out_dir, f"no_room_train.json"), 'w', encoding='utf-8') as f:
    json.dump(no_room_train_res, f, ensure_ascii=False, indent=4)

with open(os.path.join(out_dir, f"no_room_dev.json"), 'w', encoding='utf-8') as f:
    json.dump(no_room_dev_res, f, ensure_ascii=False, indent=4)

