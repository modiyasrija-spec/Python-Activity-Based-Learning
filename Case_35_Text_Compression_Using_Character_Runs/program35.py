# Case Study 35: Text Compression Using Character Runs

text = input("Enter a string to compress: ")

compressed = ""

if len(text) > 0:
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)

print("\n===== TEXT COMPRESSION REPORT =====")
print("Original text:", text)
print("Compressed text:", compressed)
print("Original length:", len(text))
print("Compressed length:", len(compressed))