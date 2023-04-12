# Import necessary modules
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import random
import timeit

# Import the Array class from the SortArray module
from SortArray import Array

# Set up Google Sheets API credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'sortarray-credentials.json'
SPREADSHEET_ID = '1d9cP_SKQdwkJJ87SB1I5UoKtOqcF32APF4K0HCnsnN0'
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Create an array with a fixed sequence of 'random' elements
def initArray(size=100, maxValue=100, seed=3.14159):
    arr = Array(size)
    random.seed(seed)
    for i in range(size):
        arr.insert(random.randrange(maxValue))
    return arr

arr = initArray()
print("Array containing", len(arr), "items:\n", arr)

# Test sorting algorithms and measure execution time
for sort_func in [arr.bubbleSort, arr.selectionSort, arr.insertionSort]:
    elapsed = timeit.timeit(sort_func, number=100, globals=globals())
    print(f"{sort_func.__name__} took {elapsed} seconds", flush=True)

# Print the unordered array
arr.traverse()
print('Unordered array contains:\n', arr)

# Insert array values into Google Sheets
values = [[arr.get(i)] for i in range(len(arr))]
range_ = f'Sheet1!A2:A{len(values)+1}' # Define the range to include all rows of the array
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=range_,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Data inserted successfully. {result.get('updatedCells')} cells updated.")

# Bubble sort
arr.bubbleSort()
print('The array sorted by bubbleSort contains: \n', arr)
values = [[arr.get(i)] for i in range(len(arr))]
range2_ = f'Sheet1!B2:B{len(values)+1}' # Define the range to include all rows of the array
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range2_).execute()
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=range2_,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Data inserted successfully. {result.get('updatedCells')} cells updated.")

#Selectionsort
arr.selectionSort()
print('The array sorted by selectionSort contains: \n', arr)
values = [[arr.get(i)] for i in range(len(arr))]
range3_ = 'C2:C'
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range3_).execute()
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=range3_,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Data inserted successfully. {result.get('updatedCells')} cells updated.")

# InsertionSort
arr.insertionSort()
print('The array sorted by insertionSort contains:\n', arr)
values = [[arr.get(i)] for i in range(len(arr))]
range4_ = 'D2:D'
sheet.values().clear(spreadsheetId=SPREADSHEET_ID, range=range4_).execute()
result = sheet.values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=range4_,
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print(f"Data inserted successfully. {result.get('updatedCells')} cells updated.")
