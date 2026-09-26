rooms=['a','b','c','d']
status=['dirty','clean','dirty','dirty']
position=0
while True:
    print("Room:", rooms[position])
    if status[position]=='dirty':
        print("Room is dirty")
        print("Cleaning the room")
        print("Room is clean")
        status[position]='clean'
    else:
        print("Room is clean now")

    if all(room==0 for room in status):
        print("All rooms are clean")
        break
    if position<3:
        position+=1
    else:
        position-=1

