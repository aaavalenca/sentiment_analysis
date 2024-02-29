import csv
import glob
import os

def txt_to_csv(file_list_sorted, sentiment, header_needed=True):
    mode = 'w' if header_needed else 'a'
    with open('data.csv', mode, newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        if header_needed:
            writer.writerow(["review", "sentiment"])
        for file_path in file_list_sorted:
            try:
                with open(file_path, "r", encoding='utf-8') as file:
                    content = file.read()
                    writer.writerow([content, sentiment])
            except UnicodeDecodeError:
                try:
                    with open(file_path, "r", encoding='latin-1') as file:
                        content = file.read() 
                        writer.writerow([content, sentiment])
                except Exception as e:
                    print(f"Couldn't read {file_path}: {e}")

folder_path_neg = 'tokens/neg'
folder_path_pos = 'tokens/pos'
file_list_neg = glob.glob(os.path.join(folder_path_neg, '*'))
file_list_pos = glob.glob(os.path.join(folder_path_pos, '*'))
file_list_sorted_neg = sorted(file_list_neg)
file_list_sorted_pos = sorted(file_list_pos)

txt_to_csv(file_list_sorted_pos, "pos", header_needed=True)
txt_to_csv(file_list_sorted_neg, "neg", header_needed=False)
