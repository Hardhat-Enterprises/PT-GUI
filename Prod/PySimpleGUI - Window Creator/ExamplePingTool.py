from WindowCreator import WindowCreator

w1 = WindowCreator()
w1.AddText("Target IP: ")
w1.AddInputText(index=0)
w1.AddText("Number of packets to send: ")
w1.AddInputText("4", index=1)
w1.AddButton("Ping IP")
w1.AddCloseButton(index=2)

w1.ShowLayout(create_close=False)