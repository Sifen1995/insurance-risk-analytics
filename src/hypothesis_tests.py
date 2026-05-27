import pandas as pd
import numpy as np
from scipy import stats

def run_chi2_test(df, feature_col, target_col='HasClaim'):
    """
    Runs a Chi-Squared test of independence for a categorical feature against claim frequency.
    """
    # Create the contingency table
    contingency_table = pd.crosstab(df[feature_col], df[target_col])
    
    # Calculate chi2 stats
    chi2, p_val, dof, expected = stats.chi2_contingency(contingency_table)
    return chi2, p_val

def run_ttest(group_a_series, group_b_series):
    """
    Runs a two-sample independent t-test for numerical variables.
    Handles unequal variances gracefully via Welch's t-test.
    """
    t_stat, p_val = stats.ttest_ind(group_a_series, group_b_series, equal_var=False, nan_policy='omit')
    return t_stat, p_val