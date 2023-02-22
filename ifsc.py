# Import required module
from ifscApi.getDetails import FetchData

# Assign IFSC code
ifsc = 'SBIN0000454'

# Parse the ifsc code
data = FetchData().getdata(ifsc)

# Display details
print(data)

# Import required modules
import requests

# Assign IFSC code and URL
IFSC_Code = 'SBIN0017292'
URL = "https://ifsc.razorpay.com/"

# Use get() method
data = requests.get(URL + IFSC_Code).json()

# Display bank details
print(data)