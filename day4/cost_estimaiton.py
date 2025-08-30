import locale


locale.setlocale( locale.LC_ALL, '' )
#oil
oil = 6000
oil_pirce = 60_000 #rupiah
oil_km = 0
#break
m_break = 25000
m_break_price = 200_000 #rupiah
m_break_km = 0
#v-belt
v_belt = 28000
v_belt_price = 200_000 #rupiah
v_belt_km = 0
#bearing
bearing = 20000
bearing_price = 150_000
bearing_km = 0
#cvt service
cvt_ser = 8000
cvt_ser_price = 100_000
cvt_ser_km = 0
# roller cvt
roller_cvt = 15000
roller_cvt_price = 350_000
roller_cvt_km = 0
# ban
tires = 35000 #ban
tires_price = 1_000_000
tires_km = 0

km_motor = 0
gas_consume = 65 #km
daily_use = 200 #km
gas_price = 25_000 #rupiah

total_price = 0
price_all = 0
count_km_every_35000 = 0
income_daily = 100_000
total_income = 0
km_motor_gas = 0
total_gas_daily = 0

for i in range(733):
    print(f'day {i + 1}')

    km_motor +=daily_use
    oil_km +=daily_use
    m_break_km +=daily_use
    v_belt_km +=daily_use
    bearing_km +=daily_use
    cvt_ser_km +=daily_use
    roller_cvt_km +=daily_use
    tires_km +=daily_use

    count_km_every_35000 += daily_use
    total_income += income_daily
    km_motor_gas += daily_use
    if km_motor_gas > gas_consume:
        total_gas_daily += gas_price
        km_motor_gas %= gas_consume

    if oil_km >= oil :
        total_price += oil_pirce
        oil_km %= oil

    if m_break_km >= m_break:
        total_price += m_break_price
        m_break_km %= m_break

    if v_belt_km >= v_belt:
        total_price += v_belt_price
        v_belt_km %= v_belt

    if bearing_km >= bearing:
        total_price += bearing_price
        bearing_km %= bearing

    if cvt_ser_km >= cvt_ser:
        total_price += cvt_ser_price
        cvt_ser_km %= cvt_ser

    if roller_cvt_km >= roller_cvt:
        total_price += roller_cvt_price
        roller_cvt_km %= roller_cvt

    if tires_km >= tires:
        total_price += tires_price
        tires_km %= tires_km




    print(f'Km motor gas daily = {km_motor_gas}, km for gas = {km_motor_gas}, gas price = {gas_price}')
    total_price += total_gas_daily
    total_gas_daily = 0


    print(f'total price Rp{locale.currency( total_price, grouping=True )}, total kilometer :{km_motor},'
          f' total income: {locale.currency( total_income, grouping=True )}, '
          f'total uang bersih = {locale.currency( total_income-total_price, grouping=True )}')

