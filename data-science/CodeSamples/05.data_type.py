roomGuest = ["王明", "柳宇", "陳尚"]
roomKey = (1111, 2222, 3333)
breakfastChoice = {"中式", "西式", "法式"}
guestBreakfast = {
    "王明":"中式",
    "柳宇":"法式",
    "陳尚":"中式"
}
print("王明有住房嗎? " + str("王明" in roomGuest))
print("陳尚應該沒來住房吧? " + str("陳尚" not in roomGuest))
