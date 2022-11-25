#write a function findSecretMessage that will find the secret words
#of the message and return them in order. The words in the secret
#message should be ordered in the order in which they are found as a duplicate.
#Example:'This is a test. this test is fun.' #-> this test is
import re
def find_secret_message(paragraph):
    
    uniq = []
    message = []
    p = re.sub(r"[^a-zA-z0-9\s\-]+", "", paragraph).lower().strip()
    print(p)
    paragraph_list = p.split()
    for i in paragraph_list:
        if i not in uniq:
            uniq.append(i)
        else:
            message.append(i)
    result = []
    for item in message:
        if item not in result:
            result.append(item)
            
    
    return " ".join(result)
