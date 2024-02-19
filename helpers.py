from bcrypt import gensalt, hashpw

def hash_passcode(password: str):
  passByte = password.encode('utf-8')
  mySalt = gensalt()
  hashPass = hashpw(passByte, mySalt)
  return hashPass