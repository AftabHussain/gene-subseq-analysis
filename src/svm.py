import json

def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data

# Load the training and validation data
train_file_path = '/home/aftab/workspace/git-repos/gene-subseq-analysis/data/synth_gseq_family_k3_subseq/train_enriched.jsonl'
val_file_path = '/home/aftab/workspace/git-repos/gene-subseq-analysis/data/synth_gseq_family_k3_subseq/val_enriched.jsonl'
train_data = load_jsonl(train_file_path)
val_data = load_jsonl(val_file_path)

# Extract X and Y for training and validation
X_train = [item['subseqs_A_k3'] for item in train_data]
Y_train = [item['gene_family'] for item in train_data]
X_val = [item['subseqs_A_k3'] for item in val_data]
Y_val = [item['gene_family'] for item in val_data]

print("Extracted train and validation data.")

# Display the first few entries to verify
print(X_train[:5], Y_train[:5])
print(X_val[:5], Y_val[:5])

from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np

# Encode the gene family labels
label_encoder = LabelEncoder()
Y_train_encoded = label_encoder.fit_transform(Y_train)
Y_val_encoded = label_encoder.transform(Y_val)

# Convert X to numpy array for further processing
X_train = np.array(X_train).reshape(-1, 1)
X_val = np.array(X_val).reshape(-1, 1)

# Normalize X if needed
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

print("Done preparing data for training.")

print("Normalized features and encoded labels for some sample examples:")
# Display the encoded labels and normalized features
print(X_train[:5], Y_train_encoded[:5])
print(X_val[:5], Y_val_encoded[:5])

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Define and train the SVM model
svm_model = SVC(kernel='linear')

print("Now training SVM model..")
svm_model.fit(X_train, Y_train_encoded)

# Predict on the validation set
print("Done training, now make predictions on val set")
Y_pred = svm_model.predict(X_val)

# Calculate the accuracy
accuracy = accuracy_score(Y_val_encoded, Y_pred)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")

