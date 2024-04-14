import pandas as pd
import numpy as np
from scipy.stats import sem
from statsmodels.formula.api  import ols

# https://www.openicpsr.org/openicpsr/project/113599/version/V1/view?path=/openicpsr/113599/fcr:versions/V1/2013-0533_data--TO-SUBMIT-&type=folder

dtafile = 'C:/Users/dennis/OneDrive/Desktop/2013-0533_data_endlines1and2.dta'
df = pd.read_stata(dtafile)
df

# Select (Subset) Variables of Interest
subset_df = df[['treatment', 'anymfi_amt_1', 'bizprofit_1', 'bizemployees_1', 'adults_1', 'children_1']]
subset_df

# Remove Missing Values (Rows)
new_df = subset_df.dropna()
new_df

# Check for missing values
new_df.isnull().sum()

# Entire Sample Size (Total Number of Samples)
n = len(new_df)
n

# Treatment Size (Total Number of Treated Sample)
list(new_df.treatment).count('Treatment')

# Control Size (Total Number of Control Sample)
list(new_df.treatment).count('Control')

# Let Treatment = 1 (Replace string with integer)
new_df=new_df.replace(to_replace="Treatment",value=1)

# Let Control = 0 (Replace string with integer)
new_df=new_df.replace(to_replace="Control",value=0)

# Convert all DataFrame columns to the int64 dtype
new_df = new_df.astype(int)

# Summary Statistics

# Mean Calculations of Variables for Entire Group
new_df.describe()

# Mean Calculations of Variables for Treatment Group

# Mean of anymfi_amt_1 (AnyMFIAmount) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'anymfi_amt_1'].mean()

# Mean of treatment (Treatment) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'treatment'].mean()

# Mean of bizprofit_1 (BusinessProfits) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'bizprofit_1'].mean()

# Mean of bizemployees_1 (BusinessEmployees) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'bizemployees_1'].mean()

# Mean of adults_1 (Adults) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'adults_1'].mean()

# Mean of children_1 (Children) for Treatment Group
new_df.loc[(new_df['treatment']==1), 'children_1'].mean()

# Mean Calculations of Variables for Control Group

# Mean of anymfi_amt_1 (AnyMFIAmount) for Control Group
new_df.loc[(new_df['treatment']==0), 'anymfi_amt_1'].mean()

# Mean of treatment (Treatment) for Control Group
new_df.loc[(new_df['treatment']==0), 'treatment'].mean()

# Mean of bizprofit_1 (BusinessProfits) for Control Group
new_df.loc[(new_df['treatment']==0), 'bizprofit_1'].mean()

# Mean of bizemployees_1 (BusinessEmployees) for Control Group
new_df.loc[(new_df['treatment']==0), 'bizemployees_1'].mean()

# Mean of adults_1 (Adults) for Control Group
new_df.loc[(new_df['treatment']==0), 'adults_1'].mean()

# Mean of children_1 (Children) for Control Group
new_df.loc[(new_df['treatment']==0), 'children_1'].mean()

# Standard Error Calculations of Variables for Entire Group

# Standard Error of anymfi_amt_1 (AnyMFIAmount) for Entire Group
sem(new_df["anymfi_amt_1"])

# Standard Error of treatment (Treatment) for Entire Group
sem(new_df["treatment"])

# Standard Error of bizprofit_1 (BusinessProfits) for Entire Group
sem(new_df["bizprofit_1"])

# Standard Error of bizemployees_1 (BusinessEmployees) for Entire Group
sem(new_df["bizemployees_1"])

# Standard Error of adults_1 (Adults) for Entire Group
sem(new_df["adults_1"])

# Standard Error of children_1 (Children) for Entire Group
sem(new_df["children_1"])

# Standard Error Calculations of Variables for Treatment Group

# Standard Error of anymfi_amt_1 (AnyMFIAmount) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'anymfi_amt_1'])

# Standard Error of treatment (Treatment) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'treatment'])

# Standard Error of bizprofit_1 (BusinessProfits) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'bizprofit_1'])

# Standard Error of bizemployees_1 (BusinessEmployees) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'bizemployees_1'])

# Standard Error of adults_1 (Adults) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'adults_1'])

# Standard Error of children_1 (Children) for Treatment Group
sem(new_df.loc[(new_df['treatment']==1), 'children_1'])

# Standard Error Calculations of Variables for Control Group

# Standard Error of anymfi_amt_1 (AnyMFIAmount) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'anymfi_amt_1'])

# Standard Error of treatment (Treatment) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'treatment'])

# Standard Error of bizprofit_1 (BusinessProfits) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'bizprofit_1'])

# Standard Error of bizemployees_1 (BusinessEmployees) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'bizemployees_1'])

# Standard Error of adults_1 (Adults) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'adults_1'])

# Standard Error of children_1 (Children) for Control Group
sem(new_df.loc[(new_df['treatment']==0), 'children_1'])

# Basic Model
Basic_LRM = new_df[['treatment', 'anymfi_amt_1']]
Basic_LRM

# Change to DataFrame Variables
treatment=pd.DataFrame(Basic_LRM['treatment'])
anymfi_amt_1=pd.DataFrame(Basic_LRM['anymfi_amt_1'])

# Basic_LRM (OLS Regression Results)
est = ols(formula = 'anymfi_amt_1 ~  treatment', data = Basic_LRM).fit()
est.summary()

# Full Model
Full_LRM = new_df[['treatment', 'anymfi_amt_1', 'bizprofit_1', 'bizemployees_1', 'adults_1', 'children_1']]
Full_LRM

# Change to DataFrame Variables
treatment=pd.DataFrame(Full_LRM['treatment'])
anymfi_amt_1=pd.DataFrame(Full_LRM['anymfi_amt_1'])
bizprofit_1=pd.DataFrame(Full_LRM['bizprofit_1'])
bizemployees_1=pd.DataFrame(Full_LRM['bizemployees_1'])
adults_1=pd.DataFrame(Full_LRM['adults_1'])
children_1=pd.DataFrame(Full_LRM['children_1'])

# Full_LRM (OLS Regression Results)
est = ols(formula = 'anymfi_amt_1 ~  treatment + bizprofit_1 + bizemployees_1 + adults_1 + children_1', data = df).fit()
est.summary()
