print("=============================================")
print("SOP-V")
print("5200411001")
print("RATNA ROCHMANNINGRUM")

# Inputan
print("=============================================")
ram = int(input("Kapasitas Ram : "))
blok = 2
petabit = int(input("kapasitas petabit : "))
sistemOperasi = int(input("kapasitas sistemOpersi (KBps) : "))
program1 = int(input("Kapasitas program1 (KBps)  : "))
program2 = int(input("kapasitas program2 (KBps) "))

# Rumus
perpetabit = (ram/blok)
sistemOperasi = (ram - sistemOperasi - program1 - program2)
totalram = (sistemOperasi + program1 + program2)
lokasi = (program1 + program2)/perpetabit

# Hasil
print("+---------------------------------------------+")
print("total ram : " , ram)
print("Kapasitas petabit adalah : " , petabit)
print("kapasitas perpetabit adalah : " , petabit)
print("ram terpakai :  " , totalram)
print("ram tidak terpakai : " , sistemOperasi)
print("total blok value 1 :" , lokasi)
print("total blok value 0 : " , blok - lokasi)