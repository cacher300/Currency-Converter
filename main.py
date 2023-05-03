import tkinter as tk
import requests

# Define the API endpoint and headers
url = "https://api.apilayer.com/exchangerates_data/convert"
headers = {
    "apikey": ""
}

# Define the GUI
root = tk.Tk()
root.title("Currency Converter")

# Define the input fields
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_label = tk.Label(root, text="From:")
from_label.grid(row=1, column=0)

from_entry = tk.Entry(root)
from_entry.grid(row=1, column=1)

to_label = tk.Label(root, text="To:")
to_label.grid(row=2, column=0)

to_entry = tk.Entry(root)
to_entry.grid(row=2, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

# Define the conversion function
def convert():
    # Get the user input
    amount = amount_entry.get()
    _from = from_entry.get()
    to = to_entry.get()

    # Make the API request
    query_params = {"amount": amount, "from": _from, "to": to}
    response = requests.get(url, headers=headers, params=query_params)

    # Update the result label
    if response.status_code == 200:
        data = response.json()
        result_label.config(text=f"{data['result']:.2f} {to}")
    else:
        result_label.config(text="Error: Failed to convert currency")

# Define the convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=4, column=0, columnspan=2)

# Start the GUI loop
root.mainloop()
