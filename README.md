# RSA_encryption
A code generator program for RSA + appying the RSA encryption to the chatroom application

## Code generator
This python file produces public and private codes for encrypting data 
It also test whether the generated codes work properly or not. That is, the function "Keys()" using a variable named "m = 'This is a test'" checks the codes. If the codes work well, "Keys()" return them, otherwise it will produce a new set of codes.

## RSA_encrypted Chatroom
I used this code_generator program to secure my client-server chatroom. 
The server and clients have their own public and private keys. When a client binds to the server, the server sends it public key to the client, and the client do the same.
After this step, both client and server, encode thier message using their private key and then send the message to each other. They also decode the message using the public key of each other sent at the beginning of the connection.
