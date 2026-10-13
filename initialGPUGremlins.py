# As I start on this, i dont have access ot nvida GPU and I will be mostly working on xpu (intel) but in instance where i need plartform agnostic code I wil use this to work for either platform if my code get worthy of exporting

device = "cuda" if torch.cuda.is_available() else ("xpu" if torch.xpu.is_available() else "cpu")

