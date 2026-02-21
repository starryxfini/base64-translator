import base64

print("do you want to " \
"1. encode a string (normal string -> base64)" \
"2. decode a string (base64 -> normal string)")

activity = input("")

string = input("enter your string: ")

if activity == "1":
    encoded_text = base64.b64encode(string.encode('utf-8'))
    encoded_text_str = encoded_text.decode('utf-8')
    print("encoded string:", encoded_text_str)

elif activity == "2":
    decoded_text_bytes = base64.b64decode(string.encode('utf-8'))
    decoded_text = decoded_text_bytes.decode('utf-8')
    print("decoded string:", decoded_text)

else:
    print("that was no option u duck!")