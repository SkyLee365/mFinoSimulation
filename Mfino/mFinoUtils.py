import uuid
from datetime import datetime


def getBitMap(processingCode):
    if processingCode in ('380000', '390000'):
        return "0200223A400108218008"
    elif processingCode in ('180000', '280000', '490000'):
        return "0200323A400108A18008"
    elif processingCode in ('400000'):
        return "02003238400108010008"
    else:
        return "NULL"


def getTransactionAmount(Amount):
    return ("000000000000" + Amount)[-12:]


def getTransmissionTime():
    return datetime.now().strftime('%m%d%H%M%S')


def getSystemTraceAuditNumber():
    return datetime.now().strftime('%f')


def getLocalTransactionTime():
    return datetime.now().strftime('%H%M%S')


def getLocalTransactionDate():
    return datetime.now().strftime('%m%d')


def getSettlementDate():
    return datetime.now().strftime('%m%d')


def getBankCode(bankCode):
    if len(bankCode) <= 3:
        return "03" + ("000" + bankCode)[-3:]
    elif len(bankCode) < 10:
        return "0" + str(len(bankCode)) + bankCode
    else:
        return "03881"


def getRetrievalReferenceNumber():
    return uuid.UUID(int=uuid.getnode()).hex[-12:]


def getCardAcceptorTerminalIdentification():
    return "11      "


def getCardAcceptorName():
    return "SMS SMART                               "


def getProductIndicator():
    return "5100"


def getCurrenyCode():
    return "360"


def getMDN(MDN):
    return ("62" + MDN + "                ")[0:16]


def getPackageID(packageID):
    return ("000000000000" + packageID)[-12:]


def getAreaID(areaID):
    return (areaID + "         ")[0:9]


def getMsgForInquiry(mobileNumber, processingCode, merchantCode, bankCode):
    msg = getBitMap(
        processingCode) + processingCode + getTransmissionTime() + getSystemTraceAuditNumber() + getLocalTransactionTime() + getLocalTransactionDate() + getSettlementDate() + merchantCode + getBankCode(
        bankCode) + getRetrievalReferenceNumber() + getCardAcceptorName() + getProductIndicator() + getCurrenyCode() + "016" + getMDN(
        mobileNumber)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def getMsgForPayment(mobileNumber, processingCode, merchantCode, bankCode, transactionAmount):
    msg = getBitMap(
        processingCode) + processingCode + getTransactionAmount(
        transactionAmount) + getTransmissionTime() + getSystemTraceAuditNumber() + getLocalTransactionTime() + getLocalTransactionDate() + getSettlementDate() + merchantCode + getBankCode(
        bankCode) + getRetrievalReferenceNumber() + getCardAcceptorTerminalIdentification() + getCardAcceptorName() + getProductIndicator() + getCurrenyCode() + "016" + getMDN(
        mobileNumber)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def getMsgForTransfer(mobileNumber, processingCode, merchantCode, bankCode, transactionAmount, mobileNumberB):
    msg = getBitMap(
        processingCode) + processingCode + getTransactionAmount(
        transactionAmount) + getTransmissionTime() + getSystemTraceAuditNumber() + getLocalTransactionTime() + getLocalTransactionDate() + merchantCode + getBankCode(
        bankCode) + getRetrievalReferenceNumber() + getProductIndicator() + "032" + getMDN(
        mobileNumber) + getMDN(mobileNumberB)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def getMsgForPackageInquiry(mobileNumber, processingCode, merchantCode, bankCode, packageID, areaID):
    msg = getBitMap(
        processingCode) + processingCode + getTransmissionTime() + getSystemTraceAuditNumber() + getLocalTransactionTime() + getLocalTransactionDate() + getSettlementDate() + merchantCode + getBankCode(
        bankCode) + getRetrievalReferenceNumber() + getCardAcceptorName() + getProductIndicator() + getCurrenyCode() + "037" + getMDN(
        mobileNumber) + getPackageID(packageID) + getAreaID(areaID)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def getMsgForPackagePurchase(mobileNumber, processingCode, merchantCode, bankCode, transactionAmount, packageID, areaID):
    msg = getBitMap(
        processingCode) + processingCode + getTransactionAmount(
        transactionAmount) + getTransmissionTime() + getSystemTraceAuditNumber() + getLocalTransactionTime() + getLocalTransactionDate() + getSettlementDate() + merchantCode + getBankCode(
        bankCode) + getRetrievalReferenceNumber() + getCardAcceptorTerminalIdentification() + getCardAcceptorName() + getProductIndicator() + getCurrenyCode() + "037" + getMDN(
        mobileNumber) + getPackageID(packageID) + getAreaID(areaID)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg
