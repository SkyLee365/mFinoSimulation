import socket
import mFinoUtils

IP = "10.17.85.22"
Port = 8583

# Payment (Topup)
# msg = mFinoUtils.getMsgForPayment("88295290170","180000","5011","14","5000")
# Account Inquiry / Postpaid Bill Inquiry
# msg=mFinoUtils.getMsgForInquiry("88295290170","380000","5011","14")
# Postpaid Bill Payment
# msg = mFinoUtils.getMsgForPayment("88295290170","280000","5011","14","5000")
# Share Load (P2P) - Transfer balance
# msg = mFinoUtils.getMsgForTransfer("88295290170","400000","5011","14","5000","88295290171")
# Package Inquiry
# msg = mFinoUtils.getMsgForPackageInquiry("88295290170","390000","5011","14","329068","358")
# Package Purchase
# msg = mFinoUtils.getMsgForPackagePurchase("88295290170", "490000", "5011", "14", "20000", "329067", "358")

def Judgeinput(var):
    if var == 0 :
        exit()
    if var > 0 and var < 7 :
        run(var)
    else:
        print("Input error!")
        init()

def run(var):
    if var == 1:
        MobileNumber = input("MobileNumber:")
        Amount = input("Amount:")
        msg = mFinoUtils.getMsgForPayment(MobileNumber, "180000", "5011", "14", Amount)
    elif var == 2:
        MobileNumber = input("MobileNumber:")
        msg = mFinoUtils.getMsgForInquiry(MobileNumber, "380000", "5011", "14")
    elif var == 3:
        MobileNumber = input("MobileNumber:")
        Amount = input("Amount:")
        msg = mFinoUtils.getMsgForPayment(MobileNumber, "280000", "5011", "14", Amount)
    elif var == 4:
        SourceMobileNumber = input("SourceMobileNumber:")
        DestinationMobileNumber = input("DestinationMobileNumber:")
        Amount = input("Amount:")
        msg = mFinoUtils.getMsgForTransfer(SourceMobileNumber, "400000", "5011", "14", Amount, DestinationMobileNumber)
    elif var == 5:
        MobileNumber = input("MobileNumber:")
        PackageID = input("PackageID:")
        AreaID = input("AreaID:")
        msg = mFinoUtils.getMsgForPackageInquiry(MobileNumber, "390000", "5011", "14", PackageID, AreaID)
    elif var == 6:
        MobileNumber = input("MobileNumber:")
        Amount = input("Amount:")
        PackageID = input("PackageID:")
        AreaID = input("AreaID:")
        msg = mFinoUtils.getMsgForPackagePurchase(MobileNumber, "490000", "5011", "14", Amount, PackageID, AreaID)
    print(msg)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((IP, Port))
        s.sendall(msg.encode())
        date = s.recv(1024)
        print(date.decode())
        init()


def init():
    print("Input number as follow:")
    print("0: quit")
    print("1: Payment / Topup")
    print("2: Account Inquiry / Postpaid Bill Inquiry")
    print("3: Postpaid Bill Payment")
    print("4: Share Load / Transfer balance")
    print("5: Package Inquiry")
    print("6: Package Purchase")
    Judgeinput(int(input("Select:")))

if __name__ == "__main__":
    print("Welcome to use simulation tool for mFino.")
    init()