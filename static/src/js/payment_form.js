odoo.define('custom_task.payment_form', function (require) {
    "use strict";
    
    var PaymentForm = require('payment.payment_form');
        
    PaymentForm.include({    
    /**
     * @override
     */
     payEvent: function (ev) {
        ev.preventDefault();
        var dis_ids = document.getElementsByClassName('distributor')
        var checked_dis_id;
        Object.entries(dis_ids).forEach(item => {
            if(item[1].checked){
                checked_dis_id = item[1].value;
            }
          });
        this._rpc({
            model: 'sale.order',
            method: 'update_sales_destributor',
            args: [[],Number(checked_dis_id)],
        })
        return this._super.apply(this, arguments);
    },
});
});
