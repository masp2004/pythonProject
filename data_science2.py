import matplotlib.pyplot as plt
import pandas as pd


# Sie haben eine Schraubenlänge von 70mm spezifiziert.
# Zwei Zulieferer schicken Ihnen Muster mit je 250 Schrauben zur Evaluation.
# Charakterisieren Sie die Zulieferer ausführlich. Wem geben Sie den Auftrag?

def load_data(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None


# Load the data from both suppliers
data_a = load_data(r"/Users/marvinspiegel/Downloads/data_a.csv")
data_b = load_data(r"/Users/marvinspiegel/Downloads/data_b.csv")

# Print the column names to check them
print("Supplier A Columns:", data_a.columns)
print("Supplier B Columns:", data_b.columns)

# Ensure both datasets were loaded successfully
if data_a is not None and data_b is not None:
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Assuming the correct column names are identified (replace 'length' with the actual name)
    ax[0].scatter(data_a.index, data_a['length'], color="red", label='Supplier A')
    ax[0].set_title('Supplier A Screw Lengths')
    ax[0].set_xlabel('Index')
    ax[0].set_ylabel('Length (mm)')

    ax[1].scatter(data_b.index, data_b['length'], color="blue", label='Supplier B')
    ax[1].set_title('Supplier B Screw Lengths')
    ax[1].set_xlabel('Index')
    ax[1].set_ylabel('Length (mm)')

    # Adjust layout for better visualization
    plt.tight_layout()
    plt.show()
else:
    print("Unable to load one or both datasets.")
