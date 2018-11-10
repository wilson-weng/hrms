# -*- coding: utf8 -*-
import time

from plugins.plugin import Plugin, Props, Output


class WageByWork3levels(Plugin):

    __plugin_id__ = 'WageByWork3levels'
    __plugin_name__ = '三级按件计费'
    __category__    = 'wage'
    __priority__    = 100000

    __desc__ = '而级件数以下部分按一级单价计算，二级件数至三级件数部分按二级单价计算，以此类推，三级件数以上按三级单价计算'

    lv1_amount = Props(type='int', default=0, nullable=True, comment='一级件数')
    lv1_price = Props(type='float', default=0.00, nullable=True, comment='一级单价')
    lv2_amount = Props(type='int', default=0, nullable=True, comment='二级件数')
    lv2_price = Props(type='float', default=0.00, nullable=True, comment='二级单价')
    lv3_amount = Props(type='int', default=0, nullable=True, comment='三级件数')
    lv3_price = Props(type='float', default=0.00, nullable=True, comment='三级单价')

    @staticmethod
    def on_position_calculate(props, form, data):
        offer = data['offer']
        calculated_datas = []
        for item in data['raw_datas']:
            if item['position'] != offer['position']:
                continue
            work_amount = item['work_amount']
            if work_amount < props['lv2_amount']:
                wage_amount = work_amount * props['lv1_price']
            elif work_amount < props['lv3_amount']:
                wage_amount = props['lv2_amount'] * props['lv1_price'] + (work_amount - props['lv2_amount']) * props['lv2_price']
            else:
                wage_amount = props['lv2_amount'] * props['lv1_price'] + \
                              (props['lv3_amount'] - props['lv2_amount']) * props['lv2_price']\
                              + (work_amount - props['lv3_amount']) * props['lv3_price']
            work_rate = work_amount * 10000 / props['lv1_amount']
            calculated_datas.append({
                'proj_id': offer['proj_id'],
                'supplier_id': offer['supplier_id'],
                'offer_type': offer['offer_type'],
                'crew_id': item['crew_id'],
                'bill_id': item['bill_id'],
                'wage_time': item['wage_time'],
                'confirm_time': time.time(),
                'amount': wage_amount,
                'work_rate': work_rate
            })
        data['calculated_datas'].extend(calculated_datas)
        return Output(Output.OK, content=data)

