# # loader.py
# import os
# import pandas as pd

# CORE_PATH = "data/core"
# SUPP_PATH = "data/supplementary"

# def load_folder(folder):
#     files = {}

#     for file in os.listdir(folder):
#         if file.endswith(".xlsx"):
#             path = os.path.join(folder, file)

#             try:
#                 df = pd.read_excel(path)

#                 files[file] = df

#                 print(f"Loaded: {file} | Rows: {len(df)}")

#             except Exception as e:
#                 print(f"Error loading {file}: {e}")

#     return files


# if __name__ == "__main__":

#     print("\n=== CORE FILES ===")
#     core_data = load_folder(CORE_PATH)

#     print("\n=== SUPPLEMENTARY FILES ===")
#     supp_data = load_folder(SUPP_PATH)

#     print("\nAll files loaded successfully.")










# import os
# import pandas as pd

# folders = ["data/core", "data/supplementary"]

# for folder in folders:
#     print(f"\n===== {folder} =====\n")

#     for file in os.listdir(folder):
#         if file.endswith(".xlsx"):

#             path = os.path.join(folder, file)

#             try:
#                 df = pd.read_excel(path)

#                 print(f"\n{'='*50}")
#                 print(file)
#                 print(f"{'='*50}")

#                 print("Rows:", len(df))
#                 print("Columns:")

#                 for col in df.columns:
#                     print(" -", col)

#             except Exception as e:
#                 print(file, e)












import os
import pandas as pd

CORE_PATH = "data/core"
SUPP_PATH = "data/supplementary"

def load_core_file(path):
    # Row 1 contains actual headers
    return pd.read_excel(path, header=1)

def load_supp_file(path):
    # Supplementary files already have proper headers
    return pd.read_excel(path)

def load_folder(folder, is_core=False):
    data = {}

    for file in os.listdir(folder):
        if file.endswith(".xlsx"):
            path = os.path.join(folder, file)

            try:
                if is_core:
                    df = load_core_file(path)
                else:
                    df = load_supp_file(path)

                data[file] = df

                print(f"\nLoaded: {file}")
                print(f"Rows: {len(df)}")
                print("Columns:")
                print(df.columns.tolist())

            except Exception as e:
                print(f"Error loading {file}: {e}")

    return data


if __name__ == "__main__":

    print("\n=== CORE FILES ===")
    core_data = load_folder(CORE_PATH, is_core=True)

    print("\n=== SUPPLEMENTARY FILES ===")
    supp_data = load_folder(SUPP_PATH)

    print("\nAll files loaded successfully.")