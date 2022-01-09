print("=============================================")
print("SOP-V")
print("5200411001")
print("RATNA ROCHMANNINGRUM")
print("=============================================")

def createQueue():
    dataQueue = []
    return dataQueue
def enqueue(dataQueue,data):
    dataQueue.insert(0,data)
    return dataQueue
def dequeue(dataQueue):
    data = dataQueue.pop()
    return data
def isEmpty(dataQueue):
    return dataQueue==[]
def size(dataQueue):
    return len(dataQueue)
def inputdata(jumlah):
    tampung = []
    for i in range (jumlah):
        nama = input("nama aplikasi{} :" .format(i)).upper()
        waktu = int(input("lama waktu aplikasi : "))
        tampung.append([nama,waktu])
    return tampung
def Task_Schedulling(waktu_Prosesor,tugas):
    q = createQueue()
    for i in tugas:
        enqueue(q,i)
    print ("jadwal proses",q)
    hitung = 1
    while not isEmpty(q):
        print ("proses ",hitung)
        hitung += 1
        temp = dequeue(q)
        pengurangan = temp[1] - waktu_Prosesor
        if pengurangan > 0:
            enqueue(q,temp)
            q [0][1] = pengurangan
            print ("\tproses {} di Proses, Sisa Waktu Proses {} = {}".format(temp[0],temp[0],pengurangan))
        else:
            print ("\tproses {} Selesai Diproses".format(temp[0]))
        print ("\t Proses yang Tersisa",q)
jumlah = int(input("Jumlah proses yang akan di jalankan :"))
task = inputdata(jumlah)
waktu = int(input("Quantum Time  :"))
Task_Schedulling(waktu,task)