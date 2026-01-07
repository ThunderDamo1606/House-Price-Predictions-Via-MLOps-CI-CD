import os
import sys, os
sys.path.append(os.path.abspath("src"))

from train import train_model



def test_model_creation():
    train_model()
    assert os.path.exists("models/model.pkl")
