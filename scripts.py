import os
import re
import collections
import socket
import contractions


def word_count(text):
    words = re.findall(r"\b\w+'\w+|\w+\b", text)  
    word_freq = collections.Counter(words)
    return len(words), word_freq

def make_dir(dir_path):
     if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
    return text


if __name__ == "__main__":
    current_path = os.getcwd()

    file1 = "IF-1.txt"
    file2 = "AlwaysRememberUsThisWay-1.txt"
    result_file = "result.txt"
    output_folder = "output"

    dir_path = os.path.join(current_path,output_folder)
    result_path = os.path.join(dir_path,result_file)

    make_dir(dir_path)
    
    source_text1 = read_file(os.path.join(current_path,file1))
    source_text2 = read_file(os.path.join(current_path,file2))
    expanded_text = contractions.fix(source_text2)
    words_file1, freq_file1 = word_count(source_text1)
    words_file2, freq_file2 = word_count(expanded_text)

    grand_total_words = words_file1 + words_file2


    top3_file1 = freq_file1.most_common(3)
    top3_file2 = freq_file2.most_common(3)

    ip_address = socket.gethostbyname(socket.gethostname())

    with open(result_path, "w") as result_file:
        result_file.write(f"Total words in {file1}: {words_file1}\n")
        result_file.write(f"Total words in {file2}: {words_file2}\n")
        result_file.write(f"Grand total words: {grand_total_words}\n")
        result_file.write(f"Top 3 words in {file1}: {top3_file1}\n")
        result_file.write(f"Top 3 words in {file2}: {top3_file2}\n")
        result_file.write(f"Container IP Address: {ip_address}\n")


    with open(result_path, "r") as result_file:
        print(result_file.read())