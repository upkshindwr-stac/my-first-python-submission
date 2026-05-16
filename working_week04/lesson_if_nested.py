name = input("What's your name? ")
is_friend = input("Are you a friend of mike? ").lower()
guest_list = ["John","Julia","Ema","Justin","Laura"]

if is_friend == "Yes":
    if name in [guest.lower() for guest in guest_list]:
        print('Welcome! Please come inside')
    else :
        print('Your name is not included in the guest list. Sorry!')
else:
    print('Get the hell out of here')