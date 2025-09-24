def main():
    marks=[]

    while 1:
        a=input("Введіть ім'я та оцінку студента або stop щоб вивести результат")
        if a == "stop":
            avg_score=0
            mark_A=[]  #10-12
            mark_B=[]  #7-9
            mark_C=[]  #4-6
            mark_D=[]  #0-3
            print("оцінки групи:")
            for i in marks:
                avg_score += i["mark"]
                print(i["name"],"-",i["mark"])

                if 10 <= i["mark"] <=12:
                    mark_A.append(i["name"])

                if 7 <= i["mark"] <=9:
                    mark_B.append(i["name"])

                if 4 <= i["mark"] <=6:
                    mark_C.append(i["name"])

                if 0 <= i["mark"] <=3:
                    mark_D.append(i["name"])


            print("середній бал:",avg_score/len(marks))

            print("відмінників(",len(mark_A),") :",mark_A)
            print("хорошистів(",len(mark_B),") :",mark_B)
            print("відстаючих(",len(mark_C),") :",mark_C)
            print("не здали(",len(mark_D),") :",mark_D)

        else:
            marks.append({"name":a.split(" ")[0],"mark":int(a.split(" ")[1])})


if __name__ == '__main__':
    main()
        

