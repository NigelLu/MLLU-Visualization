import os
import sys
import pandas as pd
import numpy as np

DATASET_LIST = ['mnli', 'race', 'squad', 'yelp']
METHOD_LIST = ['adapter', 'bitfit', 'lora', 'none']
DATA_RATIO_LIST = ['0.001', '0.010', '0.100', '1.000']
COL_NAMES = ["Dataset", "Data-ratio",
             "Tuning Method", "Steps", "Average Metrics"]


def dump_log(dump_dir="./results/convergence/csv", log_dir='./results/convergence/raw'):
    result_dict = {col: [] for col in COL_NAMES}

    for dataset in DATASET_LIST:
        for method in METHOD_LIST:
            for data_ratio in DATA_RATIO_LIST:
                with open(os.path.join(log_dir, f'{dataset}_{method}_{data_ratio}.log'), 'r') as f:
                    # read and parse data
                    data = [eval(l) for l in f.read().split('\n')]

                performance = [datapoint['eval_average_metrics']
                               for datapoint in data]
                peak_idx = np.argmax(performance)
                for idx in range(peak_idx+1):

                    result_dict[COL_NAMES[0]].append(dataset)
                    result_dict[COL_NAMES[1]].append(data_ratio)
                    result_dict[COL_NAMES[2]].append(
                        method.capitalize() if method != "none" else "Fine-tuning")
                    result_dict[COL_NAMES[3]].append((idx+1)*2000)
                    result_dict[COL_NAMES[4]].append(
                        data[idx]["eval_average_metrics"])

    result_df = pd.DataFrame(result_dict)
    result_df.to_csv(os.path.join(dump_dir, "convergence.csv"), index=False)


if __name__ == "__main__":
    assert len(sys.argv) == 3 or len(
        sys.argv) == 1, 'Usage: python3 log_dump.py [log_dir] [output_dir]'

    if (len(sys.argv) == 3):
        assert os.path.isdir(sys.argv[1]) and os.path.isdir(
            sys.argv[2]), 'Invalid path(s)'

    log_dir, output_dir = "./results/convergence/raw" if len(
        sys.argv) != 3 else sys.argv[1], './results/convergence/csv' if len(sys.argv) != 3 else sys.argv[2]
    print('[Log Dir]:', os.path.abspath(log_dir))
    print('[Output Dir]:', os.path.abspath(output_dir))
    dump_log(log_dir=log_dir, dump_dir=output_dir)
