import call_invoice
def idata(phone_number):
    fiels,sdata = call_invoice.input_data(phone_number)
    origin = fiels.index('msisdn_origin') 
    dest = fiels.index('msisdn_dest')
    call = fiels.index('call_duration')
    sms = fiels.index('sms_number')
    
    call_out = 0
    call_in = 0
    free_call = 20 #20 минут бесплатно
    sms_number = 0 
    cost_ci=2 #2руб/минута исходящие звонки
    cost_co=0 #0руб/минута входящие
    cost_sms=2 #смс - 2руб/шт

    for row in sdata:
        if row[origin] == phone_number:
            call_in += float(row[call])
            sms_number += float(row[sms])
        if row[dest] == phone_number:
            call_out += float(row[call])
    if call_in > 20:
        sum_call = round((call_in-free_call)*cost_ci,2)+call_out*cost_co
    sum_sms = sms_number*cost_sms
    return sum_call,sum_sms
