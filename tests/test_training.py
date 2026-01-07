import os
import sys

sys.path.append(os.path.abspath("src"))
from train import train_model


def test_training_runs():
    result = train_model()
    assert result is None
