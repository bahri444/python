masuk = int(input("input jam masuk :"))
pulang = int(input("input jam pulang :"))
if masuk < pulang:
    lama_kerja = pulang-masuk
else:
    lama_kerja = (pulang+12)-masuk
print("anda kerja selama : ", lama_kerja, ".jam")
