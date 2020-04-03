def rake_garden(garden):
    """(str) -> str
    Replace any other word than "rock" or "gravel" with "gravel".
    """
    #Convert string with spaces to list.
    a = garden.split()
    for i in range(len(a)):
      if a[i] == "rock" and a[i] != "gravel":
        a[i] = "rock"
      else:
        a[i]= "gravel"
    #Convert list into string with spaces in place of commas.
    a1 = " ".join(a)
    return a1
