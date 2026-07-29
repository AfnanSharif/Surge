
import pandas as pd
import numpy as np
import yaml
import os

def generate_data(num_samples: int, output_path: str):
    np.random.seed(42)
    f1 = np.random.normal(100, 20, num_samples)
    f2 = np.random.uniform(10, 50, num_samples)
    target = (f1 * 2.5) + (f2 * 1.5) + np.random.normal(0, 10, num_samples)
    df = pd.DataFrame({'f1': f1, 'f2': f2, 'target': target})
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Generated data at {output_path}")

if __name__ == "__main__":
    with open("configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    generate_data(config['data']['num_samples'], config['data']['raw_path'])
