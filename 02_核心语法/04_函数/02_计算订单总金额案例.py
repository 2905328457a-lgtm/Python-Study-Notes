"""
案例2:定义一个用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额的函数。
具体规则如下:
1. 优惠券需要商品金额满5000才可以使用,且优惠券金额不能超过商品总价。
2. 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。
"""
def calc_order_cost(*args:tuple[str, float, int], coupon: int=0, score: int=0, express: float=0.0):
    """
    根据传入的商品信息计算订单的总金额
    :param args: 商品信息(商品名、价格、数量)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额 = 价格 * 数量 - 优惠券 - 积分抵扣 + 运费
    """
    # 1.商品信息
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
    # 2.优惠券
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon
    # 3.积分
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100
    # 4.运费
    total_cost += express
    return total_cost

s = calc_order_cost(("qew", 555.5, 5), coupon=100, score=100, express=9.9)
print(s)