print("Insert hours: ", end="")
h_sec = int(input()) * 60 * 60 
print("Insert minutes: ", end="")
m_sec = int(input()) * 60
print("Insert seconds: ", end="")
sec = int(input())
print("Total seconds:", h_sec + m_sec + sec)