


import random


weeklyRevenue = 0.0


dropBox = 0.0
broughtForward = 0.0


prizePercentage = [0, 0, 0.05, 0.1, 0.2, 0.25, 0.4]




def draw():
    numbers=[]
    while(len(numbers)<6):
        number=random.randint(1,49)
        if(not number in numbers):
            numbers.append(number)
    return numbers





def play_week():
    global weeklyRevenue
    people_list=[]

    people_num = random.randint(50000, 100000)

    for i in range(1,people_num+1):
        people_list.append(draw())

    weeklyRevenue=people_num*3
    return people_list






play_week()






def decide_winners(played_tickets, lucky_numbers):
    right_guesses = [0,0,0,0,0,0,0]
    for i in played_tickets:
        index=0
        guess=0
        for j in i:
            if(j==lucky_numbers[index]):
                guess+=1
            index+=1
        right_guesses[guess]+=1
    return right_guesses




shared=weeklyRevenue*0.55
dropBox=weeklyRevenue*0.45

def prize_payout(winners):
    global shared
    global dropBox
    global broughtForward
    x=0
    if(winners[-1]==0):
        broughtForward+=shared*prizePercentage[-1]
    for i in prizePercentage:
        earned = 0

        if (winners[x] != 0):
            earned = (shared * i) / winners[x]
        if (earned != 0):
            print(f"{winners[x]} person who knew {x} out of 6 earned {earned:,.2f} liras.")
        elif (earned == 0 and i != 0):
            print(f"Nobody knew {x} out of 6 and the prize that will be forwarded to next week is {shared * i:,.2f} liras.")

        if (winners[x]== 0):
            dropBox+= shared*i


        x += 1







def play_year():
    global weeklyRevenue
    global dropBox
    six_founders=0
    for i in range(1,13):
        for j in range(1,5):
            lucky_numbers = draw()
            played_tickets = play_week()
            print("MONTH : {}".format(i))
            print("WEEK : {}".format(j))
            print("Weekly revenue : {}".format(weeklyRevenue))
            print(f"Total prize : {weeklyRevenue*0.55:,.2f}")
            winners=decide_winners(played_tickets,lucky_numbers)
            prize_payout(winners)
            if(winners[-1]!=0):
                six_founders+=winners[-1]

            print("*******************")
    if(six_founders!=0):
        print(f"Total revenue of the dropbox at the end of the year is : {broughtForward+dropBox:,.2f} liras.")
    else:
        print(f"Total revenue of the dropbox at the end of the year is : {dropBox:,.2f} liras.")






# This the only function call that you need to initiate(trigger) the your simulation.
play_year()
