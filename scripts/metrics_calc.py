def calculate_metrics(TP, FP, TN, FN):
    recall = TP / (TP + FN)
    
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    
    precision = TP / (TP + FP)
    
    f1_score = (2 * precision * recall) / (precision + recall)
    
    return recall, accuracy, precision, f1_score

# TP, FP, TN, FN values
TP= 138 
FP= 4
TN= 175
FN= 58

recall, accuracy, precision, f1_score = calculate_metrics(TP, FP, TN, FN)

print("Recall:", recall)
print("Precision:", precision)
print("Accuracy:", accuracy)
print("F1 Score:", f1_score)
