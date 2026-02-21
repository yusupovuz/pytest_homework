def duty_free(price, discount, holiday_cost):
    t = price*0.01*discount
    return int(holiday_cost/t)