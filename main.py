import okx.Account as Account
from dotenv import load_dotenv
import os

load_dotenv(".env")

def getAccountConfig():
    # Load API credentials from environment variables
    apikey = os.environ.get("apikey")
    secretkey = os.environ.get("secretkey")
    passphrase = os.environ.get("passPhrase")

    # Set the environment flag (0 for production, 1 for demo)
    flag = "0"  # Change this to "0" if you want to connect to the production environment

    try:
        # Initialize the account API
        accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

        # Retrieve current account configuration
        result = accountAPI.get_account_config()
        print("Account Configuration:", result)
    except Exception as e:
        print("Error:", str(e))

getAccountConfig()