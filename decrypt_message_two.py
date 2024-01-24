encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
cipher_text = encrypted_message
start = 1
end = len(cipher_text) - 2 

decrypted_message = list(cipher_text)
while start <= end:
    decrypted_message[start], decrypted_message[end] = decrypted_message[end], decrypted_message[start]
    start += 2
    end -= 2

decrypted_message = "".join(decrypted_message)
print(decrypted_message)
