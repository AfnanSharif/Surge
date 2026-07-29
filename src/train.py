
import pandas as pd
import yaml
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

def train_model():
    with open("configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    df = pd.read_csv(config['data']['raw_path'])
    X, y = df.drop('target', axis=1), df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=config['model']['test_size'], random_state=42)
    pipeline = Pipeline([('scaler', StandardScaler()), ('reg', RandomForestRegressor(n_estimators=50, random_state=42))])
    pipeline.fit(X_train, y_train)
    print(f"R2: {r2_score(y_test, pipeline.predict(X_test)):.4f}")
    os.makedirs(os.path.dirname(config['data']['model_path']), exist_ok=True)
    joblib.dump(pipeline, config['data']['model_path'])

if __name__ == "__main__":
    train_model()
