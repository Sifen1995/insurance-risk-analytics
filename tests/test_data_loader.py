import pytest
import pandas as pd
import os
from src.data_loader import load_insurance_data

def test_load_insurance_data_file_not_found():
    """
    Ensures that the loader gracefully raises a FileNotFoundError
    if given a dummy path that doesn't exist.
    """
    with pytest.raises(FileNotFoundError):
        load_insurance_data("data/non_existent_file.csv")