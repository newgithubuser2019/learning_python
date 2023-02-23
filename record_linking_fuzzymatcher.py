import pandas as pd
from pathlib import Path
import fuzzymatcher
hospital_accounts = pd.read_csv('hospital_account_info.csv', header = None, sep='\n')
hospital_accounts = hospital_accounts[0].str.split(',', expand=True)
hospital_reimbursement = pd.read_csv('hospital_reimbursement.csv', header=None, sep='\n')
hospital_reimbursement = hospital_reimbursement[0].str.split(',', expand=True)
print("hospital_accounts")
print(hospital_accounts)
print("\n")
print("hospital_reimbursement")
print(hospital_reimbursement)