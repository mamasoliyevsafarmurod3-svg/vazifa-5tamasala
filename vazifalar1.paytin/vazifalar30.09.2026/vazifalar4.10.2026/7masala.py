def talaba_info(**malumotlar):
    for kalit, qiymat in malumotlar.items():
        print(f"{kalit.title()}: {qiymat}")

talaba_info(ism="Aziz", yosh=20, shahar="Samarqand")