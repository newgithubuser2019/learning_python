import pandas as pd
import recordlinkage
hospital_accounts = pd.read_csv('hospital_account_info.csv', header = None, sep='\n')
hospital_accounts = hospital_accounts[0].str.split(',', expand=True)
hospital_reimbursement = pd.read_csv('hospital_reimbursement.csv', header=None, sep='\n')
hospital_reimbursement = hospital_reimbursement[0].str.split(',', expand=True)
indexer = recordlinkage.Index()
indexer.full()
