import uuid
from datetime import datetime


def get_bit_map(processing_code):
    if processing_code in ('380000', '390000'):
        return "0200223A400108218008"
    elif processing_code in ('180000', '280000', '490000', '590000'):
        return "0200323A400108A18008"
    elif processing_code in '400000':
        return "02003238400108010008"
    else:
        return "NULL"


def get_transaction_amount(amount):
    return ("000000000000" + amount)[-12:]


def get_transmission_time():
    return datetime.now().strftime('%m%d%H%M%S')


def get_system_trace_audit_number():
    return datetime.now().strftime('%f')


def get_local_transaction_time():
    return datetime.now().strftime('%H%M%S')


def get_local_transaction_date():
    return datetime.now().strftime('%m%d')


def get_settlement_date():
    return datetime.now().strftime('%m%d')


def get_bank_code(bank_code):
    if len(bank_code) <= 3:
        return "03" + ("000" + bank_code)[-3:]
    elif len(bank_code) < 10:
        return "0" + str(len(bank_code)) + bank_code
    else:
        return "03881"


def get_retrieval_reference_number():
    return uuid.UUID(int=uuid.getnode()).hex[-12:]


def get_card_acceptor_terminal_identification():
    return "11      "


def get_card_acceptor_name():
    return "SMS SMART                               "


def get_product_indicator():
    return "5100"


def get_currency_code():
    return "360"


def get_mdn(mdn):
    return ("62" + mdn + "                ")[0:16]


def get_package_id(package_id):
    return ("000000000000" + package_id)[-12:]


def get_area_id(area_id):
    return (area_id + "         ")[0:9]


def get_city_code(city_code):
    return (city_code + "                                                  ")[0:50]


def get_msg_for_inquiry(mobile_number, processing_code, merchant_code, bank_code):
    msg = get_bit_map(
        processing_code) + processing_code + get_transmission_time() + get_system_trace_audit_number() + \
          get_local_transaction_time() + get_local_transaction_date() + get_settlement_date() + merchant_code + \
          get_bank_code(bank_code) + get_retrieval_reference_number() + get_card_acceptor_name() + \
          get_product_indicator() + get_currency_code() + "016" + get_mdn(mobile_number)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def get_msg_for_payment(mobile_number, processing_code, merchant_code, bank_code, transaction_amount):
    msg = get_bit_map(processing_code) + processing_code + get_transaction_amount(transaction_amount) + \
          get_transmission_time() + get_system_trace_audit_number() + get_local_transaction_time() + \
          get_local_transaction_date() + get_settlement_date() + merchant_code + get_bank_code(bank_code) + \
          get_retrieval_reference_number() + get_card_acceptor_terminal_identification() + get_card_acceptor_name() + \
          get_product_indicator() + get_currency_code() + "016" + get_mdn(mobile_number)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def get_msg_for_transfer(mobile_number, processing_code, merchant_code, bank_code, transaction_amount, mobile_number_b):
    msg = get_bit_map(processing_code) + processing_code + get_transaction_amount(transaction_amount) + \
          get_transmission_time() + get_system_trace_audit_number() + get_local_transaction_time() + \
          get_local_transaction_date() + merchant_code + get_bank_code(bank_code) + get_retrieval_reference_number() + \
          get_product_indicator() + "032" + get_mdn(mobile_number) + get_mdn(mobile_number_b)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def get_msg_for_package_inquiry(mobile_number, processing_code, merchant_code, bank_code, package_id, area_id):
    msg = get_bit_map(processing_code) + processing_code + get_transmission_time() + get_system_trace_audit_number() + \
          get_local_transaction_time() + get_local_transaction_date() + get_settlement_date() + merchant_code + \
          get_bank_code(bank_code) + get_retrieval_reference_number() + get_card_acceptor_name() + \
          get_product_indicator() + get_currency_code() + "037" + get_mdn(mobile_number) + \
          get_package_id(package_id) + get_area_id(area_id)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def get_msg_for_package_purchase(mobile_number, processing_code, merchant_code, bank_code, transaction_amount,
                                 package_id, area_id):
    msg = get_bit_map(processing_code) + processing_code + get_transaction_amount(transaction_amount) + \
          get_transmission_time() + get_system_trace_audit_number() + get_local_transaction_time() + \
          get_local_transaction_date() + get_settlement_date() + merchant_code + get_bank_code(bank_code) + \
          get_retrieval_reference_number() + get_card_acceptor_terminal_identification() + get_card_acceptor_name() + \
          get_product_indicator() + get_currency_code() + "037" + get_mdn(mobile_number) + \
          get_package_id(package_id) + get_area_id(area_id)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg


def get_msg_for_package_purchase_area(mobile_number, processing_code, merchant_code, bank_code, transaction_amount,
                                      package_id, city_code):
    msg = get_bit_map(processing_code) + processing_code + get_transaction_amount(transaction_amount) + \
          get_transmission_time() + get_system_trace_audit_number() + get_local_transaction_time() + \
          get_local_transaction_date() + get_settlement_date() + merchant_code + get_bank_code(bank_code) + \
          get_retrieval_reference_number() + get_card_acceptor_terminal_identification() + get_card_acceptor_name() + \
          get_product_indicator() + get_currency_code() + "078" + get_mdn(mobile_number) + \
          get_package_id(package_id) + get_city_code(city_code)
    msg = ("0" * 4 + str(len(msg)))[-4:] + msg
    return msg
