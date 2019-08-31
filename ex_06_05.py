text = "X-DSPAM-Confidence:0.8475"
colpos = text.find(":")
print(colpos)
extract = text[colpos+1: ]
print(extract)
ftract = float(extract)
print(ftract)
