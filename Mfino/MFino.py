import socket
import mFinoUtils
from sys import exit

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


def judgeinput(var):
    if var == 0:
        exit()
    if 0 < var < 8:
        run(var)
    else:
        print("Input error!")
        init()


def run(var):
    msg = "NULL"
    if var == 1:
        mobile_number = input("MobileNumber:")
        amount = input("Amount:")
        msg = mFinoUtils.get_msg_for_payment(mobile_number, "180000", "0006", "881", amount)
    elif var == 2:
        mobile_number = input("MobileNumber:")
        msg = mFinoUtils.get_msg_for_inquiry(mobile_number, "380000", "5011", "14")
    elif var == 3:
        mobile_number = input("MobileNumber:")
        amount = input("Amount:")
        msg = mFinoUtils.get_msg_for_payment(mobile_number, "280000", "5011", "14", amount)
    elif var == 4:
        source_mobile_number = input("SourceMobileNumber:")
        destination_mobile_number = input("DestinationMobileNumber:")
        amount = input("Amount:")
        msg = mFinoUtils.get_msg_for_transfer(source_mobile_number, "400000", "5011", "14", amount,
                                              destination_mobile_number)
    elif var == 5:
        mobile_number = input("MobileNumber:")
        package_id = input("PackageID:")
        area_id = input("AreaID:")
        msg = mFinoUtils.get_msg_for_package_inquiry(mobile_number, "390000", "5011", "14", package_id, area_id)
    elif var == 6:
        mobile_number = input("MobileNumber:")
        amount = input("Amount:")
        package_id = input("PackageID:")
        area_id = input("AreaID:")
        msg = mFinoUtils.get_msg_for_package_purchase(mobile_number, "490000", "5011", "14", amount, package_id,
                                                      area_id)
    elif var == 7:
        mobile_number = input("MobileNumber:")
        amount = input("Amount:")
        package_id = input("PackageID:")
        city_code = input("CityCode:")
        msg = mFinoUtils.get_msg_for_package_purchase_area(mobile_number, "590000", "5011", "14", amount, package_id,
                                                           city_code)
    print(msg)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, int(port)))
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
    print("7: Package Purchase Area")
    judgeinput(int(input("Select:")))


if __name__ == "__main__":
    print("Welcome To Use Simulation Tool For MFino Testing.")
    print("Prohibit The Use Of This Tool In Production Systems")
    ip = input("Server IP:")
    port = input("Server Port:")
    init()
