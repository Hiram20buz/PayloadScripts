# PayloadScripts
## Run python code with base64 and ...

### This is a proof of concept 
### You can codificate your python code with base64 and maybe you can use XOR encryption or any type of encryption.


```python
import base64

base64_message = 'JycnCklucHV0OiBudW1zID0gWzIsNywxMSwxNV0sIHRhcmdldCA9IDkKT3V0cHV0OiBbMCwxXQpFeHBsYW5hdGlvbjogQmVjYXVzZSBudW1zWzBdICsgbnVtc1sxXSA9PSA5LCB3ZSByZXR1cm4gWzAsIDFdLgonJycKCm51bXMgPSBbMywyLDRdCnRhcmdldCA9IDYKCmZvciBpIGluIHJhbmdlKGxlbihudW1zKSk6CiAgICBmb3IgaiBpbiByYW5nZShsZW4obnVtcykpOgogICAgICAgIGlmKG51bXNbaV0gKyBudW1zW2pdID09IHRhcmdldCBhbmQgbnVtc1tpXSE9bnVtc1tqXSk6CiAgICAgICAgICAgIHByaW50KGksaik='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

exec(message)
```

### This message is in base64 format
```base64

JycnCklucHV0OiBudW1zID0gWzIsNywxMSwxNV0sIHRhcmdldCA9IDkKT3V0cHV0OiBbMCwxXQpFeHBsYW5hdGlvbjogQmVjYXVzZSBudW1zWzBdICsgbnVtc1sxXSA9PSA5LCB3ZSByZXR1cm4gWzAsIDFdLgonJycKCm51bXMgPSBbMywyLDRdCnRhcmdldCA9IDYKCmZvciBpIGluIHJhbmdlKGxlbihudW1zKSk6CiAgICBmb3IgaiBpbiByYW5nZShsZW4obnVtcykpOgogICAgICAgIGlmKG51bXNbaV0gKyBudW1zW2pdID09IHRhcmdldCBhbmQgbnVtc1tpXSE9bnVtc1tqXSk6CiAgICAgICAgICAgIHByaW50KGksaik=

```

### The meaning is the next python code
```python
'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

nums = [3,2,4]
target = 6

for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[i] + nums[j] == target and nums[i]!=nums[j]):
            print(i,j)

```
### https://www.base64decode.org/

### The main idea is to hide the payload inside an image or another file and then read the binary data of a file to ...
### recover the base64 code of any type of codification to use it as the example above.


### Using the exec() function in python.
