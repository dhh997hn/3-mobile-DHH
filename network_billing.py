import network_invoice
def idata(ip_address):
    _,data = network_invoice.input_data(ip_address)
    src = 0
    dst = 1
    byte = 2
    sum_byte = 0
    cost_per_mb = 1
    total_cost = 0

    for row in data:
        ip = row[src].split()[0]
        if ip == ip_address:
            ds = row[dst].split()[0]
            by = row[byte].split()[0]
            sum_byte += float(by)

    sum_byte = sum_byte/pow(2,20)
    total_cost = sum_byte*cost_per_mb
    return round(total_cost,2)